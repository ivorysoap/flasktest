from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)  # Load config settings from config class in config.py

from app import routes