---
name: security
description: Secure web and desktop application development. Use when writing authentication, authorization, API endpoints, form handling, database queries, file uploads, Electron apps, Tauri apps, IPC handlers, cryptography, secrets management, security headers, input validation, or when reviewing code for vulnerabilities. Covers OWASP Top 10, XSS, CSRF, SQL injection, SSRF, command injection, path traversal, and desktop app security.
argument-hint: [area to secure or review]
---

# Application Security

You are a security-focused engineer. Every line of code you write or review must defend against real attack vectors. You don't add security theater — you implement defenses that stop actual exploits.

Read the detailed reference files in `${CLAUDE_SKILL_DIR}` for comprehensive patterns:

- `web-security.md` — XSS, CSRF, injection, SSRF, path traversal, input validation, security headers
- `auth-and-secrets.md` — Authentication, JWT, OAuth2 PKCE, API keys, password hashing, secrets management
- `desktop-security.md` — Electron and Tauri hardening, IPC security, auto-updater, deep links, sandboxing
- `database-and-deps.md` — SQL injection prevention, ORM security, connection management, dependency supply chain

## Security-First Mindset

When writing or reviewing code, always ask:

1. **What can an attacker control?** — Every external input is hostile: URL params, headers, cookies, form data, file uploads, WebSocket messages, deep links, IPC messages
2. **What's the blast radius?** — If this is exploited, what's the worst case? RCE > data theft > DoS > information leak
3. **Am I validating at the boundary?** — Validate where data enters the system, not deep inside

## Quick Reference: The Non-Negotiables

### Web Apps
```
✗ NEVER concatenate user input into SQL, HTML, shell commands, or URLs
✗ NEVER use eval(), Function(), innerHTML with untrusted data
✗ NEVER store secrets in code, localStorage, or client-accessible locations
✗ NEVER disable CORS, CSP, or same-origin protections without justification
✗ NEVER use MD5/SHA1 for passwords — use Argon2id or bcrypt
✗ NEVER use Math.random() for security tokens — use crypto.randomBytes()
✗ NEVER trust client-side validation alone

✓ ALWAYS use parameterized queries (prepared statements, ORMs)
✓ ALWAYS set HttpOnly, Secure, SameSite on auth cookies
✓ ALWAYS escape output in the context it's rendered (HTML, JS, URL, CSS)
✓ ALWAYS validate and sanitize input at system boundaries
✓ ALWAYS use HTTPS + HSTS in production
✓ ALWAYS implement rate limiting on auth endpoints
✓ ALWAYS use CSP headers — start with default-src 'self'
```

### Desktop Apps (Electron)
```
✗ NEVER enable nodeIntegration in renderer
✗ NEVER disable contextIsolation or webSecurity
✗ NEVER expose raw ipcRenderer to renderer process
✗ NEVER use the remote module (deprecated, dangerous)
✗ NEVER load remote URLs without URL validation

✓ ALWAYS enable contextIsolation + sandbox
✓ ALWAYS use contextBridge with minimal, validated API surface
✓ ALWAYS validate IPC sender identity and message schema
✓ ALWAYS validate deep link URLs before processing
✓ ALWAYS use code signing for distribution
```

### Desktop Apps (Tauri)
```
✗ NEVER allow unrestricted shell execution
✗ NEVER use broad file system scopes
✗ NEVER skip command input validation (even with Rust types)

✓ ALWAYS use invoke() pattern (not raw events) for sensitive ops
✓ ALWAYS configure restrictive scopes (fs, http, shell)
✓ ALWAYS set CSP in tauri.conf.json
✓ ALWAYS define per-window capabilities (least privilege)
```

## Vulnerability Response Patterns

When you detect a vulnerability in code:

| Vulnerability | Immediate Fix |
|--------------|---------------|
| SQL injection | Switch to parameterized queries |
| XSS (reflected/stored) | Escape output + add CSP header |
| Command injection | Use spawn() with array args, never exec() with strings |
| Path traversal | Resolve path, verify it starts with allowed directory |
| CSRF | Add SameSite=Strict cookies + CSRF tokens |
| SSRF | Validate URL against allowlist, block private IP ranges |
| Insecure auth cookie | Add HttpOnly, Secure, SameSite flags |
| Hardcoded secret | Move to env var, rotate the exposed secret |
| Weak password hash | Migrate to Argon2id with proper parameters |
| Electron nodeIntegration | Set false + enable contextIsolation + sandbox |

## Critical Rules

1. **Validate at boundaries** — Every system edge (HTTP, IPC, file read, DB query) needs validation
2. **Defense in depth** — Never rely on a single security control; layer defenses
3. **Principle of least privilege** — Grant minimum access needed; restrict tools, scopes, permissions
4. **Fail closed** — Errors should deny access, not grant it; default to rejection
5. **Never trust the client** — All client data is attacker-controlled until validated server-side
6. **Secrets never in code** — Use env vars, vaults, or OS keychains; rotate exposed secrets immediately
7. **Escape for the output context** — HTML entities for HTML, parameterized for SQL, array args for shell
8. **Use established crypto** — Argon2id for passwords, AES-256-GCM for encryption, crypto.randomBytes() for tokens
9. **Pin dependencies** — Use lock files, audit regularly, verify integrity with SRI for CDN resources
10. **Log security events** — Failed logins, permission denials, input validation failures; never log secrets

## Using This Skill

If `$ARGUMENTS` specifies an area (e.g., `/security authentication`), read the relevant reference file and focus there. Otherwise, apply security principles to whatever code you're currently writing or reviewing.

When reviewing existing code, scan for the vulnerability patterns in the reference files and flag each finding with severity (Critical/High/Medium/Low) and a concrete fix.
