import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import numpy as np

df = pandas.read_csv("data.csv")

coche = df['Car'].to_numpy()

arraycoches = np.empty(0, dtype='S')

for i in coche:
    if i not in arraycoches:
        arraycoches = np.append(arraycoches, i)

cont = 0 
d = {}
for i in arraycoches:   
    d[i] = cont
    cont += 1

df['Car'] = df['Car'].map(d)

features = ['Car','Volume','Weight','CO2']

X = df[features]
y = df['Comprar']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

print(dtree.predict([[1,300,2342,129]]))

plt.subplots(figsize=(15, 10))

tree.plot_tree(dtree, feature_names=features)

plt.show()
