import pickle
import numpy as np
from flask import Flask, render_template,request,jsonify

#initialize flask application
model=pickle.load(open('model.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_placement():
    cgpa=float(request.form.get('cgpa'))
    iq=int(request.form.get('iq'))
    profile_score=int(request.form.get('profile_score'))

    #predicition
    result=model.predict(np.array([cgpa,iq,profile_score]).reshape(1,3))

    if result[0]==1:
        result = "mallareddy student will place"
    else:
        result='Student need to practice get placed'

    return render_template('index.html',result=result)

if __name__=='__main__':

    #app.run(debug=True)
    app.run(host='0.0.0.0',port=8080)

