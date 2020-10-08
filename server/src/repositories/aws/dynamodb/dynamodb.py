import boto3
import os
from utility.logger import logger
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

# dynamodb instance creation
dynamodb = boto3.resource('dynamodb')

# fetching dynamodb table
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

# Logger configuration

logger = logger()

class Dynamodb:
    # createUser/createStore
    def newItem(self,item):
        try:
            response = table.put_item(
                Item=item,
                ConditionExpression='attribute_not_exists(pk) AND attribute_not_exists(sk)'
            )
            return response
        except (ClientError, KeyError) as e:
                raise
        