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

# print(data1.head(2))
# print()
# print(data2.head(2))

# Not sure if this worked
all_data = pd.merge(data1, data2, on='name')
print(all_data.head(2))


