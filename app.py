import os
from flask import Flask
from pymongo import MongoClient
from routes import pages
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)
    client = MongoClient(os.getenv("MONGODB_URI"))
    app.db = client.get_default_database()   # client.get_default_database() client.tracker

    app.register_blueprint(pages)
    return app
