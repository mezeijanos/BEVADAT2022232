# -*- coding: utf-8 -*-
"""GYAK04.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IXPj5nsBSre7lQd96h2zJGYzwVS_T15I
"""

import pandas as pd
import matplotlib.pyplot as plt

'''
FONTOS: Az első feladatáltal visszaadott DataFrame-et kell használni a további feladatokhoz. 
A függvényeken belül mindig készíts egy másolatot a bemenő df-ről, (new_df = df.copy() és ezzel dolgozz tovább.)
'''

'''
Készíts egy függvényt ami a bemeneti dictionary-ből egy DataFrame-et ad vissza.

Egy példa a bemenetre: test_dict
Egy példa a kimenetre: test_df
return type: pandas.core.frame.DataFrame
függvény neve: dict_to_dataframe
'''

stats = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

from pandas.io.formats.printing import Dict
def dict_to_dataframe(input_dict: Dict) -> pd.core.frame.DataFrame:
  #df = pd.DataFrame.from_dict(input_dict, orient='index')
  #df.index.name = 'index'
  df = pd.DataFrame(input_dict)
  return df

df = dict_to_dataframe(stats)

'''
Készíts egy függvényt ami a bemeneti DataFrame-ből vissza adja csak azt az oszlopot amelynek a neve a bemeneti string-el megegyező.

Egy példa a bemenetre: test_df, 'area'
Egy példa a kimenetre: test_df
return type: pandas.core.series.Series
függvény neve: get_column
'''

def get_column(input_df: pd.core.frame.DataFrame, column_name: str) -> pd.core.series.Series:
  work_df = input_df.copy()
  col = work_df[column_name]
  return col

#brasil = get_column(df, 'area')
#print(brasil)

'''
Készíts egy függvényt ami a bemeneti DataFrame-ből vissza adja a két legnagyobb területű országhoz tartozó sorokat.

Egy példa a bemenetre: test_df
Egy példa a kimenetre: test_df
return type: pandas.core.frame.DataFrame
függvény neve: get_top_two
'''

def get_top_two(input_df:pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
  work_df = input_df.copy()
  rows = work_df.nlargest(2, 'area')
  return rows

#print(get_top_two(df))

'''
Készíts egy függvényt ami a bemeneti DataFrame-ből kiszámolja az országok népsűrűségét és eltárolja az eredményt egy új oszlopba ('density').
(density = population / area)

Egy példa a bemenetre: test_df
Egy példa a kimenetre: test_df
return type: pandas.core.frame.DataFrame
függvény neve: population_density
'''

def population_density(input_df:pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
  work_df = input_df.copy()
  density = work_df['population'] / work_df['area']
  work_df['density'] = density
  return work_df

#print(population_density(df))

'''
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan oszlopdiagramot (bar plot),
ami vizualizálja az országok népességét.

Az oszlopdiagram címe legyen: 'Population of Countries'
Az x tengely címe legyen: 'Country'
Az y tengely címe legyen: 'Population (millions)'

Egy példa a bemenetre: test_df
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: plot_population
'''

def plot_population(input_df:pd.core.frame.DataFrame): 
  work_df = input_df.copy()

  #create a figure and axis object
  fig, ax = plt.subplots()

  #plot the data to the axis
  ax.bar(work_df['country'], work_df['population'])   #optional parameter: color='green'

  #title
  #plt.suptitle('Population of Countries')
  ax.set_title('Population of Countries')
  ax.set_xlabel('Country')
  ax.set_ylabel('Population (millions)')

  #ax.tick_params(axis='x', labelrotation=90)   #feliratok elforgatása 90 fokkal az x tengelyen

  return fig
  

#plot_population(df)

'''
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan kördiagramot,
ami vizualizálja az országok területét. Minden körcikknek legyen egy címe, ami az ország neve.

Az kördiagram címe legyen: 'Area of Countries'

Egy példa a bemenetre: test_df
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: plot_area
'''

def plot_area(input_df:pd.core.frame.DataFrame):
  work_df = input_df.copy()

  #create a figure and axis object
  fig, ax = plt.subplots()

  ax.pie(work_df['area'], labels = work_df['country'])

  ax.set_title('Area of Countries')

  return fig

#plot_area(df)

