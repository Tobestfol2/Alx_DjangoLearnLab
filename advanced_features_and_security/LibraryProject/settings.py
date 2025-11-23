# LibraryProject/settings.py
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your-very-strong-secret-key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'yourdomain.com', '.ngrok.io']

# ==================== HTTPS & SECURE REDIRECTS (ALX REQUIRED) ====================
SECURE_SSL_REDIRECT = True                      # Redirect HTTP → HTTPS
SECURE_HSTS_SECONDS = 31536000                  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True          # Apply to all subdomains
SECURE_HSTS_PRELOAD = True                      # Allow HSTS preload

# Secure Cookies
SESSION_COOKIE_SECURE = True                    # Only send over HTTPS
CSRF_COOKIE_SECURE = True                       # Only send over HTTPS

# Secure Headers
X_FRAME_OPTIONS = 'DENY'                        # Prevent clickjacking
SECURE_CONTENT_TYPE_NOSNIFF = True              # Prevent MIME sniffing
SECURE_BROWSER_XSS_FILTER = True                # Enable browser XSS filter

# Extra recommended
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# =================================================================================