import numpy as np
# Feature map
_map = {'class': {'e': 0, 'p': 1},  # Manual label encoding
        'cap-shape': {'b':'bell', 'c':'conical', 'x':'convex', 'f':'flat', 'k':'knobbed', 's':'sunken'},
        'cap-surface': {'f':'fibrous', 'g':'grooves', 'y':'scaly', 's':'smooth'},
        'cap-color': {'n':'brown', 'b':'buff', 'c':'cinnamon', 'g':'gray', 'r':'green', 'p':'pink', 'u':'purple', 'e':'red', 'w':'white', 'y':'yellow'},
        'gill-attachment': {'a':'attached', 'd':'descending', 'f':'free', 'n':'notched'},
        'gill-spacing': {'c':'close', 'w':'crowded', 'd':'distant'},
        'gill-size': {'b':'broad', 'n':'narrow'},
        'gill-color': {'k':'black', 'n':'brown', 'b':'buff', 'h':'chocolate', 'g':'gray', 'r':'green', 'o':'orange', 'p':'pink', 'u':'purple', 'e':'red', 'w':'white', 'y':'yellow'},
        'stalk-shape': {'e':'enlarging', 't':'tapering'},
        'stalk-root': {'b':'bulbous', 'c':'club', 'u':'cup', 'e':'equal', 'z':'rhizomorphs', 'r':'rooted', '?':np.nan},
        'stalk-surface-above-ring': {'f':'fibrous', 'y':'scaly', 'k':'silky', 's':'smooth'},
        'stalk-surface-below-ring': {'f':'fibrous', 'y':'scaly', 'k':'silky', 's':'smooth'},
        'stalk-color-above-ring': {'n':'brown', 'b':'buff', 'c':'cinnamon', 'g':'gray', 'o':'orange', 'p':'pink', 'e':'red', 'w':'white', 'y':'yellow'},
        'stalk-color-below-ring': {'n':'brown', 'b':'buff', 'c':'cinnamon', 'g':'gray', 'o':'orange', 'p':'pink', 'e':'red', 'w':'white', 'y':'yellow'},
        'veil-type': {'p':'partial', 'u':'universal'},
        'veil-color': {'n':'brown', 'o':'orange', 'w':'white', 'y':'yellow'},
        'ring-number': {'n':'none', 'o':'one', 't':'two'},
        'ring-type': {'c':'cobwebby', 'e':'evanescent', 'f':'flaring', 'l':'large', 'n':'none', 'p':'pendant', 's':'sheathing', 'z':'zone'},
        'bruises': {'t':'bruises', 'f':'no'},
        'odor': {'a':'almond', 'l':'anise', 'c':'creosote', 'y':'fishy', 'f':'foul', 'm':'musty', 'n':'none', 'p':'pungent', 's':'spicy' },
        'spore-print-color': {'k':'black', 'n':'brown', 'b':'buff', 'h':'chocolate', 'r':'green', 'o':'orange', 'u':'purple', 'w':'white', 'y':'yellow'},
        'population': {'a':'abundant', 'c':'clustered', 'n':'numerous', 's':'scattered', 'v':'several', 'y':'solitary'},
        'habitat': {'g':'grasses', 'l':'leaves', 'm':'meadows', 'p':'paths', 'u':'urban', 'w':'waste', 'd':'woods'}}

import os
_dir = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(_dir, '../../data/', 'data.csv')

import pandas as pd
df = pd.read_csv(path)  # Load and format dataset
for col, i in _map.items():
    df[col] = df[col].replace(i)
df.columns = df.columns.str.replace("-", " ")

drop_list = ['gill attachment', 'stalk root', 'stalk surface below ring', 'stalk color below ring', 'veil type', 'veil color', 'ring number']
for col in drop_list:  # Drop irrelevant features
    df.drop(col, axis=1, inplace=True)

from sklearn.model_selection import train_test_split as split
train_df, test_df = split(df, random_state=42)
y_train = train_df['class']
y_test = test_df['class']

path = os.path.join(_dir, '../../data/', 'test.csv')
test_df.to_csv(path, index=False)
train_df = train_df.drop('class', axis=1)
test_df = test_df.drop('class', axis=1)

from sklearn.feature_extraction import DictVectorizer
dv = DictVectorizer(sparse=False)  # One-hot encoding
train_dict = train_df.to_dict(orient="records")
X_train = dv.fit_transform(train_dict)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

import pickle
with open('./model.bin', 'wb') as f_out:
   pickle.dump((dv, model), f_out)
f_out.close()

