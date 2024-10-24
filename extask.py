import pandas as pd
import numpy as np

df = pd.read_csv("results.csv")

#pd.set_option('display.max_rows', 500)

# Activity 1

# Remember your data from results.csv?

# Find out:
# . How many different kinds of tournaments were played?
#   "tournament"
# . How many matches were played under each tournament?
# . The most reported home team and away team
# . The least reported home team and away team

df.info()
# print(df["tournament"].value_counts())

# # print(df["tournament"].value_counts())

# print (df["home_team"].mode())

# print(df["home_team"].min())

# print(df["away_team"].mode())

# print(df["away_team"].min())

#print(df["home_team"].value_counts())

#print(df.groupby('home_team' ) ['home_team'].max())
#print(df.groupby("home_team") ["home_team"].max())

# Activity 2

# Find out:
# . How many times England played at home in each tournament.
# x = (df.query("home_team == 'England'"))

# print(x["tournament"].sum())
#print(df.groupby('England') ['home_team'].ma())
# . How many times England scored more than the "average" amount of goals at a home match.



# . How many times England scored more than the "average" amount of goals at an away match.


# . What is England's average amount of goals scored at home?
# . What is each team's average home score and away score?

# Important!
# You may need to research some methods to get the results requested 
# - not every Pandas method has been covered in session.

# Important!
# If your results are truncating and you don't want them to, 
# you can change the number of rows shownwith:

# pd.set_option('display.max_rows', 500)

# Stretch
# In a match between Iceland and England*, the final score was 8 - 0.
# Based on your findings, is this an expected result?
# What factors could have caused this result?
# *Iceland (home) vs England (away)