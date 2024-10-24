import pandas as pd
import numpy as np

# df = pd.read_csv("results.csv")
df1 = pd.read_csv("spotify_songs.csv")
# df2 = pd.read_csv("goalscorers.csv")
# df3 = pd.read_csv("shootouts.csv")

# print(df)
# print(df1)
# print(df2)
# print(df3)

# df.info()
# df1.info()
# df2.info()
# df3.info()

# print(df.describe())
# print(df1.describe())
# print(df2.describe())
# print(df3.describe())

# print(df["away_score"].value_counts())
# print(df1["tempo"].value_counts())
# print(df2["minute"].value_counts())
# print(df3["first_shooter"].value_counts())


# print(df["home_score"].value_counts(normalize=True) * 100)
# print(df1["tempo"].value_counts(normalize=True) * 100)
# print(df2["minute"].value_counts(normalize=True) * 100)
# print(df3["first_shooter"].value_counts(normalize=True) * 100)

# mask = df["home_score"] < 5

# masked_df = df[mask]

# print(masked_df["home_score" ].mean( ))

# print(df1.shape)
# print(df1.columns)
# print(df1.head())
# print(df1["playlist_genre"].value_counts())
# print(df1["playlist_genre"].mode()[0])
# returns always in a series ( no specify mode returns whole data or multiple )
# print(df1["duration_ms"].median())
# print(df1["duration_ms"].mean())

# max_ms = df1 ["duration_ms" ] . max( )
# min_ms = df1 ["duration_ms" ].min( )
# print(max_ms-min_ms)

# print(df1["duration_ms"].sum())

# print(df1.sort_values(by=["duration_ms"]))
# print(df1.sort_values(by=["duration_ms"], ascending=False))

# print(df1.groupby('playlist_genre' ) ['duration_ms'].min())

# print(df1.query("track_artist == 'Ricky Martin'"))

mean_val = df1["duration_ms"].mean()

print(df1.query("duration_ms > @mean_val"))

