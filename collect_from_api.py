### Collect match, team, and player data from https://api.footystats.org ###

import requests
import pandas as pd
import json
import time
import os

## CONSTANTS ##
URL = "https://api.footystats.org"  # non-changing base url
leagueName = "England Premier League"
apiKey = '3c87c3773c4ff88f7cbdc8f44e4ced63130a5756031056c90b9025b5ffe62407'

## FUNCTIONS ##

# Find season id's for specified league(s), league name must be looked up beforehand
def getSeasonIds(leagueName):
    response = requests.get(URL + '/league-list', params={'key': apiKey})

    leagues = response.json()['data']
    seasonIds = []
    for league in leagues:
        if league['name'] == leagueName:
            for season in league['season']:
                seasonIds.append(season['id'])
            
            break  # no need to keep searching league list

    return seasonIds

def getMatchIds(season_id):
    matchIds = []

    response = requests.get(URL + '/league-matches', params={'key': apiKey, 'season_id': season_id, 'max_per_page': 500})

    seasonMatches = response.json()['data']

    for match in seasonMatches:
        matchIds.append(match['id'])
    
    return matchIds

def getMatchDetails(matchIds):
    matchDetails = []
    #count = 0
    for match_id in matchIds:
        time.sleep(2)   #sleep for two seconds because of 30-60 api calls/minute limit
        response = requests.get(URL + '/match', params={'key': apiKey, 'match_id': match_id})

        matchDetails.append(response.json()['data'])
        #if count > 2:
        #    break
        #else:
        #    count = count + 1

    return matchDetails
      

## MAIN CODE ##
seasonIds = [3119, 3121, 3125, 3131, 3137, 4759]
#seasonIds = getSeasonIds(leagueName)    #get season id's for specified league
#print(seasonIds)
allSeasons = pd.DataFrame()     #empty data frame to populate

for season_id in seasonIds:
    matchIds = getMatchIds(season_id)
    #print(matchIds)
    matchDetails = getMatchDetails(matchIds)
    df = pd.json_normalize(matchDetails)
    allSeasons = allSeasons.append(df)    #append to sum dataframe

    #produce path for file
    outname = "{}.csv".format(season_id)
    outdir = "./footy_api_csv_data/{}".format(leagueName)
    if not os.path.exists(outdir):        #check if directory exists and make it if it doesn't
        os.mkdir(outdir)

    fullname = os.path.join(outdir, outname)

    df.to_csv(fullname, index=False)
    print("finished season {}".format(season_id))

allSeasons.to_csv(outdir + '/all_seasons.csv', index=False)
print("Done creating csv's for all {} seasons of the {}".format(len(seasonIds), leagueName))

   

