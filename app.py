from flask import Flask,render_template,request
import pickle
import pandas as pd
import numpy as np
app=Flask(__name__)
model=pickle.load(open('XGBoost.pkl','rb'))

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        Time=float(request.form['time'])
        V1=float(request.form['V1'])
        V2=float(request.form['V2'])
        V3=float(request.form['V3'])
        V4=float(request.form['V4'])
        V5=float(request.form['V5'])
        V6=float(request.form['V6'])
        V7=float(request.form['V7'])
        V8=float(request.form['V8'])
        V9=float(request.form['V9'])
        V10=float(request.form['V10'])
        V11=float(request.form['V11'])
        V12=float(request.form['V12'])
        V13=float(request.form['V13'])
        V14=float(request.form['V14'])
        V15=float(request.form['V15'])
        V16=float(request.form['V16'])
        V17=float(request.form['V17'])
        V18=float(request.form['V18'])
        V19=float(request.form['V19'])
        V20=float(request.form['V20'])
        V21=float(request.form['V21'])
        V22=float(request.form['V22'])
        V23=float(request.form['V23'])
        V24=float(request.form['V24'])
        V25=float(request.form['V25'])
        V26=float(request.form['V26'])
        V27=float(request.form['V27'])
        V28=float(request.form['V28'])
        Amount=float(request.form['Amount'])

        input=np.asarray([[Time,V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,Amount]])
        
        prediction=model.predict(input)
        if prediction==0:
            return render_template('index.html',prediction_text="This is a Legitimate transaction")
        else:
            return render_template('index.html',prediction_text="This is a Fraud Transaction")
    else:
        return render_template('index.html')
    
if __name__=="__main__":
    app.run(debug=True)