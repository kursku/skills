# Desktop Application Security Reference

## Electron Security

### Secure Window Configuration
```javascript
const win = new BrowserWindow({
  webPreferences: {
    contextIsolation: true,        // Separate JS contexts (MANDATORY)
    nodeIntegration: false,         // No Node.js in renderer (MANDATORY)
    sandbox: true,                  // OS-level sandboxing (MANDATORY)
    webSecurity: true,              // Same-origin policy (MANDATORY)
    enableRemoteModule: false,      // Deprecated, dangerous
    preload: path.join(__dirname, 'preload.js'),
    allowRunningInsecureContent: false
  }
});
```

**What happens without these:**
- `nodeIntegration: true` → XSS becomes RCE (`require('child_process').exec()`)
- `contextIsolation: false` → Renderer can tamper with preload globals
- `sandbox: false` → Renderer has broader OS access
- `webSecurity: false` → Same-origin policy disabled, data theft possible

### Preload Script — Minimal API Surface

```javascript
// preload.js — expose ONLY specific, validated functions
const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('api', {
  loadPreferences: () => ipcRenderer.invoke('prefs:load'),
  savePreferences: (prefs) => {
    if (!prefs || typeof prefs !== 'object') throw new Error('Invalid prefs');
    return ipcRenderer.invoke('prefs:save', prefs);
  },
  openExternal: (url) => {
    if (typeof url !== 'string') throw new Error('Invalid URL');
    return ipcRenderer.invoke('shell:open-external', url);
  }
  // NEVER expose: ipcRenderer directly, require(), process, fs
});
```

### IPC Security — Validate Everything

```javascript
// main.js
const { ipcMain, shell } = require('electron');

ipcMain.handle('prefs:load', async (event) => {
  // Validate sender
  if (event.sender !== mainWindow.webContents) {
    throw new Error('Unauthorized sender');
  }
  return loadPreferences();
});

ipcMain.handle('prefs:save', async (event, prefs) => {
  if (event.sender !== mainWindow.webContents) throw new Error('Unauthorized');

  // Schema validation
  if (!prefs || typeof prefs !== 'object') throw new Error('Invalid data');
  if (typeof prefs.theme !== 'string') throw new Error('Invalid theme');

  return savePreferences(prefs);
});

ipcMain.handle('shell:open-external', async (event, url) => {
  if (event.sender !== mainWindow.webContents) throw new Error('Unauthorized');

  // URL validation — only allow HTTPS
  try {
    const parsed = new URL(url);
    if (!['https:', 'http:'].includes(parsed.protocol)) {
      throw new Error('Invalid protocol');
    }
  } catch { throw new Error('Invalid URL'); }

  return shell.openExternal(url);
});
```

### CSP for Electron

```javascript
// Set via webRequest (works with file:// protocol)
session.defaultSession.webRequest.onHeadersReceived((details, callback) => {
  callback({
    responseHeaders: {
      ...details.responseHeaders,
      'Content-Security-Policy': [
        "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self' https://api.myapp.com"
      ]
    }
  });
});
```

### Deep Link Security

```javascript
app.setAsDefaultProtocolClient('myapp');

app.on('open-url', (event, url) => {
  event.preventDefault();

  try {
    const parsed = new URL(url);

    // Validate protocol
    if (parsed.protocol !== 'myapp:') return;

    // Allowlist valid hosts
    const allowedHosts = ['auth', 'open', 'settings'];
    if (!allowedHosts.includes(parsed.hostname)) return;

    // Length limit
    if (url.length > 2000) return;

    // Sanitize params
    for (const [, value] of parsed.searchParams) {
      if (/[<>"'`;]/.test(value)) return; // Block injection chars
    }

    handleDeepLink(parsed);
  } catch {
    // Invalid URL — silently ignore
  }
});
```

### Auto-Updater Security

```javascript
const { autoUpdater } = require('electron-updater');

// Always HTTPS, always signed
autoUpdater.on('update-downloaded', async (info) => {
  const { response } = await dialog.showMessageBox(mainWindow, {
    type: 'info',
    buttons: ['Restart Now', 'Later'],
    message: `Update ${info.version} ready`
  });
  if (response === 0) autoUpdater.quitAndInstall();
});

autoUpdater.on('error', (err) => {
  // Never silently fail — don't install unverified updates
  console.error('Update failed:', err.message);
});

// Check after app is ready (not on startup — slows launch)
setTimeout(() => autoUpdater.checkForUpdates(), 30000);
```

### Credential Storage

```javascript
const { safeStorage } = require('electron');

function storeSecret(key, value) {
  if (!safeStorage.isEncryptionAvailable()) {
    throw new Error('Encryption not available');
  }
  const encrypted = safeStorage.encryptString(value);
  store.set(key, encrypted.toString('base64'));
}

function retrieveSecret(key) {
  const encrypted = Buffer.from(store.get(key), 'base64');
  return safeStorage.decryptString(encrypted);
}
```

### WebView / BrowserView / iframe

**Preference order (most to least secure):**
1. **iframe with sandbox** — best isolation for web content
2. **BrowserView** — Chromium-level isolation
3. **WebView tag** — deprecated, avoid

```javascript
// BrowserView with full security
const view = new BrowserView({
  webPreferences: {
    sandbox: true,
    contextIsolation: true,
    nodeIntegration: false
  }
});
```

### Electron Vulnerability Checklist
- [ ] `contextIsolation: true`
- [ ] `nodeIntegration: false`
- [ ] `sandbox: true`
- [ ] `webSecurity: true`
- [ ] No `remote` module usage
- [ ] Preload uses `contextBridge` with minimal API
- [ ] IPC validates sender AND message schema
- [ ] Deep links validated against allowlist
- [ ] Auto-updater uses HTTPS + code signing
- [ ] CSP headers configured
- [ ] No `eval()` or `Function()` in renderer
- [ ] Credentials stored via `safeStorage`

---

## Tauri Security

### Command Security

```rust
// Define commands with strict typing — Rust enforces at compile time
#[tauri::command]
async fn read_user_data(user_id: u32) -> Result<UserData, String> {
    if user_id == 0 {
        return Err("Invalid user ID".to_string());
    }
    db::get_user(user_id).map_err(|e| e.to_string())
}

// Register only needed commands
tauri::Builder::default()
    .invoke_handler(tauri::generate_handler![read_user_data])
    .run(tauri::generate_context!())
    .expect("error running app");
```

### Scope Configuration (tauri.conf.json)

```json
{
  "app": {
    "security": {
      "csp": "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'"
    }
  },
  "plugins": {
    "fs": {
      "scope": [{ "path": "$APPDATA/**", "allow": ["read", "write"] }]
    },
    "http": {
      "scope": [
        { "allow": ["https://api.myapp.com/**"] },
        { "deny": ["https://api.myapp.com/admin/**"] }
      ]
    },
    "shell": {
      "scope": [{ "name": "open", "allow": ["open"] }]
    }
  }
}
```

### Per-Window Capabilities

```json
{
  "security": {
    "capabilities": [
      {
        "windows": ["main"],
        "permissions": ["core:default", "fs:allow-read:$APPDATA"]
      },
      {
        "windows": ["settings"],
        "permissions": ["core:default", "fs:allow-read:$APPCONFIG"]
      },
      {
        "windows": ["untrusted"],
        "permissions": []
      }
    ]
  }
}
```

### Tauri Security Rules
- Use `invoke()` for sensitive operations (not events)
- Define restrictive scopes — deny by default
- Validate all command inputs even though Rust types help
- Configure CSP in tauri.conf.json
- Use per-window capabilities (least privilege)
- Audit third-party plugins before adding
- Code-sign all builds for distribution

### Tauri Vulnerability Checklist
- [ ] Commands validate all inputs
- [ ] File system scopes are restrictive
- [ ] HTTP scopes whitelist specific endpoints
- [ ] Shell scopes limit allowed commands
- [ ] CSP configured
- [ ] Per-window capabilities defined
- [ ] Plugins from trusted sources only
- [ ] Credentials in OS keychain (not plaintext files)
- [ ] Code signed for distribution
- [ ] Updates over HTTPS with signature verification

---

## Common Desktop Security Patterns

### Code Signing
- **Windows**: EV certificate (SmartScreen trusted) via Azure Key Vault
- **macOS**: Developer ID certificate + notarization
- **Linux**: GPG signing for packages
- **Never**: Commit private keys to version control

### Secure Auto-Update Flow
1. Check for updates over HTTPS only
2. Verify code signature of downloaded update
3. Verify checksum matches manifest
4. Ask user before installing (don't auto-install silently)
5. Fall back gracefully on verification failure

### Sandboxing Strategy
- Renderer processes: Always sandboxed
- Main process: Minimize direct OS access
- File access: Through validated IPC only
- Network access: Scoped to known endpoints
- Privileges: Minimum required per window/component
