#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Librarirs

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Load EPL data into a DataFrame

epl_df = pd.read_csv('C:\\Users\\ayans\\Downloads\\EPL_20_21\\EPL_20_21.csv')
epl_df.head()


# In[3]:


# Print a summary of the DataFrame

epl_df.info()


# In[4]:


# Print summary statistics of the DataFrame

epl_df.describe()


# In[5]:


# Count the number of missing values (NaN) in each column of epl_df

epl_df.isna().sum()


# In[6]:


# Create 2 new columns

epl_df['MinsPerMatch'] = (epl_df['Mins'] / epl_df['Matches']).astype(int)
epl_df['GoalsPerMatch'] = (epl_df['Goals'] / epl_df['Matches']).astype(float)
epl_df.head()


# In[7]:


# Total Goals

Total_Goals = epl_df['Goals'].sum()
print(Total_Goals)


# In[8]:


# Penalty Goals

Total_PenaltyGoals = epl_df['Penalty_Goals'].sum()
print(Total_PenaltyGoals)


# In[10]:


# Penalty Attempts

Total_PenaltyAttempts = epl_df['Penalty_Attempted'].sum()
print(Total_PenaltyAttempts)


# In[11]:


# Pie chart for penalties missed vs scored

plt.figure(figsize = (13, 6))
pl_not_scored = epl_df['Penalty_Attempted'].sum() - Total_PenaltyGoals
data = [pl_not_scored, Total_PenaltyGoals]
labels = ['Penalties Missed', 'Penalty Scored']
color_palette = sns.color_palette("Paired")
plt.pie(data, labels = labels, colors = color_palette, autopct = '%.0f%%')
plt.show()


# In[12]:


# Unique positions

epl_df['Position'].unique()


# In[13]:


# Total FW Players

epl_df[epl_df['Position'] == 'FW']


# In[14]:


# Players from different nations

np.size((epl_df['Nationality'].unique()))


# In[15]:


# Most players from which countries

nationality = epl_df.groupby('Nationality').size().sort_values(ascending = False)
nationality.head(10).plot(kind = 'bar', figsize = (12, 6), color = sns.color_palette('magma'))


# In[16]:


# Clubs with maximum players in their squad

epl_df['Club'].value_counts().nlargest(5).plot(kind = 'bar', color = sns.color_palette("viridis"))


# In[17]:


# Clubs with latest players in their squad

epl_df['Club'].value_counts().nsmallest(5).plot(kind = 'bar', color = sns.color_palette("viridis"))


# In[18]:


# Players based on age group

Under20 = epl_df[epl_df['Age'] <= 20]
age20_25 = epl_df[(epl_df['Age'] > 20) & (epl_df['Age'] <= 25)]
age25_30 = epl_df[(epl_df['Age'] > 25) & (epl_df['Age'] <= 30)]
Above30 = epl_df[epl_df['Age'] > 30]


# In[21]:


# Assuming the following DataFrame exist: Under20, age20_25, age25_30 and Above30

x = np.array([Under20['Name'].count(),age20_25['Name'].count(),age25_30['Name'].count(),Above30['Name'].count()])
mylabels = ["<=20", ">20 & <=25", ">25 & <=30", ">30"]
plt.title('Total Players with Age Groups', fontsize=20)
plt.pie(x, labels=mylabels, autopct = "%.1f%%")
plt.show()


# In[22]:


# Total under 20 players in each club

players_under_20 = epl_df[epl_df['Age'] < 20]
players_under_20['Club'].value_counts().plot(kind = 'bar', color = sns.color_palette("cubehelix"))


# In[23]:


# Under 20 players in Manu

players_under_20[players_under_20["Club"] == 'Manchester United']


# In[24]:


# Under 20 players in Chelsea

players_under_20[players_under_20["Club"] == 'Chelsea']


# In[25]:


# Average age of players in each club

plt.figure(figsize = (12, 6))
sns.boxplot(x = 'Club', y = 'Age', data = epl_df)
plt.xticks(rotation = 90)


# In[27]:


# Group the English Premier League DataFrame (epl_df) by club and count the number of players in each club

num_player = epl_df.groupby('Club').size()
data = (epl_df.groupby('Club')['Age'].sum()) / num_player
data.sort_values(ascending = False)


# In[34]:


# Total assists from each club

Assits_by_club = pd.DataFrame(epl_df.groupby('Club', as_index = False)['Assists'].sum())
sns.set_theme(style = "whitegrid", color_codes = True)
ax = sns.barplot(x = 'Club', y = 'Assists', data = Assits_by_club.sort_values(by = 'Assists'), palette = 'tab20')
ax.set_xlabel("Club", fontsize = 30)
ax.set_ylabel("Assists", fontsize = 20)
plt.xticks(rotation = 75)
plt.rcParams["figure.figsize"] = (20, 8)
plt.title('Plot of Club vs Total Assists', fontsize = 20)


# In[35]:


# Top 10 Assists

top_10_assists = epl_df[['Name', 'Club', 'Assists', 'Matches']].nlargest(n = 10, columns = 'Assists')
top_10_assists


# In[42]:


# Creating a DataFrame to group the total goals scored by each club

Goals_by_clubs = pd.DataFrame(epl_df.groupby('Club', as_index = False)['Goals'].sum())
sns.set_theme(style ="whitegrid", color_codes = True)
ax = sns.barplot(x = 'Club', y = 'Goals', data = Goals_by_clubs.sort_values(by ="Goals"), palette = 'rocket')
ax.set_xlabel("Club", fontsize = 30)
ax.set_ylabel("Goals", fontsize = 20)
plt.xticks(rotation =75)
plt.rcParams["figure.figsize"] = (20, 8)
plt.title('Plot of Club vs Total Goals', fontsize = 20)


# In[43]:


# Most goals by players

top_10_goals = epl_df[['Name', 'Club', 'Goals', 'Matches']].nlargest(n = 10, columns = 'Goals')
top_10_goals


# In[45]:


# Goals per match

top_10_goals_per_match = epl_df[['Name', 'GoalsPerMatch', 'Matches', 'Goals']].nlargest(n = 10, columns = 'GoalsPerMatch')
top_10_goals_per_match


# In[49]:


# Pie Chart - Goals with assist and without assist

plt.figure(figsize = (14, 7))
assists = epl_df['Assists'].sum()
data = [Total_Goals - assists, assists]
labels = ['Goals without assists', 'Goals with assists']
color = sns.color_palette('Set2')
plt.pie(data, labels = labels, colors = color, autopct ='%.0f%%')
plt.title('Percentage of Goals with Assists', fontsize = 20)
plt.show()


# In[50]:


# Top 10 players with most yellow cards

epl_yellow = epl_df.sort_values(by = 'Yellow_Cards', ascending = False)[:10]
plt.figure(figsize = (20, 6))
plt.title("Players with the most yellow cards")
c = sns.barplot(x = epl_yellow['Name'], y = epl_yellow['Yellow_Cards'], label = 'Players', color ='yellow')
plt.ylabel('Number of Yellow Cards')
c.set_xticklabels(c.get_xticklabels(), rotation = 45)
plt.show()


# In[ ]:




