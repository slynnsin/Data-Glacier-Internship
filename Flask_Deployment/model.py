# import libraries
import numpy as np
import pandas as pd
import pickle 

df = pd.read_csv('ds_salaries.csv')

# training data
X = df.iloc[:, :3]
Y = df.iloc[:, -1]

from sklearn.linear_model import LinearRegression
reg = LinearRegression()

# fit model with training data
reg.fit(X.values, Y.values)

# saving the model
pickle.dump(reg, open('model.pkl', 'wb'))

# load model to compare results
model = pickle.load(open('model.pkl', 'rb'))

print(model.predict([[2020, 0, 0]]))
