# HTTPS & Secure Redirects Implementation

## Settings Implemented
- `SECURE_SSL_REDIRECT = True` → Forces all HTTP → HTTPS
- `SECURE_HSTS_SECONDS = 31536000` → 1 year strict HTTPS
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True` → Covers all subdomains
- `SECURE_HSTS_PRELOAD = True` → Eligible for browser preload list
- `SESSION_COOKIE_SECURE = True` → Session cookies only over HTTPS
- `CSRF_COOKIE_SECURE = True` → CSRF cookies only over HTTPS
- `X_FRAME_OPTIONS = 'DENY'` → Anti-clickjacking
- `SECURE_CONTENT_TYPE_NOSNIFF = True` → Prevent MIME attacks
- `SECURE_BROWSER_XSS_FILTER = True` → Enable browser XSS protection

## Deployment
- Nginx configured with SSL/TLS (see `deployment/nginx_https.conf`)
- Let's Encrypt used for free certificates
- All traffic redirected from HTTP → HTTPS

## Testing
- http:// → automatically redirects to https://
- HSTS header present (check with curl -I https://yourdomain.com)
- Cookies marked "Secure"
- No mixed content warnings

## Benefits
- All data encrypted in transit
- Protection against MITM attacks
- Improved SEO and trust
- Compliance with modern security standards