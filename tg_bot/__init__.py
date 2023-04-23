from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from config import AppConfig


app = Flask(__name__)
app.config.from_object(AppConfig)
app.secret_key = os.getenv('SECRET_KEY')
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from .views import *

with app.app_context():
    db.create_all()

# Получение списка таблиц для связи с соединением
# tables = db.get_tables_for_bind()


