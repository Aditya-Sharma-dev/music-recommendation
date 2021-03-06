import numpy as np
from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)
#Load the model
model = pickle.load(open('savedmodel.sav','rb'))

@app.route('/')
def home():
    result = ' '
    return render_template('index.html', **locals() )


@app.route('/predict', methods=['POST', 'GET'])
def recommend():
    userID = request.form['enginesize']
    result = model.recommend([userID])
    return render_template('index.html', **locals() )
# prediction_text='CO2 Emission of the vehicle is :{}'.format(result)


if __name__ == '_main_':
    app.run(debug=True)