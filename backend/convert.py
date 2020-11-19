import pandas as pd 

import csv, sqlite3

con = sqlite3.connect("spotify_table.db") # change to 'sqlite:///your_filename.db'
cur = con.cursor()

df = pd.read_csv("SpotifyFeatures.csv")
df.to_sql("spotify_table", con, if_exists='append', index=False)

con.close()