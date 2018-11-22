
from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

# This queries the DB and returns all movies from a certain year

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000", aws_access_key_id='Secret', aws_secret_access_key='Secret')

table = dynamodb.Table('Movies')
year = raw_input('What is the year?> ')
print("Movies from ", year)

response = table.query(
    KeyConditionExpression=Key('year').eq(int(year))
)

for i in response['Items']:
    print(i['year'], ":", i['title'])