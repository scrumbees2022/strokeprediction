
#Importing modules
from flask import Flask, render_template, request
import joblib
import numpy as np
import pickle
import os,sys

## Making an instance of Flask
app = Flask(__name__)
#Flask decorator to render the home page
@app.route("/")
def index():
    return render_template("home.html")
## Getting the values from user
@app.route("/result",methods=['POST','GET'])
def result():
    gender=int(request.form['gender'])
    age=int(request.form['age'])
    hypertension=int(request.form['hypertension'])
    heart_disease = int(request.form['hypertension'])
    ever_married = int(request.form['ever_married'])
    work_type = int(request.form['work_type'])
    Residence_type = int(request.form['Residence_type'])
    avg_glucose_level =float(request.form['avg_glucose_level'])
    bmi = float(request.form['bmi'])
    smoking_status = int(request.form['smoking_status'])

    x=np.array([gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status]).reshape(1,-1)
    scaler_path = os.path.join('C:/Users/USER/Documents/Renju/Ineuron/Projects/StrokePrediction/', 'models/scaler.pkl')
    scaler = None
    with open(scaler_path,'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
    x=scaler.transform(x)

    model_path = os.path.join('C:/Users/USER/Documents/Renju/Ineuron/Projects/StrokePrediction/', 'models/decisionTree.sav')
    print(model_path)
    decisionTree = joblib.load(model_path)
    Y_pred = decisionTree.predict(x)[0]

    print(Y_pred)



    if Y_pred == 0:
        print("I am here")
        return render_template("nostroke.html")
    else:
        return render_template("stroke.html")

if __name__ == "__main__":
    app.run(debug=True,port=5000)