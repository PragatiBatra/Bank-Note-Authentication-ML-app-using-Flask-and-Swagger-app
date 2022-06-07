# -*- coding: utf-8 -*-
"""
Created on Sat May 28 12:19:29 2022

@author: Pragati
"""

from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger 


app = Flask(__name__)
Swagger(app)

pickle_in = open('classifier.pkl','rb')
classifier= pickle.load(pickle_in)

@app.route('/')
def welcome():
    return 'Welcome All'

@app.route('/predict', methods= ['GET'])
def predict_note_authentication():
    
    
    """Let' authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
      - name: variance   #take care of spacingas it can cause huge issue
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
    
    
    """
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return 'Hello the answer is '+str(prediction)


@app.route('/predict_file',methods= ['POST'])
def predict_note_fileauthentication():
    
    """Let' authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
    responses:
        200:
            description: The output values
    
    """
        
    df_test = pd.read_csv(request.files.get('file'))
    prediction= classifier.predict(df_test)
    return str(list(prediction))



if __name__ == '__main__':
    app.run()