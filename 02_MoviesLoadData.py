from __future__ import print_function  # Python 2/3 compatibility
import boto3
import json
import decimal
import os

dynamodb = boto3.resource(
    'dynamodb',
    region_name='ap-southeast-1'
)

table = dynamodb.Table('Movies')


file_moviedata = os.path.dirname(os.path.realpath(__file__)) + '\moviedata.json'

with open(file_moviedata) as json_file:
    movies = json.load(json_file, parse_float=decimal.Decimal)
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        info = movie['info']

        print("Adding movie:", year, title)

        table.put_item(
            Item={
                'year': year,
                'title': title,
                'info': info,
            }
        )
