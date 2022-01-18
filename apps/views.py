from apps import app
from apps.user_api_v1.views import user_bp

app.register_blueprint(user_bp)
