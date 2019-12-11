import pandas as pd
import numpy as np
import matplotlib as plt

# Makes the output display better for PyCharm. You can ignore elsewhere
desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',20)

# Change the filepaths to wherever you have them located
data1 = pd.read_csv(filepath_or_buffer='~/Library/Preferences/PyCharmCE2018.3/scratches/steam-store-games/steam.csv')
data2 = pd.read_csv(filepath_or_buffer='~/Library/Preferences/PyCharmCE2018.3/scratches/steam-200k.csv')
# Column names were missing
data2.columns = ['userid', 'name', 'behavior', 'hours', 'trashcol']

# print(data1.head())
# print(data2.head())

# Not sure if this is exactly what we want
data = pd.merge(data1, data2, on='name')

# Removing some of the columns that I don't think we need
data = data.drop(columns=['english', 'required_age', 'trashcol', 'achievements'])
# print(all_data.head())

# Start of analysis/visualization work
# print(all_data.loc[all_data['behavior'] == 'play'].describe())
print(data.loc[(data['developer'] == 'Valve')].describe())
print(data.loc[(data['developer'] == 'PopTop')].describe(), '\n')

print('Number of games : {0}'.format(len(data.name.unique())))
print('Number of users : {0}'.format(len(data.userid.unique())))
print('Number of total purchases : {0}'.format(len(data.loc[data['behavior'] == 'purchase'])))
print('Number of total plays infos : {0}'.format(len(data.loc[data['behavior'] == 'play'])))
