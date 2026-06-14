import json
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

# Mapeia o caminho do config.json na raiz do projeto
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, '..', 'config.json')

# Inicializa as diretrizes buscando do arquivo local JSON
if os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH, 'r') as config_file:
        config_data = json.load(config_file)
    app.config['SECRET_KEY'] = config_data.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = config_data.get('SQLALCHEMY_DATABASE_URI')
else:
    app.config['SECRET_KEY'] = 'fallback-seguro-desenvolvimento-local'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login' 
login_manager.login_message_category = 'danger'

bcrypt = Bcrypt(app)

from todo_project import routes