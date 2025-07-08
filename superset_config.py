import os
from flask_appbuilder.security.manager import AUTH_DB

# Clave secreta segura (puedes setearla como variable de entorno o dejar una fija para test)
SECRET_KEY = os.environ.get("SUPERSET_SECRET_KEY", "una_clave_super_segura_1234!@#")

# ------------------------------
# AUTHENTICATION
# ------------------------------
AUTH_TYPE = AUTH_DB  # Autenticación básica con usuario/contraseña
AUTH_ROLE_PUBLIC = "Public"
PUBLIC_ROLE_LIKE_GAMMA = True  # El rol "Public" se comporta como el rol Gamma (solo lectura)

# ------------------------------
# FEATURE FLAGS
# ------------------------------
FEATURE_FLAGS = {
    "EMBEDDABLE_DASHBOARDS": True,
    "ALLOW_PUBLIC_DATASETS": True,
    "DASHBOARD_RBAC": False,
    "SQL_VALIDATORS_BY_ENGINE": True,
    "ENABLE_TEMPLATE_PROCESSING": True,
    "ENABLE_REACT_CRUD_VIEWS": True,
    "ENABLE_EXPLORE_DRAG_AND_DROP": True,
    "ENABLE_ALERTS": False,
    "ENABLE_JAVASCRIPT_CONTROLS": False,
    "ENABLE_RESTRICTED_DATA_ACCESS": True,
}

# ------------------------------
# PERFORMANCE
# ------------------------------
ENABLE_TIME_ROTATE = True
SILENCE_FAB = False
ROW_LIMIT = 10000
SQL_MAX_ROW = 10000
SUPERSET_WEBSERVER_PORT = 8088

# ------------------------------
# LOGGING (opcional, para debug)
# ------------------------------
# LOG_LEVEL = "DEBUG"

# ------------------------------
# OTRAS OPCIONES
# ------------------------------
ENABLE_PROXY_FIX = True
SESSION_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_SECURE = False  # True si usas HTTPS

# Puedes agregar más configuraciones si lo necesitas
