from flask import Flask,request,redirect
from os.path import join, dirname
from dotenv import load_dotenv
from src.utility.logger import logger


# Create .env file path
dotenv_path = join(dirname(__file__), '.env')
# load file from the path
load_dotenv(dotenv_path)
logger = logger()


app = Flask(__name__)
logger.info('Flask application started')

@app.route('/')
def home():
    return 'homepage'

from src.controller import Controller
Controller() 
 
