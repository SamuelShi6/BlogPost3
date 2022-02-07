We first import the pandas package:


```python
import pandas as pd
```

Then we read the file `movies.csv` and save it as a dataframe:


```python
df = pd.read_csv("movies.csv")
df
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
      <th>actor</th>
      <th>movie_or_TV_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Devon Murray</td>
      <td>Damo &amp; Ivor The Movie</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Devon Murray</td>
      <td>Harry Potter and the Deathly Hallows: Part II</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Devon Murray</td>
      <td>Harry Potter and the Deathly Hallows: Part 2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Devon Murray</td>
      <td>Harry Potter and the Deathly Hallows: Part 1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Devon Murray</td>
      <td>Harry Potter and the Half-Blood Prince</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>10112</th>
      <td>David Tennant</td>
      <td>Heroes Unmasked</td>
    </tr>
    <tr>
      <th>10113</th>
      <td>David Tennant</td>
      <td>The Big Fat Quiz of the Year</td>
    </tr>
    <tr>
      <th>10114</th>
      <td>David Tennant</td>
      <td>Timeshift</td>
    </tr>
    <tr>
      <th>10115</th>
      <td>David Tennant</td>
      <td>A Taste of My Life</td>
    </tr>
    <tr>
      <th>10116</th>
      <td>David Tennant</td>
      <td>Greatest Before They Were Stars TV Moments</td>
    </tr>
  </tbody>
</table>
<p>10117 rows × 2 columns</p>
</div>



We have to first remove duplicated rows because certain actors have played different roles for a movie, resulting in double counting:


```python
df = df.drop_duplicates()
df
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
      <th>actor</th>
      <th>movie_or_TV_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Devon Murray</td>
      <td>Damo &amp; Ivor The Movie</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Devon Murray</td>
      <td>Harry Potter and the Deathly Hallows: Part II</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Devon Murray</td>
      <td>Harry Potter and the Deathly Hallows: Part 2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Devon Murray</td>
      <td>Harry Potter and the Deathly Hallows: Part 1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Devon Murray</td>
      <td>Harry Potter and the Half-Blood Prince</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>10110</th>
      <td>David Tennant</td>
      <td>The Big Finish</td>
    </tr>
    <tr>
      <th>10112</th>
      <td>David Tennant</td>
      <td>Heroes Unmasked</td>
    </tr>
    <tr>
      <th>10114</th>
      <td>David Tennant</td>
      <td>Timeshift</td>
    </tr>
    <tr>
      <th>10115</th>
      <td>David Tennant</td>
      <td>A Taste of My Life</td>
    </tr>
    <tr>
      <th>10116</th>
      <td>David Tennant</td>
      <td>Greatest Before They Were Stars TV Moments</td>
    </tr>
  </tbody>
</table>
<p>9275 rows × 2 columns</p>
</div>



Count the number of actors that a particular movie shares:


```python
df = df.groupby(['movie_or_TV_name']).size()
```

Rename the columns and sort the values:


```python
df = df.reset_index()
df = df.rename(columns = {0: "Number of Shared Actors", "movie_or_TV_name": "Movie or TV Name"})
df = df.sort_values(["Number of Shared Actors", "Movie or TV Name"], ascending=False)
```

Make the table more presentatble:


```python
df = df.reset_index()
df = df.drop(['index'], axis = 1)
```

Present the final result as follows:


```python
df[0:20]
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
      <th>Movie or TV Name</th>
      <th>Number of Shared Actors</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Harry Potter and the Goblet of Fire</td>
      <td>176</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Harry Potter and the Order of the Phoenix</td>
      <td>60</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Harry Potter and the Deathly Hallows: Part 1</td>
      <td>42</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Harry Potter and the Deathly Hallows: Part 2</td>
      <td>38</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Harry Potter and the Chamber of Secrets</td>
      <td>38</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Harry Potter and the Sorcerer's Stone</td>
      <td>33</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Harry Potter and the Half-Blood Prince</td>
      <td>28</td>
    </tr>
    <tr>
      <th>7</th>
      <td>The Bill</td>
      <td>26</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Harry Potter and the Prisoner of Azkaban</td>
      <td>26</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Creating the World of Harry Potter, Part 2: Ch...</td>
      <td>25</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Harry Potter 20th Anniversary: Return to Hogwarts</td>
      <td>22</td>
    </tr>
    <tr>
      <th>11</th>
      <td>This Morning</td>
      <td>21</td>
    </tr>
    <tr>
      <th>12</th>
      <td>HBO First Look</td>
      <td>20</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Doctor Who</td>
      <td>20</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Today</td>
      <td>18</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Reflections on the Fourth Film</td>
      <td>18</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Casualty</td>
      <td>18</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Preparing for the Yule Ball</td>
      <td>16</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Screen Two</td>
      <td>15</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Creating the World of Harry Potter, Part 8: Gr...</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>



It fits our expectation that the movie itself shares the most no. of actors. At the same time, the *Harry Potter* series have the most no. of the same actors, which is expected since the series used similar casts and crews for each of its movie. However, there are also some interesting results such as *The Bill*, *Doctor Who*, etc. that definitely worth checking if you are also a fan of the *Harry Potter* series. 
