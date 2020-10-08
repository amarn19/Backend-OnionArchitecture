import os
from utility.logger import logger
from src.repositories.aws.dynamodb.dynamodb import Dynamodb 
from src.dao import Dao

logger = logger()
db_type= os.getenv('DB_TYPE')
logger.info(db_type)

class Service:
    def __init__(self):
        self.dao = Dao()
        self.dynamodb = Dynamodb()
        
    def handleService(self,user,dashboard,*store):
        if(db_type=='sqlLite'):
            logger.info('sqlLite')
        elif(db_type=='postgresql'):
            logger.info('postgresql')
        elif(db_type=='mysql'):
            logger.info('mysql')
        elif(db_type=='mangodb'):
            logger.info('mangodb')
        elif(db_type=='dynamodb'):
            self.dao.dataAccess(user,dashboard,self.dynamodb)
            logger.info('dynamodb')
        elif(db_type=='rds'):
            logger.info('')
        elif(db_type=='dynamodb'):
            logger.info('dynamodb')
        