from pandasql  import  sqldf as sqldf
import pandas as pd
openFile = pd.read_csv("athlete_events.csv")
pysqldf = lambda q : sqldf(q, globals())

try:
    pysqldf = ("SELECT * FROM openFile;").head(5)
except:
    pysqldf = ("SELECT * FROM openFile;")