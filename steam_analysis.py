import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
# print(data1.head())

# Start of analysis/visualization work
# print(all_data.loc[all_data['behavior'] == 'play'].describe())
# print(data.loc[(data['developer'] == 'Valve')].describe())
# print(data.loc[(data['developer'] == 'PopTop')].describe(), '\n')

print('Number of games : {0}'.format(len(data.name.unique())))
print('Number of users : {0}'.format(len(data.userid.unique())))
print('Number of total purchases : {0}'.format(len(data.loc[data['behavior'] == 'purchase'])))
print('Number of total plays infos : {0}'.format(len(data.loc[data['behavior'] == 'play'])))

# plt.hist(data1., bins=100)
# price_data = data1.price[data1.price!=0]
# plt.hist(price_data, bins=100)
# plt.show()

# print(len(data1.genres.unique()))

action = len(data1.genres[data1.genres=='Action'])
indie = len(data1.genres[data1.genres=='Indie'])
strategy = len(data1.genres[data1.genres=='Strategy'])
rpg = len(data1.genres[data1.genres=='RPG'])
sports = len(data1.genres[data1.genres=='Sports'])
racing = len(data1.genres[data1.genres=='Racing'])
adventure = len(data1.genres[data1.genres=='Adventure'])
simulation = len(data1.genres[data1.genres=='Simulation'])

genre_data = pd.DataFrame({
    'Action': [action],
    'Indie': [indie],
    'Adventure': [adventure],
    'Strategy': [strategy],
    'Simulation': [simulation],
    'RPG': [rpg],
    'Racing': [racing],
    'Sports': [sports],
})

print(len(data1.price[data1.price!=0]))

genres = ['Indie','Action','Adventure','Strategy','Simulation','RPG','Sports','Racing']
genres_counters = [0,0,0,0,0,0,0,0]
for row, column in data1.iterrows():
    for ind in range(len(genres)):
        if genres[ind] in column['genres'] and (column['price'] != 0):
            genres_counters[ind]+=1

genres_rating_counters = [0,0,0,0,0,0,0,0]
for row, column in data1.iterrows():
    for ind in range(len(genres)):
        if (genres[ind] in column['genres']) and (column['price'] != 0):
            genres_rating_counters[ind]+=column['price']
for ind in range(len(genres_rating_counters)):
    genres_rating_counters[ind] = genres_rating_counters[ind] / genres_counters[ind]

# genres_playtime_counters = [0,0,0,0,0,0,0,0]
# for row, column in data1.iterrows():
#     for ind in range(len(genres)):
#         if genres[ind] in column['genres']:
#             genres_playtime_counters[ind]+=column['average_playtime']
# for ind in range(len(genres_playtime_counters)):
    # genres_playtime_counters[ind] = genres_playtime_counters[ind] / genres_counters[ind]

flatui = ['#b00404','#3e1087', '#76c941', '#0d3b89', '#565c67', '#ee3405', '#d9ee31', '#106008']
sns.set(style='whitegrid')

ax = sns.barplot(x=genre_data.columns, y=genres_rating_counters,
            palette=flatui)
ax.set(xlabel='Game Genre', ylabel='Mean Price - British Pounds')
plt.show()

print(data1.head())



