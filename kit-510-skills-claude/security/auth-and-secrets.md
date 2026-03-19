# Authentication & Secrets Management Reference

## Password Hashing

### Argon2id (Recommended — 2025 standard)
```javascript
const argon2 = require('argon2');

async function hashPassword(password) {
  return argon2.hash(password, {
    type: argon2.argon2id,
    memoryCost: 65536,   // 64 MB
    timeCost: 3,
    parallelism: 4
  });
}

async function verifyPassword(hash, password) {
  return argon2.verify(hash, password);
}

// Login — never reveal which field was wrong
async function login(email, password) {
  const user = await db.findUser(email);
  if (!user || !(await verifyPassword(user.passwordHash, password))) {
    throw new Error('Invalid credentials'); // Same message for both cases
  }
  return user;
}
```

### bcrypt (Acceptable alternative)
```javascript
const bcrypt = require('bcrypt');
const SALT_ROUNDS = 12; // Minimum 10, prefer 12+

const hash = await bcrypt.hash(password, SALT_ROUNDS);
const valid = await bcrypt.compare(password, hash);
```

**Never use:** MD5, SHA1, SHA256 (without key stretching), or plain text for passwords.

---

## JWT Authentication

### Short-Lived Access + Refresh Token Pattern
```javascript
const jwt = require('jsonwebtoken');

function createAccessToken(userId) {
  return jwt.sign({ sub: userId }, process.env.JWT_SECRET, {
    expiresIn: '15m',
    algorithm: 'HS256'
  });
}

function createRefreshToken(userId) {
  return jwt.sign({ sub: userId }, process.env.REFRESH_SECRET, {
    expiresIn: '7d',
    algorithm: 'HS256'
  });
}

// Middleware
function authenticate(req, res, next) {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).json({ error: 'No token' });

  try {
    req.user = jwt.verify(token, process.env.JWT_SECRET);
    next();
  } catch (err) {
    if (err.name === 'TokenExpiredError') {
      return res.status(401).json({ error: 'Token expired' });
    }
    return res.status(401).json({ error: 'Invalid token' });
  }
}

// Refresh endpoint — refresh token in HttpOnly cookie
app.post('/auth/refresh', (req, res) => {
  const refreshToken = req.cookies.refreshToken;
  try {
    const decoded = jwt.verify(refreshToken, process.env.REFRESH_SECRET);
    const newAccess = createAccessToken(decoded.sub);
    res.json({ accessToken: newAccess });
  } catch {
    res.clearCookie('refreshToken');
    res.status(401).json({ error: 'Invalid refresh token' });
  }
});
```

### JWT Security Rules
- Access tokens: 15 minutes max
- Refresh tokens: HttpOnly cookie, 7 days max, rotate on use
- Never store JWTs in localStorage (XSS-accessible)
- Always verify `algorithm` — don't accept `none`
- Include `sub` (subject), `iat` (issued at), `exp` (expiry) claims

---

## OAuth2 with PKCE

```javascript
const crypto = require('crypto');

// Generate PKCE values
const codeVerifier = crypto.randomBytes(32).toString('base64url');
const codeChallenge = crypto.createHash('sha256').update(codeVerifier).digest('base64url');

// Step 1: Redirect to provider
app.get('/auth/login', (req, res) => {
  const state = crypto.randomBytes(32).toString('base64url');
  req.session.oauthState = state;
  req.session.codeVerifier = codeVerifier;

  const params = new URLSearchParams({
    client_id: process.env.OAUTH_CLIENT_ID,
    redirect_uri: 'https://myapp.com/auth/callback',
    response_type: 'code',
    scope: 'openid profile email',
    state,
    code_challenge: codeChallenge,
    code_challenge_method: 'S256'
  });

  res.redirect(`https://provider.com/authorize?${params}`);
});

// Step 2: Handle callback
app.get('/auth/callback', async (req, res) => {
  // Verify state (CSRF protection)
  if (req.query.state !== req.session.oauthState) {
    return res.status(403).send('Invalid state');
  }

  const response = await fetch('https://provider.com/token', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({
      grant_type: 'authorization_code',
      code: req.query.code,
      code_verifier: req.session.codeVerifier,
      client_id: process.env.OAUTH_CLIENT_ID,
      redirect_uri: 'https://myapp.com/auth/callback'
    })
  });

  const tokens = await response.json();
  // Verify ID token, create session
});
```

---

## API Key Security

```javascript
const crypto = require('crypto');

// Generate: prefix + random bytes
function generateApiKey() {
  return `sk_live_${crypto.randomBytes(32).toString('hex')}`;
}

// Store: hash only, never plaintext
function hashApiKey(key) {
  return crypto.createHash('sha256').update(key).digest('hex');
}

// Verify middleware
async function apiKeyAuth(req, res, next) {
  const key = req.headers.authorization?.replace('Bearer ', '');
  if (!key) return res.status(401).json({ error: 'Missing API key' });

  const hash = hashApiKey(key);
  const record = await db.apiKeys.findOne({ hash });
  if (!record) return res.status(401).json({ error: 'Invalid API key' });

  req.userId = record.userId;
  next();
}
```

---

## Rate Limiting

```javascript
const rateLimit = require('express-rate-limit');

// General API limiter
app.use('/api/', rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100,
  standardHeaders: true,
  legacyHeaders: false
}));

// Strict auth limiter
app.use('/auth/login', rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5,
  skipSuccessfulRequests: true,
  message: { error: 'Too many login attempts, try again later' }
}));

// Tiered limiting
app.use('/api/v1/', rateLimit({
  windowMs: 60 * 1000,
  max: (req) => {
    if (req.user?.tier === 'premium') return 1000;
    if (req.user?.tier === 'pro') return 500;
    return 100;
  }
}));
```

---

## Secrets Management

### Environment Variables
```javascript
require('dotenv').config();

// Validate required secrets at startup
const REQUIRED = ['JWT_SECRET', 'DB_PASSWORD', 'OAUTH_CLIENT_SECRET'];
for (const key of REQUIRED) {
  if (!process.env[key]) {
    console.error(`Missing required env var: ${key}`);
    process.exit(1);
  }
}

// Never log secrets
function sanitizeForLogging(env) {
  const sensitive = ['PASSWORD', 'SECRET', 'KEY', 'TOKEN'];
  return Object.fromEntries(
    Object.entries(env).map(([k, v]) => [
      k, sensitive.some(s => k.includes(s)) ? '[REDACTED]' : v
    ])
  );
}
```

### .env Security
```bash
# .env.example (committed — no real values)
DB_PASSWORD=CHANGE_ME
JWT_SECRET=CHANGE_ME

# .env (gitignored — real values)
DB_PASSWORD=actual-secret
JWT_SECRET=actual-secret
```

**.gitignore must contain:**
```
.env
.env.local
.env.*.local
*.pem
*.key
```

---

## Cryptography Essentials

### Secure Random Generation
```javascript
const crypto = require('crypto');

// Session tokens, CSRF tokens, API keys
const token = crypto.randomBytes(32).toString('hex');

// Numeric codes (OTP, verification)
const code = crypto.randomInt(100000, 999999).toString();

// NEVER use Math.random() for security purposes
```

### AES-256-GCM Encryption
```javascript
const ALGO = 'aes-256-gcm';

function encrypt(plaintext, key) {
  const iv = crypto.randomBytes(16);
  const cipher = crypto.createCipheriv(ALGO, key, iv);
  const encrypted = Buffer.concat([cipher.update(plaintext, 'utf8'), cipher.final()]);
  const tag = cipher.getAuthTag();
  return Buffer.concat([iv, tag, encrypted]).toString('base64');
}

function decrypt(ciphertext, key) {
  const buf = Buffer.from(ciphertext, 'base64');
  const iv = buf.subarray(0, 16);
  const tag = buf.subarray(16, 32);
  const encrypted = buf.subarray(32);
  const decipher = crypto.createDecipheriv(ALGO, key, iv);
  decipher.setAuthTag(tag);
  return decipher.update(encrypted, undefined, 'utf8') + decipher.final('utf8');
}
```

### Crypto Rules
- **Passwords**: Argon2id (preferred) or bcrypt (minimum rounds: 12)
- **Encryption**: AES-256-GCM (authenticated encryption)
- **Hashing**: SHA-256 for integrity, HMAC-SHA256 for signatures
- **Randomness**: Always `crypto.randomBytes()`, never `Math.random()`
- **Key derivation**: `crypto.scryptSync()` or HKDF
- **Never**: Roll your own crypto, use ECB mode, use MD5/SHA1 for security
