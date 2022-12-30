from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import Config

#######################################
# app.config['CONFIGURATION_VARIABLES']
#######################################

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    from .main.routes import main
    from .dirs.routes import dirs
    from .selectorlib_api.routes import selector
    from .users.routes import users

    app.register_blueprint(main)
    app.register_blueprint(dirs)
    app.register_blueprint(selector)
    app.register_blueprint(users)
    
    return app