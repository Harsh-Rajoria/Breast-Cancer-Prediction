from flask import Flask, request, render_template
import pandas
import numpy as np 
import pickle

model=pickle.load(open("model.pkl",'rb'))

#flask app
app=Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
@app.route("/predict",methods=['POST'])
def predict():
    features = request.form['feature']
    features = features.split(',')
    np_features = np.asarray(features, dtype=np.float32)

    # prediction
    pred = model.predict(np_features.reshape(1, -1))
    message = ['Cancrouse' if pred[0] == 1 else 'Not Cancrouse']
    # print(message[0])
    return render_template('index.html', message=message)




#python main
if __name__ == "__main__" :
    app.run(debug=True)