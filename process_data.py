import pandas as pd

data = pd.read_csv("datahub_io_raw_data\seasgit on-1819_csv.csv")

col_names = data.columns

col_to_keep = ['Date', 'HomeTeam', 'AwayTeam', 'FTR', 'Referee',]

##produce team form for every date (results from 5 previous matches)
## format is a 
form = []
for ind in data.index:
    date = data['Date'][ind]
    homeTeam = data['HomeTeam'][ind]
    awayTeam = data['AwayTeam'][ind]
    result = data['FTR'][ind]

    if result == 'H':



table = data
print("hi")

