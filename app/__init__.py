import os
from flask import Flask
from config import basedir


app = Flask(__name__)
app.config.from_object('config')



#this should always be at the bottom
from app import views