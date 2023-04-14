# Data Analysis Football Project Using Python

This project serves as a comprehensive guide to performing football analysis using Python. It covers data collection, cleaning, manipulation, and visualization to gain insights into football data.

## Live Project Demo

You can view my live project demo: https://youtu.be/_7Q9iiH2A10

## Requirements

To successfully run this project, you will need the following:
- Python 3.x
- Jupyter Notebook
- Pandas
- Numpy
- Matplotlib
- Seaborn

## Installation

To get started, follow these installation steps:
1. Install Python 3.x from the [official website](https://www.python.org/downloads/).
2. Open the Command Prompt terminal.
3. Type `python --version` to check if Python is already installed and if it is, verify that the version is up-to-date.
4. Verify the preferred installer program, `pip`, by typing `pip --version`.
5. Install Jupyterlab by running `pip install jupyterlab` in the Command Prompt terminal.
6. Install Jupyter Notebook by running `pip install jupyter notebook` in the Command Prompt terminal.
7. Once Jupyter Notebook has finished downloading, you will see the file path location in the terminal. Copy this path file location and paste it on a new line, and then hit enter. In my case, the file path is:<br>
`C:\Users\ayans\AppData\Local\Programs\Python\Python310\python.exe -m pip install --upgrade pip`
8. Install the necessary packages by running `pip install pandas`, `pip install numpy`, `pip install matplotlib`, and `pip install seaborn` in the Command Prompt terminal.
9. Create a folder on your desktop for this project. For example:<br><br> ![Desktop Folder](https://user-images.githubusercontent.com/80643467/230805087-43a0eab9-3563-4e95-a2d2-b49798e6376a.png)<br><br>
10. Once you have created the desktop folder, open the folder and copy the folder path location. In my case, the folder path location is: `C:\Users\ayans\Desktop\Test_Jupyter`
11. Paste the folder path location into the Command Prompt terminal by typing `cd C:\Users\ayans\Desktop\Test_Jupyter`
12. After pasting the folder path location, the path will change to:<br><br> ![JN- STEP 7](https://user-images.githubusercontent.com/80643467/230805177-300bda0a-ef73-40cf-a17c-8167e8204684.png)<br><br>
13. Type `jupyter notebook` and hit enter. You will see a new tab open in your browser displaying the Jupyter Notebook dashboard.
14. Click on the following options to get started, as shown in the image below:<br><br> ![JN- STEP 10](https://user-images.githubusercontent.com/80643467/230805220-9d2bea58-36c6-45b7-986f-447243425ab1.png)<br><br>

## Jupyter Notebook - Python Programming

To begin football data analysis with Python, follow these steps:

Step 1:
```python
# Import Librarirs

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
```

Step 2:
```python
# Load EPL data into a DataFrame

epl_df = pd.read_csv('C:\\Users\\ayans\\Downloads\\EPL_20_21\\EPL_20_21.csv')
epl_df.head()
```

Step 3:
```python
# Print a summary of the DataFrame

epl_df.info()
```

Step 4:
```python
# Print summary statistics of the DataFrame

epl_df.describe()
```

Step 5:
```python
# Count the number of missing values (NaN) in each column of epl_df

epl_df.isna().sum()
```

Step 6:
```python
# Create 2 new columns

epl_df['MinsPerMatch'] = (epl_df['Mins'] / epl_df['Matches']).astype(int)
epl_df['GoalsPerMatch'] = (epl_df['Goals'] / epl_df['Matches']).astype(float)
epl_df.head()
```

Step 7:
```python
# Total Goals

Total_Goals = epl_df['Goals'].sum()
print(Total_Goals)
```

Step 8:
```python
# Penalty Goals

Total_PenaltyGoals = epl_df['Penalty_Goals'].sum()
print(Total_PenaltyGoals)
```

Step 9:
```python
# Penalty Attempts

Total_PenaltyAttempts = epl_df['Penalty_Attempted'].sum()
print(Total_PenaltyAttempts)
```

Step 10:
```python
# Pie chart for penalties missed vs scored

plt.figure(figsize = (13, 6))
pl_not_scored = epl_df['Penalty_Attempted'].sum() - Total_PenaltyGoals
data = [pl_not_scored, Total_PenaltyGoals]
labels = ['Penalties Missed', 'Penalty Scored']
color_palette = sns.color_palette("Paired")
plt.pie(data, labels = labels, colors = color_palette, autopct = '%.0f%%')
plt.show()
```

Step 11:
```python
# Unique positions

epl_df['Position'].unique()
```

Step 12:
```python
# Total FW Players

epl_df[epl_df['Position'] == 'FW']
```

Step 13:
```python
# Players from different nations

np.size((epl_df['Nationality'].unique()))
```

Step 14:
```python
# Most players from which countries

nationality = epl_df.groupby('Nationality').size().sort_values(ascending = False)
nationality.head(10).plot(kind = 'bar', figsize = (12, 6), color = sns.color_palette('magma'))
```

Step 15:
```python
# Clubs with maximum players in their squad

epl_df['Club'].value_counts().nlargest(5).plot(kind = 'bar', color = sns.color_palette("viridis"))
```

Step 16:
```python
# Clubs with latest players in their squad

epl_df['Club'].value_counts().nsmallest(5).plot(kind = 'bar', color = sns.color_palette("viridis"))
```

Step 17:
```python
# Players based on age group

Under20 = epl_df[epl_df['Age'] <= 20]
age20_25 = epl_df[(epl_df['Age'] > 20) & (epl_df['Age'] <= 25)]
age25_30 = epl_df[(epl_df['Age'] > 25) & (epl_df['Age'] <= 30)]
Above30 = epl_df[epl_df['Age'] > 30]
```

Step 18:
```python
# Assuming the following DataFrame exist: Under20, age20_25, age25_30 and Above30

x = np.array([Under20['Name'].count(),age20_25['Name'].count(),age25_30['Name'].count(),Above30['Name'].count()])
mylabels = ["<=20", ">20 & <=25", ">25 & <=30", ">30"]
plt.title('Total Players with Age Groups', fontsize=20)
plt.pie(x, labels=mylabels, autopct = "%.1f%%")
plt.show()
```

Step 19:
```python
# Total under 20 players in each club

players_under_20 = epl_df[epl_df['Age'] < 20]
players_under_20['Club'].value_counts().plot(kind = 'bar', color = sns.color_palette("cubehelix"))
```

Step 20:
```python
# Under 20 players in Manu

players_under_20[players_under_20["Club"] == 'Manchester United']
```

Step 21:
```python
# Under 20 players in Chelsea

players_under_20[players_under_20["Club"] == 'Chelsea']
```

Step 22:
```python
# Average age of players in each club

plt.figure(figsize = (12, 6))
sns.boxplot(x = 'Club', y = 'Age', data = epl_df)
plt.xticks(rotation = 90)
```

Step 23:
```python
# Group the English Premier League DataFrame (epl_df) by club and count the number of players in each club

num_player = epl_df.groupby('Club').size()
data = (epl_df.groupby('Club')['Age'].sum()) / num_player
data.sort_values(ascending = False)
```

Step 24:
```python
# Total assists from each club

Assits_by_club = pd.DataFrame(epl_df.groupby('Club', as_index = False)['Assists'].sum())
sns.set_theme(style = "whitegrid", color_codes = True)
ax = sns.barplot(x = 'Club', y = 'Assists', data = Assits_by_club.sort_values(by = 'Assists'), palette = 'tab20')
ax.set_xlabel("Club", fontsize = 30)
ax.set_ylabel("Assists", fontsize = 20)
plt.xticks(rotation = 75)
plt.rcParams["figure.figsize"] = (20, 8)
plt.title('Plot of Club vs Total Assists', fontsize = 20)
```

Step 25:
```python
# Top 10 Assists

top_10_assists = epl_df[['Name', 'Club', 'Assists', 'Matches']].nlargest(n = 10, columns = 'Assists')
top_10_assists
```

Step 26:
```python
# Creating a DataFrame to group the total goals scored by each club

Goals_by_clubs = pd.DataFrame(epl_df.groupby('Club', as_index = False)['Goals'].sum())
sns.set_theme(style ="whitegrid", color_codes = True)
ax = sns.barplot(x = 'Club', y = 'Goals', data = Goals_by_clubs.sort_values(by ="Goals"), palette = 'rocket')
ax.set_xlabel("Club", fontsize = 30)
ax.set_ylabel("Goals", fontsize = 20)
plt.xticks(rotation =75)
plt.rcParams["figure.figsize"] = (20, 8)
plt.title('Plot of Club vs Total Goals', fontsize = 20)
```

Step 27:
```python
# Most goals by players

top_10_goals = epl_df[['Name', 'Club', 'Goals', 'Matches']].nlargest(n = 10, columns = 'Goals')
top_10_goals
```

Step 28:
```python
# Goals per match

top_10_goals_per_match = epl_df[['Name', 'GoalsPerMatch', 'Matches', 'Goals']].nlargest(n = 10, columns = 'GoalsPerMatch')
top_10_goals_per_match
```

Step 29:
```python
# Pie Chart - Goals with assist and without assist

plt.figure(figsize = (14, 7))
assists = epl_df['Assists'].sum()
data = [Total_Goals - assists, assists]
labels = ['Goals without assists', 'Goals with assists']
color = sns.color_palette('Set2')
plt.pie(data, labels = labels, colors = color, autopct ='%.0f%%')
plt.title('Percentage of Goals with Assists', fontsize = 20)
plt.show()
```

Step 30:
```python
# Top 10 players with most yellow cards

epl_yellow = epl_df.sort_values(by = 'Yellow_Cards', ascending = False)[:10]
plt.figure(figsize = (20, 6))
plt.title("Players with the most yellow cards")
c = sns.barplot(x = epl_yellow['Name'], y = epl_yellow['Yellow_Cards'], label = 'Players', color ='yellow')
plt.ylabel('Number of Yellow Cards')
c.set_xticklabels(c.get_xticklabels(), rotation = 45)
plt.show()
```

## Data Visualization

Finally, we will visualize the data to make it more accessible and understandable. This includes creating plots, charts, and graphs.


## Conclusion

This project provides a comprehensive guide to performing data analysis football using Python. By following these steps, you will be able to collect, clean, manipulate, and visualize football data. Enjoy exploring the world of football data analytics!

## Thank you for watching this project.



