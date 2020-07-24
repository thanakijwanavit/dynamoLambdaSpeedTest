import json
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, JSONAttribute, BinaryAttribute
from timeit import timeit

class PynamoTestTable(Model):
    '''a table to store the list of sensitive columns which was last read in pynamodb'''
    class Meta:
      table_name = 'speed-test-table'
      region = 'us-east-1'
    hashedPhone = UnicodeAttribute(hash_key = True)
    arn = UnicodeAttribute()
    name = UnicodeAttribute()
    versionId = UnicodeAttribute()
    sensitiveColumn = JSONAttribute()
# import requests


def lambda_handler(event, context):
    dummyObject = PynamoTestTable(hashedPhone='dummy', arn = 'dummyARN', name='dummyName', versionId='dummyVersion', sensitiveColumn=['col1', 'col2', 'col3'])
    saveTime = timeit(dummyObject.save(), number=100)
    loadTime = timeit(dummyObject.query('dummy'), number=100)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "saveTime": saveTime,
            "loadTime": loadTime
        }),
    }
