# set FLASK_APP=app
# set FLASK_ENV=development
# set FLASK_DEBUG=1
# flask run

from flask import Flask
from config import Config
from app.extensions import db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.profile import bp as profile_bp
    app.register_blueprint(profile_bp, url_prefix='/profile')

    return app