from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    CORS(app)

    load_dotenv()

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from app.modules.item.api import item_bp
    app.register_blueprint(item_bp, url_prefix='/api/items')

    from app.modules.item import model  

    return app