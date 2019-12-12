#!/usr/bin/env python
# coding: utf-8

# In[76]:


import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
games = pd.read_csv('steam.csv')
people = pd.read_csv('steam-200k.csv')
people.columns = ['User ID', "name", "purchase/play", "Hours", "0"]


# In[26]:


master_set = people.join(games.set_index('name'), on = "name").drop(columns = ['0', "platforms", "steamspy_tags"])


# In[106]:


master_set
games[['price']].apply(pd.to_numeric)
games = games.drop(games[games.price == 0.00].index)
games


# In[107]:


games['genres'] = games['genres'].str.split(';').str[0]
Y = games[['price']]
X = pd.get_dummies(games[['genres']]).apply(pd.to_numeric)
X = X.join(games[['average_playtime']], how = "outer")


# In[108]:


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = .20, random_state = 40)
regr = linear_model.SGDRegressor(max_iter=1000, tol = None)
regr.fit(X_train, Y_train)
predicted = regr.predict(X_test)
#for val in X['genres']:
#    if val.dtype==object:


# In[109]:


predicted
mse = mean_squared_error(predicted, Y_test)/len(predicted)
mse

