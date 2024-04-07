from flask import Flask
from .config import DevelopmentConfig

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    from .routes.sheets_api import sheets_bp
    app.register_blueprint(sheets_bp, url_prefix='/api')

    return app
