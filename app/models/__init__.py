from flask_sqlalchemy import SQLAlchemy

from app.application import application

db = SQLAlchemy(application)