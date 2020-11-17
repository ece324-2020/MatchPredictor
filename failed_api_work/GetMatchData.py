import http.client
import pandas
import json

seasons = list(range(2020,2017, -1))          #CONTACT DEV, ONLY SEASONS 2020-2018 available

#print(seasons)

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': 'c578d9631c68411884e3cd1280bd340e' }
matches = []

for season in seasons:                  #can only collect matches from a single season at a time    
    connection.request('GET', '/v2/competitions/PL/matches?season={}&status=FINISHED'.format(season), None, headers )
    response = json.loads(connection.getresponse().read().decode())
    matches = matches + response['matches']

print(matches)
#print(response['filters'])
#print(response['count'])
df = pandas.DataFrame(matches)
#print("hi")
df.to_csv('raw_pl_match_get_data.csv')
