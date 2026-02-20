import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

data = pd.read_csv("data/traffic.csv")

X = data[['vehicles']]
y = data['green_time']

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "models/traffic_model.pkl")

print("Model trained successfully")