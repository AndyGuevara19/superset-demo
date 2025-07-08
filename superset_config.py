import os

SECRET_KEY = os.environ.get("SUPERSET_SECRET_KEY", "clave_super_secreta_123")

# Auth
AUTH_TYPE = 1  # AUTH_DB
AUTH_ROLE_PUBLIC = "Public"
PUBLIC_ROLE_LIKE_GAMMA = True

# Embed y flags
FEATURE_FLAGS = {
    "EMBEDDABLE_DASHBOARDS": True,
    "EMBEDDED_SUPERSET": True,
    "DASHBOARD_NATIVE_FILTERS": True,
    "ENABLE_TEMPLATE_PROCESSING": True,
    "ENABLE_REACT_CRUD_VIEWS": True,
    "ALLOW_PUBLIC_DATASETS": True,
    "ENABLE_EXPLORE_DRAG_AND_DROP": True,
}

# CORS para permitir GitHub Pages (¡importante!)
ENABLE_CORS = True
CORS_OPTIONS = {
    "supports_credentials": True,
    "origins": ["https://andyguevara19.github.io"],
    "methods": ["GET", "POST", "OPTIONS"],
    "allow_headers": ["*"],
}

# Proxy para producción
ENABLE_PROXY_FIX = True
