from sklearn import datasets
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, MultinomialNB

df = pd.read_csv("titanic.csv")

df.drop(['PassengerId','Name','SibSp','Parch','Ticket','Cabin','Embarked'], axis='columns', inplace=True)

inputs = df.drop('Survived', axis='columns')
dependiente = df.Survived

dummies = pd.get_dummies(inputs.Sex)

print (dummies)

inputs = pd.concat([inputs,dummies], axis='columns')

print(inputs)

inputs.drop(['Sex','male'], axis='columns', inplace=True)

print(inputs)

inputs.columns[inputs.isna().any()]

inputs.Age = inputs.Age.fillna(inputs.Age.mean())

print(inputs)

X_train, X_test, y_train, y_test = train_test_split(inputs, dependiente, test_size=0.3, random_state=758648)

model = GaussianNB()
model.fit(X_train,y_train)

print(model.score(X_test,y_test))
