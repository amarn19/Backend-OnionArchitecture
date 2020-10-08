from utility.logger import logger
from flask import request
from src.model.User import User
from src.model.Store import Store
from src.model.Dashboard import Dashboard
from src.service import Service
from app import app

logger = logger()
# Routes
#Create Delete user
service = None
response = ""
class Controller:   
    def __init__(self):
        print('Controller class')
        global service 
        service = Service()
        
    @app.route('/createUser',methods=["POST"])
    def createUser():
        try:
            global service,response
            logger.info('Calling createUser')
            data = request.json
            user = User(
            username = data.get('username'),
            user_type = data.get('user_type'),
            name = data['user_details']['name'],
            dob = data['user_details']['dob'],
            email = data['user_details']['email'],
            gender = data['user_details']['gender'],
            street = data['user_details']['address']['street'],
            province = data['user_details']['address']['province'],
            country = data['user_details']['address']['country'],
            phonenumber = data['user_details']['phonenumber']
            )
            dashboard = Dashboard(
            total_visits =  data['dashboard']['total_visits'],
            cancelled_visits = data['dashboard']['cancelled_visits'],
            upcoming_visits = data['dashboard']['upcoming_visits'],
            bookings_history = data.get('bookings_history'),
            messages = data['dashboard']['messages']
            )
            if(data.get('user_type')=='store_owner'):
                store = Store(
                    name = data['store_details']['name'],
                    establishedon = data['store_details']['establishedon'],
                    email = data['store_details']['email'],
                    size = data['store_details']['size'],
                    street = data['store_details']['street'],
                    province = data['store_details']['province'],
                    country = data['store_details']['country'],
                    phonenumber = data['store_details']['phonenumber']
                )
                response = service.handleService(user,dashboard,store)
            response = service.handleService(user,dashboard)
            if(response!=""):
                return 'User created'
            else:
                return 'User not created'
        except (Exception) as e:
            return e.response
    
    @app.route('/deleteUser')
    def deleteUser():
        logger.info('Calling deleteUser')
        return 'Hello, World!'

    #update record
    @app.route('/updateRecord')
    def updateRecord():
        logger.info('Calling updateRecord')
        return 'Hello, World!'

    #fetch user,users
    @app.route('/getUser')
    def getUser():
        logger.info('Calling getUser')
        return 'Hello, World!'
    @app.route('/getUsers')
    def getUsers():
        logger.info('Calling getUsers')
        return 'Hello, World!'

    #fetch store,stores
    @app.route('/getStore')
    def getStore():
        logger.info('Calling getStore')
        return 'Hello, World!'
    @app.route('/getStores')
    def getStores():
        logger.info('Calling getStores')
        return 'Hello, World!'
    
    #upload,fetch image
    @app.route('/uploadImage')
    def uploadImage():
        logger.info('Calling uploadImage')
        return 'Hello, World!'
    @app.route('/fetchImage')
    def fetchImage():
        logger.info('Calling fetchImage')
        return 'Hello, World!'