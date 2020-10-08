from flask import Flask,request,redirect
from os.path import join, dirname
from dotenv import load_dotenv
from src.controller import Controller
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
Controller(app)     

#find out the db type 
#pass the repository object to controller
#write py test to test the functionalities
#onion architecture

# class App(Flask):
#     def __init__(self,*args, **kwargs):
#         super().__init__(*args, **kwargs)

# if __name__ == "__main__":
#     my_server = App(__name__)
#     my_server.run(port=5000)