import numpy as np
import pandas as pd
from  ydata_profiling import ProfileReport

# results.csv

df = pd.read_csv("results.csv")

profile = ProfileReport(df, title="Football Report")

profile.to_file('results_report.html')

#spotify_songs.csv

df1 = pd.read_csv("spotify_songs.csv")

profile = ProfileReport(df1, title="spotify Report")

profile.to_file('spotify_report.html')

#goalscorers.csv

df2 = pd.read_csv("goalscorers.csv")

profile = ProfileReport(df2, title="Goal Report")

profile.to_file('goal_report.html')

# #shootouts.csv

df3 = pd.read_csv("shootouts.csv")

profile = ProfileReport(df3, title="Shootout Report")

profile.to_file('Shootout_report.html')