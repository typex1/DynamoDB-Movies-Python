from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key


def query_and_project_movies(year, title_range, dynamodb=None):
    if not dynamodb:
        #dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Movies')
    print(f"Get year, title, genres, and lead actor")

    # Expression attribute names can only reference items in the projection expression.
    response = table.query(
        ProjectionExpression="#yr, title, info.genres, info.actors[0]",
        ExpressionAttributeNames={"#yr": "year"},
        KeyConditionExpression=
            #Key('yea'r').eq(year) & Key('title').between(title_range[0], title_range[1])
            Key('year').between(2012, 2013)
    )
    return response['Items']


if __name__ == '__main__':
    query_year = 2013
    query_range = ('N', 'Z')
    print(f"Get movies from {query_year} with titles from "
          f"{query_range[0]} to {query_range[1]}")
    movies = query_and_project_movies(query_year, query_range)
    for movie in movies:
        print(f"\n{movie['year']} : {movie['title']}")
        pprint(movie['info'])
