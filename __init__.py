from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

app = Flask(__name__)

app.config["SECRET_KEY"] = b'5eed9b976f6d5c80fb8bb74b1bcff9f01218a864d0f2dd76143356d3cc36eda8'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://acd2022:acd2022@10.59.80.90:2022/collectivities'

db = SQLAlchemy()
db.init_app(app)
metadata = MetaData(bind=db)

from app_coll import routes
