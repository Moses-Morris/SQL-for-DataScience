import pandas as pd
from csv import reader 

file = open("athlete_events.csv")
data = reader(file)
information = list(data)
print(data)
print(information)