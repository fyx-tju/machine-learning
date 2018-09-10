import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor

train_file_path = "../data/titanic/train.csv"
test_file_path = "../data/titanic/test.csv"
train_data = pd.read_csv(train_file_path)

test_data = pd.read_csv(test_file_path)
#select one colume and show the head
names = train_data.Name

#select multi columes
columes = ["Name","Age"]
X = train_data[columes]
y = train_data.Embarked

test_X = test_data[columes]
test_y = test_data.Embarked

model = DecisionTreeRegressor()
model.fit(X,y)

model.predict(test_X)

