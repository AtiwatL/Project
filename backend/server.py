from flask import Flask, send_from_directory
#import extract feature
import os
import librosa
import numpy as np
import tensorflow as tf
from tensorflow import keras

#import model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,Activation,Flatten

from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from api.HelloApiHandler import HelloApiHandler

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app) #comment this on deployment
api = Api(app)

def create_model():
    model=Sequential()

    model.add(Flatten(input_shape=(40,)))

    ###first layer
    model.add(Dense(100, Activation('relu')))
    model.add(Dropout(0.5))

    ###second layer
    model.add(Dense(200, Activation('relu')))
    model.add(Dropout(0.5))

    ###third layer
    model.add(Dense(100, Activation('relu')))
    model.add(Dropout(0.5))

    ###final layer
    model.add(Dense(2, Activation('softmax')))
    
    model.compile(loss='categorical_crossentropy',metrics=['accuracy'],optimizer='adam')
    
    return model

model = create_model()

# Restore the weights
model.load_weights('save_model/my_model.ckpt')

def features_extractor(filename):
    audio, sample_rate = librosa.load(filename, res_type='kaiser_fast')
    mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfccs_scaled_features = np.mean(mfccs_features.T, axis=0)
    
    return mfccs_scaled_features

@app.route('/', methods=["GET","POST"])
def predictAudio():
    filename = './ProjectSounds/HumanExample2.wav'
    audio, sample_rate = librosa.load(filename, res_type='kaiser_fast')
    mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfccs_scaled_features = np.mean(mfccs_features.T, axis=0)
    
    prediction_feature = features_extractor(filename)
    prediction_feature = prediction_feature.reshape(1,-1)
    prediction_class = model.predict_classes(prediction_feature)
    
    if prediction_class == [0]:
        result = "Sorry!, You are not human"
    else :
        result = "Yes!, Let's go you are human"
    
    return result


if __name__ == '__main__':
    app.run(debug=True)