import pandas as pd
import matplotlib.pyplot as plt
from pandas.api.types import is_numeric_dtype

# Imported CSV becomes a pandas dataframe object
data_20 = pd.read_csv("Prem_data_19-20\england-premier-league-matches-2019-to-2020-stats.csv")
data_19 = pd.read_csv("Prem_data_18-19\england-premier-league-matches-2018-to-2019-stats.csv")
data_18 = pd.read_csv("Prem_data_17-18\england-premier-league-matches-2017-to-2018-stats.csv")
data_17 = pd.read_csv("Prem_data_16-17\england-premier-league-matches-2016-to-2017-stats.csv")
data_16 = pd.read_csv("Prem_data_15-16\england-premier-league-matches-2015-to-2016-stats.csv")
data_15 = pd.read_csv("Prem_data_14-15\england-premier-league-matches-2014-to-2015-stats.csv")
data_14 = pd.read_csv("Prem_data_13-14\england-premier-league-matches-2013-to-2014-stats.csv")
data_13 = pd.read_csv("Prem_data_12-13\england-premier-league-matches-2012-to-2013-stats.csv")


data = [data_20, data_19, data_18, data_17, data_16, data_15, data_14, data_13]
data = pd.concat(data)

data['Winning_Side'] = data.apply(lambda x: 'Home' if x.home_team_goal_count > x.away_team_goal_count else 'Away' if x.home_team_goal_count < x.away_team_goal_count else "Draw", axis=1)
print(data.head())

data.Winning_Side.value_counts().plot(kind='pie', title = "Winning side of every Premier League match from 2012-2020", autopct='%1.1f%%', startangle=270, fontsize = 24)
#plt.show()
plt.savefig('data_figures/result_pie.png')
plt.close()



def make_density_plot(columnName, df):
    df.groupby("Winning_Side")[columnName].plot(kind = "kde", title = "Density graph of {} for each match result".format(columnName), legend=True)
    plt.xlabel(columnName)
    #fig.figure.savefig('data_figures/{}_density.png'.format(columnName))
    #plt.show()
    plt.savefig('data_figures/{}_density.png'.format(columnName))
    plt.close()

def make_histogram_plot(columnName, df):
    df.groupby("Winning_Side")[columnName].plot(kind = "hist", title = "Histogram graph of {} for each match result".format(columnName), legend=True, bins = 20, alpha = 0.3)
    plt.xlabel(columnName)
    #fig.figure.savefig('data_figures/{}_density.png'.format(columnName))
    #plt.show()
    plt.savefig('data_figures/{}_histogram.png'.format(columnName))
    plt.close()

def make_box_plot(columnName, df):
    df.boxplot(by="Winning_Side", column=columnName)
    plt.ylabel(columnName)
    plt.title("Box plot of {} for each match result".format(columnName))
    plt.suptitle('')
    #plt.show()
    plt.savefig('data_figures/{}_boxplot.png'.format(columnName))
    plt.close()

columns = list(data.columns)
columns.remove("Winning_Side")
print(columns)
for column in columns:
    if is_numeric_dtype(data[column]):
        make_density_plot(column, data)
        make_histogram_plot(column, data)
        make_box_plot(column, data)


