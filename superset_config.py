import os
SECRET_KEY = os.environ.get("SUPERSET_SECRET_KEY", "tu_clave_ultra_secreta_123!@#")
ENABLE_PUBLIC_DASHBOARD = True
FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True,
    "ALLOW_JINJA_IN_DASHBOARD_FILTERS": True,
    "DASHBOARD_RBAC": True,
}
