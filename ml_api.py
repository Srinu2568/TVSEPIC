# imports
import uvicorn
from fastapi import FastAPI
from FeaturesNote import FeatureNote
import pickle
import json
import numpy as np
import pandas as pd

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)

pickle_in = open('price_pred.pkl', 'rb')
rf = pickle.load(pickle_in)

params = '''Car	Location	
Year	Kilometers_Driven	
Owner_Type	Fuel_Type	Power'''

@app.get('/')
def index():
    return {'message': 'Hello, Stranger'}

@app.post('/predict')
def predict_price(data: FeatureNote):
    data = data.dict()
    print(data)
    car = data['Car']
    location = data['Location']
    year = data['Year']
    km_driven = data['Kilometers_Driven']
    owner_type = data['Owner_Type']
    fuel_type = data['Fuel_Type']
    power = data['Power']
    prediction = rf.predict([[car, location, year, km_driven, owner_type, fuel_type, power]])
    return {
        'prediction': prediction[0]
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)