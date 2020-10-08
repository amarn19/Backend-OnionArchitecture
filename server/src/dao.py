from utility.logger import logger
import os

logger = logger()
db_type= os.getenv('DB_TYPE')
logger.info(db_type)

class Dao:
    def dataAccess(self,user,dashboard,*store,repository):
        if(db_type=='sqlLite'):
            logger.info('sqlLite')
        elif(db_type=='postgresql'):
            logger.info('postgresql')
        elif(db_type=='mysql'):
            logger.info('mysql')
        elif(db_type=='mangodb'):
            logger.info('mangodb')
        elif(db_type=='dynamodb'):
            item = {
            'pk': getattr(user,'username'),
            'sk': getattr(user,'user_type'),
            'type': 'user',
            'user_details': user.getUserDetails(),
            'dashboard': dashboard.getDashboard()
            }
            if getattr(user,'user_type') == "shopper":
                booking_history = getattr(dashboard,'bookings_history')
                item.update({'booking_history': booking_history})
            elif getattr(user,'user_type') == "store_owner":
                store_details = store.getStoreDetails()
                messages = getattr(user,'messages')
                item.update({'store_details': store_details, 'messages': messages})
            logger.info('dynamodb')
        elif(db_type=='rds'):
            logger.info('')
        elif(db_type=='dynamodb'):
            logger.info('dynamodb')