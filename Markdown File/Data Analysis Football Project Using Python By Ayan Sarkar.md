```python
# Import Librarirs

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
```


```python
# Load EPL data into a DataFrame

epl_df = pd.read_csv('C:\\Users\\ayans\\Downloads\\EPL_20_21\\EPL_20_21.csv')
epl_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Club</th>
      <th>Nationality</th>
      <th>Position</th>
      <th>Age</th>
      <th>Matches</th>
      <th>Starts</th>
      <th>Mins</th>
      <th>Goals</th>
      <th>Assists</th>
      <th>Passes_Attempted</th>
      <th>Perc_Passes_Completed</th>
      <th>Penalty_Goals</th>
      <th>Penalty_Attempted</th>
      <th>xG</th>
      <th>xA</th>
      <th>Yellow_Cards</th>
      <th>Red_Cards</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mason Mount</td>
      <td>Chelsea</td>
      <td>ENG</td>
      <td>MF,FW</td>
      <td>21</td>
      <td>36</td>
      <td>32</td>
      <td>2890</td>
      <td>6</td>
      <td>5</td>
      <td>1881</td>
      <td>82.3</td>
      <td>1</td>
      <td>1</td>
      <td>0.21</td>
      <td>0.24</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Edouard Mendy</td>
      <td>Chelsea</td>
      <td>SEN</td>
      <td>GK</td>
      <td>28</td>
      <td>31</td>
      <td>31</td>
      <td>2745</td>
      <td>0</td>
      <td>0</td>
      <td>1007</td>
      <td>84.6</td>
      <td>0</td>
      <td>0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Timo Werner</td>
      <td>Chelsea</td>
      <td>GER</td>
      <td>FW</td>
      <td>24</td>
      <td>35</td>
      <td>29</td>
      <td>2602</td>
      <td>6</td>
      <td>8</td>
      <td>826</td>
      <td>77.2</td>
      <td>0</td>
      <td>0</td>
      <td>0.41</td>
      <td>0.21</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ben Chilwell</td>
      <td>Chelsea</td>
      <td>ENG</td>
      <td>DF</td>
      <td>23</td>
      <td>27</td>
      <td>27</td>
      <td>2286</td>
      <td>3</td>
      <td>5</td>
      <td>1806</td>
      <td>78.6</td>
      <td>0</td>
      <td>0</td>
      <td>0.10</td>
      <td>0.11</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Reece James</td>
      <td>Chelsea</td>
      <td>ENG</td>
      <td>DF</td>
      <td>20</td>
      <td>32</td>
      <td>25</td>
      <td>2373</td>
      <td>1</td>
      <td>2</td>
      <td>1987</td>
      <td>85.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.06</td>
      <td>0.12</td>
      <td>3</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Print a summary of the DataFrame

epl_df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 532 entries, 0 to 531
    Data columns (total 18 columns):
     #   Column                 Non-Null Count  Dtype  
    ---  ------                 --------------  -----  
     0   Name                   532 non-null    object 
     1   Club                   532 non-null    object 
     2   Nationality            532 non-null    object 
     3   Position               532 non-null    object 
     4   Age                    532 non-null    int64  
     5   Matches                532 non-null    int64  
     6   Starts                 532 non-null    int64  
     7   Mins                   532 non-null    int64  
     8   Goals                  532 non-null    int64  
     9   Assists                532 non-null    int64  
     10  Passes_Attempted       532 non-null    int64  
     11  Perc_Passes_Completed  532 non-null    float64
     12  Penalty_Goals          532 non-null    int64  
     13  Penalty_Attempted      532 non-null    int64  
     14  xG                     532 non-null    float64
     15  xA                     532 non-null    float64
     16  Yellow_Cards           532 non-null    int64  
     17  Red_Cards              532 non-null    int64  
    dtypes: float64(3), int64(11), object(4)
    memory usage: 74.9+ KB
    


```python
# Print summary statistics of the DataFrame

epl_df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Matches</th>
      <th>Starts</th>
      <th>Mins</th>
      <th>Goals</th>
      <th>Assists</th>
      <th>Passes_Attempted</th>
      <th>Perc_Passes_Completed</th>
      <th>Penalty_Goals</th>
      <th>Penalty_Attempted</th>
      <th>xG</th>
      <th>xA</th>
      <th>Yellow_Cards</th>
      <th>Red_Cards</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>532.000000</td>
      <td>532.000000</td>
      <td>532.000000</td>
      <td>532.000000</td>
      <td>532.000000</td>
      <td>532.000000</td>
      <td>532.000000</td>
      <td>532.000000</td>
      <td>532.000000</td>
      <td>532.000000</td>
      <td>532.000000</td>
      <td>532.000000</td>
      <td>532.000000</td>
      <td>532.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>25.500000</td>
      <td>19.535714</td>
      <td>15.714286</td>
      <td>1411.443609</td>
      <td>1.853383</td>
      <td>1.287594</td>
      <td>717.750000</td>
      <td>77.823872</td>
      <td>0.191729</td>
      <td>0.234962</td>
      <td>0.113289</td>
      <td>0.072650</td>
      <td>2.114662</td>
      <td>0.090226</td>
    </tr>
    <tr>
      <th>std</th>
      <td>4.319404</td>
      <td>11.840459</td>
      <td>11.921161</td>
      <td>1043.171856</td>
      <td>3.338009</td>
      <td>2.095191</td>
      <td>631.372522</td>
      <td>13.011631</td>
      <td>0.850881</td>
      <td>0.975818</td>
      <td>0.148174</td>
      <td>0.090072</td>
      <td>2.269094</td>
      <td>0.293268</td>
    </tr>
    <tr>
      <th>min</th>
      <td>16.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>-1.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>22.000000</td>
      <td>9.000000</td>
      <td>4.000000</td>
      <td>426.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>171.500000</td>
      <td>73.500000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.010000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>26.000000</td>
      <td>21.000000</td>
      <td>15.000000</td>
      <td>1345.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>573.500000</td>
      <td>79.200000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.060000</td>
      <td>0.050000</td>
      <td>2.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>29.000000</td>
      <td>30.000000</td>
      <td>27.000000</td>
      <td>2303.500000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>1129.500000</td>
      <td>84.625000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.150000</td>
      <td>0.110000</td>
      <td>3.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>38.000000</td>
      <td>38.000000</td>
      <td>38.000000</td>
      <td>3420.000000</td>
      <td>23.000000</td>
      <td>14.000000</td>
      <td>3214.000000</td>
      <td>100.000000</td>
      <td>9.000000</td>
      <td>10.000000</td>
      <td>1.160000</td>
      <td>0.900000</td>
      <td>12.000000</td>
      <td>2.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Count the number of missing values (NaN) in each column of epl_df

epl_df.isna().sum()
```




    Name                     0
    Club                     0
    Nationality              0
    Position                 0
    Age                      0
    Matches                  0
    Starts                   0
    Mins                     0
    Goals                    0
    Assists                  0
    Passes_Attempted         0
    Perc_Passes_Completed    0
    Penalty_Goals            0
    Penalty_Attempted        0
    xG                       0
    xA                       0
    Yellow_Cards             0
    Red_Cards                0
    dtype: int64




```python
# Create 2 new columns

epl_df['MinsPerMatch'] = (epl_df['Mins'] / epl_df['Matches']).astype(int)
epl_df['GoalsPerMatch'] = (epl_df['Goals'] / epl_df['Matches']).astype(float)
epl_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Club</th>
      <th>Nationality</th>
      <th>Position</th>
      <th>Age</th>
      <th>Matches</th>
      <th>Starts</th>
      <th>Mins</th>
      <th>Goals</th>
      <th>Assists</th>
      <th>Passes_Attempted</th>
      <th>Perc_Passes_Completed</th>
      <th>Penalty_Goals</th>
      <th>Penalty_Attempted</th>
      <th>xG</th>
      <th>xA</th>
      <th>Yellow_Cards</th>
      <th>Red_Cards</th>
      <th>MinsPerMatch</th>
      <th>GoalsPerMatch</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mason Mount</td>
      <td>Chelsea</td>
      <td>ENG</td>
      <td>MF,FW</td>
      <td>21</td>
      <td>36</td>
      <td>32</td>
      <td>2890</td>
      <td>6</td>
      <td>5</td>
      <td>1881</td>
      <td>82.3</td>
      <td>1</td>
      <td>1</td>
      <td>0.21</td>
      <td>0.24</td>
      <td>2</td>
      <td>0</td>
      <td>80</td>
      <td>0.166667</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Edouard Mendy</td>
      <td>Chelsea</td>
      <td>SEN</td>
      <td>GK</td>
      <td>28</td>
      <td>31</td>
      <td>31</td>
      <td>2745</td>
      <td>0</td>
      <td>0</td>
      <td>1007</td>
      <td>84.6</td>
      <td>0</td>
      <td>0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>2</td>
      <td>0</td>
      <td>88</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Timo Werner</td>
      <td>Chelsea</td>
      <td>GER</td>
      <td>FW</td>
      <td>24</td>
      <td>35</td>
      <td>29</td>
      <td>2602</td>
      <td>6</td>
      <td>8</td>
      <td>826</td>
      <td>77.2</td>
      <td>0</td>
      <td>0</td>
      <td>0.41</td>
      <td>0.21</td>
      <td>2</td>
      <td>0</td>
      <td>74</td>
      <td>0.171429</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ben Chilwell</td>
      <td>Chelsea</td>
      <td>ENG</td>
      <td>DF</td>
      <td>23</td>
      <td>27</td>
      <td>27</td>
      <td>2286</td>
      <td>3</td>
      <td>5</td>
      <td>1806</td>
      <td>78.6</td>
      <td>0</td>
      <td>0</td>
      <td>0.10</td>
      <td>0.11</td>
      <td>3</td>
      <td>0</td>
      <td>84</td>
      <td>0.111111</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Reece James</td>
      <td>Chelsea</td>
      <td>ENG</td>
      <td>DF</td>
      <td>20</td>
      <td>32</td>
      <td>25</td>
      <td>2373</td>
      <td>1</td>
      <td>2</td>
      <td>1987</td>
      <td>85.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.06</td>
      <td>0.12</td>
      <td>3</td>
      <td>0</td>
      <td>74</td>
      <td>0.031250</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Total Goals

Total_Goals = epl_df['Goals'].sum()
print(Total_Goals)
```

    986
    


```python
# Penalty Goals

Total_PenaltyGoals = epl_df['Penalty_Goals'].sum()
print(Total_PenaltyGoals)
```

    102
    


```python
# Penalty Attempts

Total_PenaltyAttempts = epl_df['Penalty_Attempted'].sum()
print(Total_PenaltyAttempts)
```

    125
    


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


    
![png](output_9_0.png)
    



```python
# Unique positions

epl_df['Position'].unique()
```




    array(['MF,FW', 'GK', 'FW', 'DF', 'MF', 'FW,MF', 'FW,DF', 'DF,MF',
           'MF,DF', 'DF,FW'], dtype=object)




```python
# Total FW Players

epl_df[epl_df['Position'] == 'FW']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Club</th>
      <th>Nationality</th>
      <th>Position</th>
      <th>Age</th>
      <th>Matches</th>
      <th>Starts</th>
      <th>Mins</th>
      <th>Goals</th>
      <th>Assists</th>
      <th>Passes_Attempted</th>
      <th>Perc_Passes_Completed</th>
      <th>Penalty_Goals</th>
      <th>Penalty_Attempted</th>
      <th>xG</th>
      <th>xA</th>
      <th>Yellow_Cards</th>
      <th>Red_Cards</th>
      <th>MinsPerMatch</th>
      <th>GoalsPerMatch</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>Timo Werner</td>
      <td>Chelsea</td>
      <td>GER</td>
      <td>FW</td>
      <td>24</td>
      <td>35</td>
      <td>29</td>
      <td>2602</td>
      <td>6</td>
      <td>8</td>
      <td>826</td>
      <td>77.2</td>
      <td>0</td>
      <td>0</td>
      <td>0.41</td>
      <td>0.21</td>
      <td>2</td>
      <td>0</td>
      <td>74</td>
      <td>0.171429</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Tammy Abraham</td>
      <td>Chelsea</td>
      <td>ENG</td>
      <td>FW</td>
      <td>22</td>
      <td>22</td>
      <td>12</td>
      <td>1040</td>
      <td>6</td>
      <td>1</td>
      <td>218</td>
      <td>68.3</td>
      <td>0</td>
      <td>0</td>
      <td>0.56</td>
      <td>0.07</td>
      <td>0</td>
      <td>0</td>
      <td>47</td>
      <td>0.272727</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Olivier Giroud</td>
      <td>Chelsea</td>
      <td>FRA</td>
      <td>FW</td>
      <td>33</td>
      <td>17</td>
      <td>8</td>
      <td>748</td>
      <td>4</td>
      <td>0</td>
      <td>217</td>
      <td>74.2</td>
      <td>0</td>
      <td>0</td>
      <td>0.58</td>
      <td>0.09</td>
      <td>1</td>
      <td>0</td>
      <td>44</td>
      <td>0.235294</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Ruben Loftus-Cheek</td>
      <td>Chelsea</td>
      <td>ENG</td>
      <td>FW</td>
      <td>24</td>
      <td>1</td>
      <td>1</td>
      <td>60</td>
      <td>0</td>
      <td>0</td>
      <td>16</td>
      <td>68.8</td>
      <td>0</td>
      <td>0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0</td>
      <td>0</td>
      <td>60</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Raheem Sterling</td>
      <td>Manchester City</td>
      <td>ENG</td>
      <td>FW</td>
      <td>25</td>
      <td>31</td>
      <td>28</td>
      <td>2536</td>
      <td>10</td>
      <td>7</td>
      <td>1127</td>
      <td>85.4</td>
      <td>0</td>
      <td>1</td>
      <td>0.43</td>
      <td>0.17</td>
      <td>4</td>
      <td>0</td>
      <td>81</td>
      <td>0.322581</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>516</th>
      <td>Oliver Burke</td>
      <td>Sheffield United</td>
      <td>SCO</td>
      <td>FW</td>
      <td>23</td>
      <td>25</td>
      <td>14</td>
      <td>1269</td>
      <td>1</td>
      <td>1</td>
      <td>262</td>
      <td>70.6</td>
      <td>0</td>
      <td>0</td>
      <td>0.17</td>
      <td>0.13</td>
      <td>2</td>
      <td>0</td>
      <td>50</td>
      <td>0.040000</td>
    </tr>
    <tr>
      <th>518</th>
      <td>Oliver McBurnie</td>
      <td>Sheffield United</td>
      <td>SCO</td>
      <td>FW</td>
      <td>24</td>
      <td>23</td>
      <td>12</td>
      <td>1324</td>
      <td>1</td>
      <td>0</td>
      <td>426</td>
      <td>62.9</td>
      <td>0</td>
      <td>0</td>
      <td>0.21</td>
      <td>0.07</td>
      <td>2</td>
      <td>0</td>
      <td>57</td>
      <td>0.043478</td>
    </tr>
    <tr>
      <th>519</th>
      <td>Rhian Brewster</td>
      <td>Sheffield United</td>
      <td>ENG</td>
      <td>FW</td>
      <td>20</td>
      <td>27</td>
      <td>12</td>
      <td>1128</td>
      <td>0</td>
      <td>0</td>
      <td>225</td>
      <td>69.3</td>
      <td>0</td>
      <td>0</td>
      <td>0.14</td>
      <td>0.13</td>
      <td>1</td>
      <td>0</td>
      <td>41</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>523</th>
      <td>Billy Sharp</td>
      <td>Sheffield United</td>
      <td>ENG</td>
      <td>FW</td>
      <td>34</td>
      <td>16</td>
      <td>7</td>
      <td>735</td>
      <td>3</td>
      <td>0</td>
      <td>123</td>
      <td>69.9</td>
      <td>2</td>
      <td>2</td>
      <td>0.33</td>
      <td>0.07</td>
      <td>1</td>
      <td>0</td>
      <td>45</td>
      <td>0.187500</td>
    </tr>
    <tr>
      <th>526</th>
      <td>Daniel Jebbison</td>
      <td>Sheffield United</td>
      <td>ENG</td>
      <td>FW</td>
      <td>17</td>
      <td>4</td>
      <td>3</td>
      <td>284</td>
      <td>1</td>
      <td>0</td>
      <td>34</td>
      <td>70.6</td>
      <td>0</td>
      <td>0</td>
      <td>0.50</td>
      <td>0.01</td>
      <td>0</td>
      <td>0</td>
      <td>71</td>
      <td>0.250000</td>
    </tr>
  </tbody>
</table>
<p>81 rows × 20 columns</p>
</div>




```python
# Players from different nations

np.size((epl_df['Nationality'].unique()))
```




    59




```python
# Most players from which countries

nationality = epl_df.groupby('Nationality').size().sort_values(ascending = False)
nationality.head(10).plot(kind = 'bar', figsize = (12, 6), color = sns.color_palette('magma'))
```




    <Axes: xlabel='Nationality'>




    
![png](output_13_1.png)
    



```python
# Clubs with maximum players in their squad

epl_df['Club'].value_counts().nlargest(5).plot(kind = 'bar', color = sns.color_palette("viridis"))
```




    <Axes: xlabel='Club'>




    
![png](output_14_1.png)
    



```python
# Clubs with latest players in their squad

epl_df['Club'].value_counts().nsmallest(5).plot(kind = 'bar', color = sns.color_palette("viridis"))
```




    <Axes: xlabel='Club'>




    
![png](output_15_1.png)
    



```python
# Players based on age group

Under20 = epl_df[epl_df['Age'] <= 20]
age20_25 = epl_df[(epl_df['Age'] > 20) & (epl_df['Age'] <= 25)]
age25_30 = epl_df[(epl_df['Age'] > 25) & (epl_df['Age'] <= 30)]
Above30 = epl_df[epl_df['Age'] > 30]
```


```python
# Assuming the following DataFrame exist: Under20, age20_25, age25_30 and Above30

x = np.array([Under20['Name'].count(),age20_25['Name'].count(),age25_30['Name'].count(),Above30['Name'].count()])
mylabels = ["<=20", ">20 & <=25", ">25 & <=30", ">30"]
plt.title('Total Players with Age Groups', fontsize=20)
plt.pie(x, labels=mylabels, autopct = "%.1f%%")
plt.show()
```


    
![png](output_17_0.png)
    



```python
# Total under 20 players in each club

players_under_20 = epl_df[epl_df['Age'] < 20]
players_under_20['Club'].value_counts().plot(kind = 'bar', color = sns.color_palette("cubehelix"))
```




    <Axes: xlabel='Club'>




    
![png](output_18_1.png)
    



```python
# Under 20 players in Manu

players_under_20[players_under_20["Club"] == 'Manchester United']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Club</th>
      <th>Nationality</th>
      <th>Position</th>
      <th>Age</th>
      <th>Matches</th>
      <th>Starts</th>
      <th>Mins</th>
      <th>Goals</th>
      <th>Assists</th>
      <th>Passes_Attempted</th>
      <th>Perc_Passes_Completed</th>
      <th>Penalty_Goals</th>
      <th>Penalty_Attempted</th>
      <th>xG</th>
      <th>xA</th>
      <th>Yellow_Cards</th>
      <th>Red_Cards</th>
      <th>MinsPerMatch</th>
      <th>GoalsPerMatch</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>61</th>
      <td>Mason Greenwood</td>
      <td>Manchester United</td>
      <td>ENG</td>
      <td>FW</td>
      <td>18</td>
      <td>31</td>
      <td>21</td>
      <td>1822</td>
      <td>7</td>
      <td>2</td>
      <td>732</td>
      <td>83.1</td>
      <td>0</td>
      <td>0</td>
      <td>0.37</td>
      <td>0.09</td>
      <td>2</td>
      <td>0</td>
      <td>58</td>
      <td>0.225806</td>
    </tr>
    <tr>
      <th>72</th>
      <td>Brandon Williams</td>
      <td>Manchester United</td>
      <td>ENG</td>
      <td>DF</td>
      <td>19</td>
      <td>4</td>
      <td>2</td>
      <td>188</td>
      <td>0</td>
      <td>0</td>
      <td>140</td>
      <td>85.7</td>
      <td>0</td>
      <td>0</td>
      <td>0.05</td>
      <td>0.01</td>
      <td>0</td>
      <td>0</td>
      <td>47</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>73</th>
      <td>Amad Diallo</td>
      <td>Manchester United</td>
      <td>CIV</td>
      <td>FW</td>
      <td>18</td>
      <td>3</td>
      <td>2</td>
      <td>166</td>
      <td>0</td>
      <td>1</td>
      <td>64</td>
      <td>84.4</td>
      <td>0</td>
      <td>0</td>
      <td>0.02</td>
      <td>0.26</td>
      <td>0</td>
      <td>0</td>
      <td>55</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>74</th>
      <td>Anthony Elanga</td>
      <td>Manchester United</td>
      <td>SWE</td>
      <td>FW</td>
      <td>18</td>
      <td>2</td>
      <td>2</td>
      <td>155</td>
      <td>1</td>
      <td>0</td>
      <td>53</td>
      <td>81.1</td>
      <td>0</td>
      <td>0</td>
      <td>0.16</td>
      <td>0.02</td>
      <td>0</td>
      <td>0</td>
      <td>77</td>
      <td>0.500000</td>
    </tr>
    <tr>
      <th>76</th>
      <td>Shola Shoretire</td>
      <td>Manchester United</td>
      <td>ENG</td>
      <td>FW</td>
      <td>16</td>
      <td>2</td>
      <td>0</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>75.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>78</th>
      <td>Hannibal Mejbri</td>
      <td>Manchester United</td>
      <td>FRA</td>
      <td>MF</td>
      <td>17</td>
      <td>1</td>
      <td>0</td>
      <td>9</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>100.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>79</th>
      <td>William Thomas Fish</td>
      <td>Manchester United</td>
      <td>ENG</td>
      <td>DF</td>
      <td>17</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Under 20 players in Chelsea

players_under_20[players_under_20["Club"] == 'Chelsea']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Club</th>
      <th>Nationality</th>
      <th>Position</th>
      <th>Age</th>
      <th>Matches</th>
      <th>Starts</th>
      <th>Mins</th>
      <th>Goals</th>
      <th>Assists</th>
      <th>Passes_Attempted</th>
      <th>Perc_Passes_Completed</th>
      <th>Penalty_Goals</th>
      <th>Penalty_Attempted</th>
      <th>xG</th>
      <th>xA</th>
      <th>Yellow_Cards</th>
      <th>Red_Cards</th>
      <th>MinsPerMatch</th>
      <th>GoalsPerMatch</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>18</th>
      <td>Callum Hudson-Odoi</td>
      <td>Chelsea</td>
      <td>ENG</td>
      <td>FW,DF</td>
      <td>19</td>
      <td>23</td>
      <td>10</td>
      <td>1059</td>
      <td>2</td>
      <td>3</td>
      <td>659</td>
      <td>82.2</td>
      <td>0</td>
      <td>0</td>
      <td>0.12</td>
      <td>0.26</td>
      <td>0</td>
      <td>0</td>
      <td>46</td>
      <td>0.086957</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Billy Gilmour</td>
      <td>Chelsea</td>
      <td>SCO</td>
      <td>MF</td>
      <td>19</td>
      <td>5</td>
      <td>3</td>
      <td>261</td>
      <td>0</td>
      <td>0</td>
      <td>215</td>
      <td>89.3</td>
      <td>0</td>
      <td>0</td>
      <td>0.01</td>
      <td>0.04</td>
      <td>0</td>
      <td>0</td>
      <td>52</td>
      <td>0.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Average age of players in each club

plt.figure(figsize = (12, 6))
sns.boxplot(x = 'Club', y = 'Age', data = epl_df)
plt.xticks(rotation = 90)
```




    (array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
            17, 18, 19]),
     [Text(0, 0, 'Chelsea'),
      Text(1, 0, 'Manchester City'),
      Text(2, 0, 'Manchester United'),
      Text(3, 0, 'Liverpool FC'),
      Text(4, 0, 'Leicester City'),
      Text(5, 0, 'West Ham United'),
      Text(6, 0, 'Tottenham Hotspur'),
      Text(7, 0, 'Arsenal'),
      Text(8, 0, 'Leeds United'),
      Text(9, 0, 'Everton'),
      Text(10, 0, 'Aston Villa'),
      Text(11, 0, 'Newcastle United'),
      Text(12, 0, 'Wolverhampton Wanderers'),
      Text(13, 0, 'Crystal Palace'),
      Text(14, 0, 'Southampton'),
      Text(15, 0, 'Brighton'),
      Text(16, 0, 'Burnley'),
      Text(17, 0, 'Fulham'),
      Text(18, 0, 'West Bromwich Albion'),
      Text(19, 0, 'Sheffield United')])




    
![png](output_21_1.png)
    



```python
# Group the English Premier League DataFrame (epl_df) by club and count the number of players in each club

num_player = epl_df.groupby('Club').size()
data = (epl_df.groupby('Club')['Age'].sum()) / num_player
data.sort_values(ascending = False)
```




    Club
    Crystal Palace             28.333333
    West Ham United            27.500000
    Burnley                    27.040000
    West Bromwich Albion       26.766667
    Newcastle United           26.074074
    Manchester City            25.708333
    Tottenham Hotspur          25.625000
    Chelsea                    25.592593
    Leicester City             25.592593
    Liverpool FC               25.571429
    Everton                    25.413793
    Leeds United               25.347826
    Fulham                     25.035714
    Arsenal                    24.965517
    Sheffield United           24.814815
    Brighton                   24.555556
    Wolverhampton Wanderers    24.444444
    Aston Villa                24.291667
    Southampton                24.137931
    Manchester United          23.862069
    dtype: float64




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




    Text(0.5, 1.0, 'Plot of Club vs Total Assists')




    
![png](output_23_1.png)
    



```python
# Top 10 Assists

top_10_assists = epl_df[['Name', 'Club', 'Assists', 'Matches']].nlargest(n = 10, columns = 'Assists')
top_10_assists
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Club</th>
      <th>Assists</th>
      <th>Matches</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>162</th>
      <td>Harry Kane</td>
      <td>Tottenham Hotspur</td>
      <td>14</td>
      <td>35</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Kevin De Bruyne</td>
      <td>Manchester City</td>
      <td>12</td>
      <td>25</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Bruno Fernandes</td>
      <td>Manchester United</td>
      <td>12</td>
      <td>37</td>
    </tr>
    <tr>
      <th>161</th>
      <td>Son Heung-min</td>
      <td>Tottenham Hotspur</td>
      <td>10</td>
      <td>37</td>
    </tr>
    <tr>
      <th>273</th>
      <td>Jack Grealish</td>
      <td>Aston Villa</td>
      <td>10</td>
      <td>26</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Marcus Rashford</td>
      <td>Manchester United</td>
      <td>9</td>
      <td>37</td>
    </tr>
    <tr>
      <th>110</th>
      <td>Jamie Vardy</td>
      <td>Leicester City</td>
      <td>9</td>
      <td>34</td>
    </tr>
    <tr>
      <th>220</th>
      <td>Raphael Dias Belloli</td>
      <td>Leeds United</td>
      <td>9</td>
      <td>30</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Timo Werner</td>
      <td>Chelsea</td>
      <td>8</td>
      <td>35</td>
    </tr>
    <tr>
      <th>136</th>
      <td>Aaron Cresswell</td>
      <td>West Ham United</td>
      <td>8</td>
      <td>36</td>
    </tr>
  </tbody>
</table>
</div>




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




    Text(0.5, 1.0, 'Plot of Club vs Total Goals')




    
![png](output_25_1.png)
    



```python
# Most goals by players

top_10_goals = epl_df[['Name', 'Club', 'Goals', 'Matches']].nlargest(n = 10, columns = 'Goals')
top_10_goals
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Club</th>
      <th>Goals</th>
      <th>Matches</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>162</th>
      <td>Harry Kane</td>
      <td>Tottenham Hotspur</td>
      <td>23</td>
      <td>35</td>
    </tr>
    <tr>
      <th>81</th>
      <td>Mohamed Salah</td>
      <td>Liverpool FC</td>
      <td>22</td>
      <td>37</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Bruno Fernandes</td>
      <td>Manchester United</td>
      <td>18</td>
      <td>37</td>
    </tr>
    <tr>
      <th>161</th>
      <td>Son Heung-min</td>
      <td>Tottenham Hotspur</td>
      <td>17</td>
      <td>37</td>
    </tr>
    <tr>
      <th>214</th>
      <td>Patrick Bamford</td>
      <td>Leeds United</td>
      <td>17</td>
      <td>38</td>
    </tr>
    <tr>
      <th>237</th>
      <td>Dominic Calvert-Lewin</td>
      <td>Everton</td>
      <td>16</td>
      <td>33</td>
    </tr>
    <tr>
      <th>110</th>
      <td>Jamie Vardy</td>
      <td>Leicester City</td>
      <td>15</td>
      <td>34</td>
    </tr>
    <tr>
      <th>267</th>
      <td>Ollie Watkins</td>
      <td>Aston Villa</td>
      <td>14</td>
      <td>37</td>
    </tr>
    <tr>
      <th>33</th>
      <td>İlkay Gündoğan</td>
      <td>Manchester City</td>
      <td>13</td>
      <td>28</td>
    </tr>
    <tr>
      <th>191</th>
      <td>Alexandre Lacazette</td>
      <td>Arsenal</td>
      <td>13</td>
      <td>31</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Goals per match

top_10_goals_per_match = epl_df[['Name', 'GoalsPerMatch', 'Matches', 'Goals']].nlargest(n = 10, columns = 'GoalsPerMatch')
top_10_goals_per_match
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>GoalsPerMatch</th>
      <th>Matches</th>
      <th>Goals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>162</th>
      <td>Harry Kane</td>
      <td>0.657143</td>
      <td>35</td>
      <td>23</td>
    </tr>
    <tr>
      <th>81</th>
      <td>Mohamed Salah</td>
      <td>0.594595</td>
      <td>37</td>
      <td>22</td>
    </tr>
    <tr>
      <th>307</th>
      <td>Joe Willock</td>
      <td>0.571429</td>
      <td>14</td>
      <td>8</td>
    </tr>
    <tr>
      <th>145</th>
      <td>Jesse Lingard</td>
      <td>0.562500</td>
      <td>16</td>
      <td>9</td>
    </tr>
    <tr>
      <th>175</th>
      <td>Gareth Bale</td>
      <td>0.550000</td>
      <td>20</td>
      <td>11</td>
    </tr>
    <tr>
      <th>74</th>
      <td>Anthony Elanga</td>
      <td>0.500000</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Bruno Fernandes</td>
      <td>0.486486</td>
      <td>37</td>
      <td>18</td>
    </tr>
    <tr>
      <th>237</th>
      <td>Dominic Calvert-Lewin</td>
      <td>0.484848</td>
      <td>33</td>
      <td>16</td>
    </tr>
    <tr>
      <th>120</th>
      <td>Kelechi Iheanacho</td>
      <td>0.480000</td>
      <td>25</td>
      <td>12</td>
    </tr>
    <tr>
      <th>92</th>
      <td>Diogo Jota</td>
      <td>0.473684</td>
      <td>19</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




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


    
![png](output_28_0.png)
    



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


    
![png](output_29_0.png)
    



```python

```
