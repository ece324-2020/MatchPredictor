### Collect match, team, and player data from https://api.footystats.org ###

import requests
import pandas as pd
import json
import time

URL = "https://api.footystats.org"  # non-changing base url

# Find season id's for specified league(s), league name must be looked up beforehand
def getLeagueIds(leagueName):
    response = requests.get(URL + '/league-list', params={'key': 'test85g57'})

    leagues = response.json()['data']
    seasonIds = []
    for league in leagues:
        if league['name'] == leagueName:
            for season in league['season']:
                seasonIds.append(season['id'])
            
            break  # no need to keep searching league list

    return seasonIds

def getMatchIds(season_ids):
    matchIds = []

    for seasId in season_ids:
        response = requests.get(URL + '/league-matches', params={'key': 'test85g57', 'season_id': seasId, 'max_per_page': 1000})

        seasonMatches = response.json()['data']

        for match in seasonMatches:
            matchIds.append(match['id'])
    
    return matchIds

def getMatchDetails(matchIds):
    matchDetails = []
    count = 0
    for match_id in matchIds:
        time.sleep(2)   #sleep for two seconds because of 30-60 api calls/minute limit
        response = requests.get(URL + '/match', params={'key': 'test85g57', 'match_id': match_id})

        matchDetails.append(response.json()['data'])
        if count > 10:
            break
        else:
            count = count + 1

    return matchDetails
      



premierIds = getLeagueIds("England Premier League")
print(premierIds)
matchIds = getMatchIds(premierIds)
print(matchIds)
matchDetails = getMatchDetails(matchIds)
df = pd.DataFrame(matchDetails)
df.to_csv('match_details.csv')

print("hi")    

