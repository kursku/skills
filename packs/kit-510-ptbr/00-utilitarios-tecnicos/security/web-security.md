# Web Security Reference

## XSS (Cross-Site Scripting) Prevention

### Output Escaping by Context

**HTML context** — escape `& < > " '`:
```javascript
const escapeHtml = (text) => {
  const map = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' };
  return text.replace(/[&<>"']/g, m => map[m]);
};
```

**React/Vue/Svelte** — auto-escape by default. Dangerous exceptions:
```jsx
// React: dangerouslySetInnerHTML — sanitize first
import DOMPurify from 'dompurify';
<div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(html) }} />

// Vue: v-html — sanitize first
<div v-html="DOMPurify.sanitize(userContent)" />

// Svelte: {@html} — sanitize first
{@html DOMPurify.sanitize(html)}
```

**URL context** — validate protocol:
```javascript
function safeHref(url) {
  try {
    const parsed = new URL(url);
    return ['http:', 'https:', 'mailto:'].includes(parsed.protocol) ? url : '#';
  } catch { return '#'; }
}
```

### Content Security Policy (CSP)

```javascript
// Express + Helmet
const helmet = require('helmet');
app.use((req, res, next) => {
  res.locals.nonce = crypto.randomBytes(16).toString('hex');
  next();
});

app.use(helmet.contentSecurityPolicy({
  directives: {
    defaultSrc: ["'self'"],
    scriptSrc: ["'self'", (req, res) => `'nonce-${res.locals.nonce}'`],
    styleSrc: ["'self'", (req, res) => `'nonce-${res.locals.nonce}'`],
    imgSrc: ["'self'", 'data:', 'https:'],
    connectSrc: ["'self'"],
    frameSrc: ["'none'"],
    objectSrc: ["'none'"],
    upgradeInsecureRequests: []
  }
}));
```

**Never use:** `'unsafe-inline'`, `'unsafe-eval'`, or wildcard `*` for script-src.

---

## CSRF Prevention

### SameSite Cookies (primary defense)
```javascript
res.cookie('session', token, {
  httpOnly: true,
  secure: true,
  sameSite: 'Strict', // or 'Lax' for links from external sites
  maxAge: 3600000,
  path: '/'
});
```

### CSRF Tokens (defense in depth)
```javascript
const csrf = require('csurf');
app.use(csrf({ cookie: false })); // session-based, not cookie-based

// Include in forms
app.get('/form', (req, res) => {
  res.render('form', { csrfToken: req.csrfToken() });
});

// AJAX: send via header
fetch('/api/action', {
  method: 'POST',
  headers: { 'X-CSRF-Token': csrfToken },
  body: JSON.stringify(data)
});
```

---

## Injection Prevention

### SQL — Always Parameterize
```javascript
// Raw SQL — parameterized
db.query('SELECT * FROM users WHERE id = ? AND status = ?', [userId, status]);

// Knex query builder
const user = await knex('users').where({ id: userId }).first();

// Prisma ORM
const user = await prisma.user.findUnique({ where: { id: userId } });
```

### Command — Never Concatenate
```javascript
// WRONG: exec() parses through shell
exec(`convert ${userFile} output.png`); // command injection!

// CORRECT: spawn() with array args, no shell parsing
spawn('convert', [userFile, 'output.png']);

// CORRECT: execFile() — no shell
execFile('convert', [userFile, 'output.png']);
```

### Path Traversal — Resolve and Verify
```javascript
const path = require('path');
const UPLOADS_DIR = path.resolve('./uploads');

function safePath(userInput) {
  const resolved = path.resolve(UPLOADS_DIR, userInput);
  if (!resolved.startsWith(UPLOADS_DIR + path.sep) && resolved !== UPLOADS_DIR) {
    throw new Error('Path traversal blocked');
  }
  return resolved;
}
```

---

## SSRF Prevention

```javascript
function validateUrl(urlString) {
  const parsed = new URL(urlString);

  // HTTPS only
  if (parsed.protocol !== 'https:') return false;

  // Block private/internal IPs
  const blocked = ['localhost', '127.0.0.1', '0.0.0.0', '169.254', '10.', '172.16', '192.168', '[::1]'];
  if (blocked.some(b => parsed.hostname.startsWith(b) || parsed.hostname === b)) return false;

  // Allowlist approach (preferred)
  const allowed = ['api.example.com', 'cdn.example.com'];
  if (!allowed.includes(parsed.hostname)) return false;

  return true;
}
```

---

## Input Validation

### Schema Validation (Zod example)
```typescript
import { z } from 'zod';

const CreateUserSchema = z.object({
  email: z.string().email().max(255),
  name: z.string().min(1).max(100).trim(),
  age: z.number().int().min(0).max(150),
  role: z.enum(['user', 'admin']),
});

// In route handler
app.post('/users', (req, res) => {
  const result = CreateUserSchema.safeParse(req.body);
  if (!result.success) {
    return res.status(400).json({ error: result.error.flatten() });
  }
  // result.data is typed and validated
});
```

### File Upload Validation
```javascript
const multer = require('multer');
const upload = multer({
  limits: { fileSize: 5 * 1024 * 1024 }, // 5MB max
  fileFilter: (req, file, cb) => {
    const allowed = ['image/jpeg', 'image/png', 'image/webp'];
    if (!allowed.includes(file.mimetype)) {
      return cb(new Error('Invalid file type'));
    }
    cb(null, true);
  }
});

// Don't trust file extension — verify magic bytes
import { fileTypeFromBuffer } from 'file-type';

async function validateFile(buffer) {
  const type = await fileTypeFromBuffer(buffer);
  if (!type || !['image/jpeg', 'image/png', 'image/webp'].includes(type.mime)) {
    throw new Error('Invalid file type');
  }
}
```

---

## Security Headers

### Complete Header Set
```javascript
app.use(helmet()); // Sets most headers with sane defaults

// Additional manual headers
app.use((req, res, next) => {
  res.setHeader('Strict-Transport-Security', 'max-age=31536000; includeSubDomains; preload');
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('X-Frame-Options', 'DENY');
  res.setHeader('Referrer-Policy', 'strict-origin-when-cross-origin');
  res.setHeader('Permissions-Policy', 'geolocation=(), camera=(), microphone=()');
  next();
});

app.disable('x-powered-by');
```

### Header Reference

| Header | Value | Purpose |
|--------|-------|---------|
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains; preload` | Force HTTPS |
| `X-Content-Type-Options` | `nosniff` | Block MIME sniffing |
| `X-Frame-Options` | `DENY` | Prevent clickjacking |
| `Content-Security-Policy` | `default-src 'self'; script-src 'nonce-{N}'` | XSS prevention |
| `Referrer-Policy` | `strict-origin-when-cross-origin` | Limit referrer leakage |
| `Permissions-Policy` | `geolocation=(), camera=()` | Restrict browser features |

---

## CORS Configuration

```javascript
const cors = require('cors');

// WRONG: Allow everything
// app.use(cors()); // Allows all origins!

// CORRECT: Explicit allowlist
app.use(cors({
  origin: ['https://myapp.com', 'https://admin.myapp.com'],
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  credentials: true,
  maxAge: 86400
}));
```

---

## iframe Security

```html
<!-- Restrictive sandbox for untrusted content -->
<iframe
  src="https://trusted.com/embed"
  sandbox="allow-scripts allow-same-origin"
  allow="geolocation 'none'; camera 'none'; microphone 'none'"
  referrerpolicy="no-referrer"
></iframe>
```

**postMessage validation:**
```javascript
window.addEventListener('message', (event) => {
  if (event.origin !== 'https://trusted.com') return; // Verify origin!
  // Process event.data
});
```
