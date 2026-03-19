# Database & Dependency Security Reference

## SQL Injection Prevention

### Parameterized Queries (Every Database)

```javascript
// PostgreSQL (pg)
const { rows } = await pool.query(
  'SELECT * FROM users WHERE email = $1 AND org_id = $2',
  [email, orgId]
);

// MySQL (mysql2)
const [rows] = await connection.execute(
  'SELECT * FROM users WHERE email = ? AND org_id = ?',
  [email, orgId]
);

// SQLite (better-sqlite3)
const user = db.prepare('SELECT * FROM users WHERE id = ?').get(userId);
```

### ORM Security

```javascript
// Prisma — safe by default
const user = await prisma.user.findUnique({ where: { id: userId } });
const users = await prisma.user.findMany({
  where: { name: { contains: searchTerm } } // Auto-parameterized
});

// DANGER: Raw queries bypass ORM protection
// Only use when necessary, ALWAYS parameterize
const result = await prisma.$queryRaw`
  SELECT * FROM users WHERE id = ${userId}
`; // Tagged template — Prisma parameterizes this

// WRONG — string concatenation in raw query
// await prisma.$queryRawUnsafe(`SELECT * FROM users WHERE id = ${userId}`);
```

```javascript
// Knex — query builder (safe)
const users = await knex('users')
  .where('email', email)
  .andWhere('status', 'active')
  .select('id', 'name', 'email');

// Knex — raw (parameterize manually)
const users = await knex.raw('SELECT * FROM users WHERE id = ?', [userId]);
```

```javascript
// TypeORM
const user = await userRepo.findOne({ where: { id: userId } });

// TypeORM — QueryBuilder (safe)
const users = await userRepo
  .createQueryBuilder('user')
  .where('user.email = :email', { email })
  .getMany();
```

### MongoDB Injection Prevention

```javascript
// Mongoose — safe with schema validation
const user = await User.findById(userId); // ObjectId validated

// DANGER: $where and $regex with user input
// WRONG:
// await User.find({ $where: `this.name == '${name}'` });

// CORRECT: Use structured queries
await User.find({ name: { $eq: name } });

// Sanitize query operators — block $ prefix in user input
function sanitizeMongoInput(input) {
  if (typeof input === 'object' && input !== null) {
    for (const key of Object.keys(input)) {
      if (key.startsWith('$')) delete input[key];
    }
  }
  return input;
}
```

---

## Connection Security

### Encrypted Connections
```javascript
// PostgreSQL with SSL
const pool = new Pool({
  host: process.env.DB_HOST,
  port: process.env.DB_PORT,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
  ssl: {
    rejectUnauthorized: true, // Verify server certificate
    ca: fs.readFileSync('/path/to/ca-cert.pem')
  },
  max: 20
});

// MySQL with SSL
const pool = mysql.createPool({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
  ssl: { rejectUnauthorized: true }
});
```

### Connection String Security
```javascript
// NEVER hardcode credentials
// WRONG: const db = connect('postgres://admin:password@host/db');

// Use env vars
const db = connect(process.env.DATABASE_URL);

// Validate at startup
if (!process.env.DATABASE_URL) {
  console.error('DATABASE_URL not set');
  process.exit(1);
}
```

### Connection Pool Limits
```javascript
const pool = new Pool({
  max: 20,                          // Max connections
  idleTimeoutMillis: 30000,         // Close idle connections after 30s
  connectionTimeoutMillis: 5000,    // Fail fast if can't connect
  allowExitOnIdle: true
});

// Always release connections
const client = await pool.connect();
try {
  const result = await client.query('SELECT * FROM users WHERE id = $1', [id]);
  return result.rows;
} finally {
  client.release(); // ALWAYS release, even on error
}
```

---

## Field-Level Encryption

```javascript
const crypto = require('crypto');

// Encrypt sensitive columns before storage
class FieldEncryption {
  constructor(masterKey) {
    this.key = crypto.scryptSync(masterKey, 'field-encrypt-salt', 32);
  }

  encrypt(value) {
    const iv = crypto.randomBytes(16);
    const cipher = crypto.createCipheriv('aes-256-gcm', this.key, iv);
    const encrypted = Buffer.concat([cipher.update(value, 'utf8'), cipher.final()]);
    const tag = cipher.getAuthTag();
    return Buffer.concat([iv, tag, encrypted]).toString('base64');
  }

  decrypt(ciphertext) {
    const buf = Buffer.from(ciphertext, 'base64');
    const iv = buf.subarray(0, 16);
    const tag = buf.subarray(16, 32);
    const data = buf.subarray(32);
    const decipher = crypto.createDecipheriv('aes-256-gcm', this.key, iv);
    decipher.setAuthTag(tag);
    return decipher.update(data, undefined, 'utf8') + decipher.final('utf8');
  }
}

// Usage with ORM
const fieldCrypto = new FieldEncryption(process.env.FIELD_ENCRYPTION_KEY);

// Before save
user.ssn = fieldCrypto.encrypt(plainSSN);
await user.save();

// After read
const plainSSN = fieldCrypto.decrypt(user.ssn);
```

---

## Dependency Supply Chain Security

### Lock Files — Always Commit
```bash
# These MUST be in version control
package-lock.json    # npm
yarn.lock           # yarn
pnpm-lock.yaml      # pnpm
Cargo.lock          # Rust

# CI: Use lockfile-only installs
npm ci              # NOT npm install
yarn --frozen-lockfile
pnpm install --frozen-lockfile
```

### Dependency Auditing
```bash
# Run regularly (weekly minimum, on every CI build ideally)
npm audit
npm audit fix --audit-level=high

# More comprehensive tools
npx snyk test
npx retire

# Check for known malicious packages
npx npm-check-updates --upgrade
```

### Version Pinning Strategy
```json
{
  "dependencies": {
    "express": "4.18.2",       // Exact pin for critical deps
    "cors": "^2.8.5",          // Minor/patch for trusted deps
    "lodash": "~4.17.21"       // Patch only for stable deps
  }
}
```

**Rules:**
- Pin exact versions for security-critical packages (auth, crypto, DB drivers)
- Use `^` for well-maintained packages you trust
- Never use `*` or `latest`
- Review changelogs before major version bumps

### Subresource Integrity (SRI) for CDN

```html
<!-- Always use SRI for CDN-loaded scripts -->
<script
  src="https://cdn.example.com/lib.js"
  integrity="sha384-oqVuAfXRKap7fdgcCY5..."
  crossorigin="anonymous"
></script>

<!-- Generate SRI hash -->
<!-- openssl dgst -sha384 -binary lib.js | openssl base64 -A -->
```

### .gitignore Security Essentials
```
# Secrets — never commit
.env
.env.local
.env.*.local
*.pem
*.key
*.p12
credentials.json
service-account.json

# Dependencies — don't commit
node_modules/
vendor/

# Build artifacts
.trigger/
dist/
build/
```

### Supply Chain Attack Prevention
- Review new dependencies before adding (check maintainers, download count, last update)
- Use `npm audit signatures` to verify package provenance
- Enable 2FA on your npm account
- Use scoped packages for internal code (@myorg/package)
- Monitor for typosquatting (lodash vs l0dash)
- Consider using a private registry for critical projects
- Set up Dependabot or Renovate for automated security updates

---

## Database Security Checklist

- [ ] All queries use parameterized statements or ORM
- [ ] No raw SQL with string concatenation
- [ ] Database connections use SSL/TLS
- [ ] Connection strings from env vars, not hardcoded
- [ ] Connection pool limits configured
- [ ] Connections always released (try/finally pattern)
- [ ] Sensitive fields encrypted at rest
- [ ] Database user has minimum required privileges
- [ ] No default/weak database passwords
- [ ] Regular backups with encryption
- [ ] Audit logging for sensitive operations
