import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

file_path = "../data/titanic/train.csv"
train_data = pd.read_csv(file_path,index_col=1)
print(train_data.head(5))
print(train_data.columns)
print(train_data.describe())

#select one colume and show the head
names = train_data.Name
print(names.head(10))
print(train_data["Name"].head())

#select multi columes
columes = ["Name","Age"]
two_columes = train_data[columes]
print(two_columes.describe())

two_columes.to_csv("output.csv")
two_columes.to_excel("output.xlsx",sheet_name="dog")

data = pd.DataFrame({"Apples":[30,11],"Bananas":[21,11],"Dog":[22],"fox":[22],"eye":[66],"Zoo":[33]},index=[0,1])
print(data.loc[:,"Apples":"Zoo"])
print("###################")
print(data[0:1])
print(data.iloc[0])
print(data.iloc[[0],[0]])
print(data.loc[[0],"Bananas"])
print(data.ix[:,'Bananas'])
print(data[data['Bananas']>12])
print(data.loc[data.Bananas==21])
print(data.loc[data.Bananas.isin([21,11])])
print(data.loc[data.Bananas.notnull()])
print(data.loc[(data.Bananas==21) & (data.Dog==22)])
data.Apples.plot.hist()
data['Bananas'] = range(len(data), 0, -1)
func = lambda x : x**2
print(data.apply(func))
print(data.applymap(func))
print(data.set_index("Bananas"))

import sqlite3
#conn = sqlite3.connect("../input/pitchfork-data/database.sqlite")
#fires = pd.read_sql_query("SELECT * FROM artists", conn)
