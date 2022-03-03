from pprint import pprint
import boto3


def transact_write_movie(dynamodb=None):
    if not dynamodb:
        #dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
        #dynamodb = boto3.resource('dynamodb')
        client = boto3.client('dynamodb')

    #table = dynamodb.Table('Movies')
    #doc: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html?highlight=transact_write_items#DynamoDB.Client.transact_write_items
    response = client.transact_write_items(
          TransactItems=[
             {
                "Put":{
                   "TableName":"Movies",
                   "Item":{
                      "year":{
                         "N":"2012"
                      },
                      "title":{
                         "S":"Prisoners"
                      },
                      "info":{
                         "M":{
                            "actors":{
                               "L":[
                                  {
                                     "S":"Hugh Jackman"
                                  },
                                  {
                                     "S":"Jake Gyllenhaal"
                                  },
                                  {
                                     "S":"Viola Davis"
                                  }
                               ]
                            },
                            "release_date":{
                               "S":"2013-08-30T00:00:00Z"
                            },
                            "plot":{
                               "S":"When Keller Dover's daughter and her friend go missing, he takes matters into his own hands as the police pursue multiple leads and the pressure mounts. But just how far will this desperate father go to protect his family?"
                            },
                            "genres":{
                               "L":[
                                  {
                                     "S":"Crime"
                                  },
                                  {
                                     "S":"Drama"
                                  },
                                  {
                                     "S":"Thriller"
                                  }
                               ]
                            },
                            "image_url":{
                               "S":"http://ia.media-imdb.com/images/M/MV5BMTg0NTIzMjQ1NV5BMl5BanBnXkFtZTcwNDc3MzM5OQ@@._V1_SX400_.jpg"
                            },
                            "directors":{
                               "L":[
                                  {
                                     "S":"Denis Villeneuve"
                                  }
                               ]
                            },
                            "rating":{
                               "N":"8.2"
                            },
                            "rank":{
                               "N":"3"
                            },
                            "running_time_secs":{
                               "N":"9180"
                            }
                         }
                      }
                   },
                   "ConditionExpression":"#pk <> :pkValue AND #sk <> :skValue",
                   "ExpressionAttributeNames":{
                      "#pk":"year",
                      "#sk":"title"
                   },
                   "ExpressionAttributeValues":{
                      ":pkValue":{
                         "N":"2012"
                      },
                      ":skValue":{
                         "S":"Prisoners"
                      }
                   }
                }
             },
             {
                "Delete":{
                   "TableName":"Movies",
                   "Key":{
                      "year":{
                         "N":"2013"
                      },
                      "title":{
                         "S":"Prisoners"
                      }
                   }
                }
             }
          ]
    )
    return response


if __name__ == '__main__':
    movie_resp = transact_write_movie()
    print("Put movie succeeded:")
    pprint(movie_resp, sort_dicts=False)
