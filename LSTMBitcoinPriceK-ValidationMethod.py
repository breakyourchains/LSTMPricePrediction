# -*- coding: utf-8 -*-
import pymongo
import pandas as pd
import numpy as np
import tensorflow as tf
import sklearn
import math
import matplotlib.pyplot as plt
from tensorflow.keras.layers import LSTM,Dense,Dropout
from tensorflow.keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
from tensorflow.keras import layers
from pymongo import MongoClient
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import KFold


client = MongoClient("mongodb://localhost:27017/")
database = client["local"]
column = database["BitcoinHourly"]


data = pd.DataFrame(list(column.find()))


data = data.drop('_id', axis=1)
data = data.drop('unix', axis=1)
data = data.drop('symbol', axis=1)
data = data.drop('high', axis=1)
data = data.drop('low', axis=1)
data = data.drop('Volume BTC', axis=1)
data = data.drop('Volume USD', axis=1)
data = data.drop('close', axis=1)



data=data.set_index('date')

scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(data)


training_data = math.ceil(0.8 * len(data))
train_data = scaled_data[0:training_data, :]

x_train = []
y_train = []

for i in range(80, len(train_data)):
    x_train.append(train_data[i-80:i, 0])
    y_train.append(train_data[i, 0])

x_train, y_train = np.array(x_train) , np.array(y_train)
x_train = np.reshape(x_train,(x_train.shape[0], x_train.shape[1],1))


test_data = scaled_data[training_data - 80 :,:]
x_test = []

y_test = data.iloc[training_data:,:]

for y in range(80,len(test_data)):
    x_test.append(test_data[y-80:y,0])
x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0],x_test.shape[1],1))

tf.keras.callbacks.EarlyStopping(
    'val_loss',
                          min_delta = 0,
                          patience = 3,
                          verbose = 1,
                          restore_best_weights = True)

es_callback = keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)

n_splits = 5
kf = KFold(n_splits = n_splits, shuffle=True, random_state=42)

for train_index, val_index in kf.split(x_train):
    
    x_train_fold, x_val_fold = x_train[train_index], x_train[val_index]
    y_train_fold, y_val_fold = y_train[train_index], y_train[val_index]
    
    model =Sequential() 
    model.add(LSTM(256, return_sequences=True, input_shape =(x_train.shape[1],1)))
    model.add(Dropout(0.5))
    model.add(LSTM(128, return_sequences=False))
    model.add(Dropout(0.5))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error',metrics =["accuracy"])
    model.fit(x_train_fold ,y_train_fold,epochs=50,validation_split=0.2,callbacks=[es_callback])
    
    predictions = model.predict(x_test)
    predictions = scaler.inverse_transform(predictions)
    print("R-Squared Skoru: ",r2_score(y_test,predictions))




