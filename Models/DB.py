from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

DB = Flask(__name__)

conn = DB.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:bansal31@localhost/FOOD_KART_SYSTEM'
db = SQLAlchemy(DB)

class USER(db.Model):

    'Class for creating user details'

    __tablename__ = 'user_detail'

    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    gender = Column(String(120),nullable=False)
    Phone_number = Column(Integer,unique=True)
    Pincode = Column(Integer,nullable=False)

