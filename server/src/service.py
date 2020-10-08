import os
from utility.logger import logger
from src.repositories.aws.dynamodb.dynamodb import Dynamodb 
from src.dao import Dao

logger = logger()
db_type= os.getenv('DB_TYPE')
logger.info(db_type)

dao = None
dynamodb = None
class Service:
    def __init__(self):
        global dao, dynamodb
        dao = Dao()
        dynamodb = Dynamodb()
        
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
            try:
                logger.info('dynamodb')
                global dao, dynamodb
                response = dao.dataAccess(user,dashboard,dynamodb)
                return response
            except (Exception) as e:
                raise
        elif(db_type=='rds'):
            logger.info('')
        elif(db_type=='dynamodb'):
            logger.info('dynamodb')
        