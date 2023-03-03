import pandas as pd
openFile = pd.read_csv("athlete_events.csv")
openFile.info() # prints the information and specifics of the dataset

print(openFile['Name'])
print(openFile.Name)
#openFile.Name.hist()
print("Minimum Age is : {}".format(openFile.Age.min()))
openFile.info() # prints the information and specifics of the dataset
openFile.Name.hist()
openFile.head(28)