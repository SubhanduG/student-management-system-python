import os
from flask import Flask
from backend.app.config import Config
from backend.app.extensions import cors
from backend.app.routes.auth import auth_bp
from backend.app.routes.students import students_bp
from backend.app.routes.pages import pages_bp


def create_app():
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "..", "..", "frontend",
                "templates"), static_folder=os.path.join(BASE_DIR, "..", "..", "frontend", "static"))
    app.config.from_object(Config)

    cors.init_app(app, supports_credentials=True)

    app.register_blueprint(pages_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(students_bp)

    return app
