#import pandas as pd
from csv import reader 

file = "athlete_events.csv"
data = reader(file)
information = data.json()
print(data)
print(information)