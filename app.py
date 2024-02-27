from flask import Flask,request,render_template,url_for
import pickle
import numpy as np

model=pickle.load(open('crop_recommend.pkl', 'rb'))

app=Flask(__name__)

@app.route('/')

def index():
    return render_template("crop.html")

@app.route('/', methods=['POST'])


def home():   
    
    N=int(request.form['Nitrogen'])
    P=int(request.form['Phospurous'])
    K=int(request.form['Potassium'])
    temperature=int(request.form['Temperature'])
    humidity=int(request.form['Humidity'])
    ph=int(request.form['ph'])
    rainfall=int(request.form['Rainfall'])
    data = np.array([[N,P,K,temperature,humidity,ph,rainfall]])
    prediction = model.predict(data)
    crop1 = str(prediction[0])

    return render_template('crop.html',result=crop1)
    
    


if __name__=='__main__':
    app.run(debug=True)