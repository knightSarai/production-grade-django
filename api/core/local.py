from .settings import *

INSTALLED_APPS += [
    'corsheaders',
]

# Insert middleware before CommonMiddleware
MIDDLEWARE.insert(2, 'corsheaders.middleware.CorsMiddleware')

CSRF_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_HTTPONLY = False
SESSION_COOKIE_HTTPONLY = True

CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_ORIGIN", default=[]).split(" ")
CORS_ALLOWED_ORIGINS = os.environ.get("CSRF_ORIGIN", default=[]).split(" ")
CORS_EXPOSE_HEADERS = ['Content-Type', 'X-CSRFToken']

print("CSRF_TRUSTED_ORIGINS", CSRF_TRUSTED_ORIGINS)
print("CORS_ALLOWED_ORIGINS", CORS_ALLOWED_ORIGINS)

CORS_ALLOW_CREDENTIALS = True


print("MIDDLEWARE", MIDDLEWARE)
