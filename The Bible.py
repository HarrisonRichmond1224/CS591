#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd


games = pd.read_csv('steam.csv')
people = pd.read_csv('steam-200k.csv')


# In[21]:


people.columns = ['User ID', "name", "purchase/play", "Hours", "0"]


# In[24]:


people.join(games.set_index('name'), on = "name").drop(columns = ['0', "platforms"])

