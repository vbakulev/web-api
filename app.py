from flask import *
from pycaret.classification import *
import pandas as pd
import numpy as np

app = Flask(__name__)

model = load_model('model')
cols = [
    'Gender',
    'Age',
    'Neighbourhood',
    'Scholarship',
    'Hipertension',
    'Diabetes',
    'Alcoholism',
    'Handcap'
]


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/predict', methods=['POST'])
def predict():
    list_features = [x for x in request.form.values()]

    if list_features[0] == 'Male':
        list_features[0] == 'M'
    elif list_features[0] == 'Famale':
        list_features[0] == 'F'

    for i in range(3, 8):
        if list_features[i] == 'Yes':
            list_features[i] = '1'
        elif list_features[i] == 'No':
            list_features[i] = '0'

    final = np.array(list_features)
    data_unseen = pd.DataFrame([final], columns=cols)
    prediction = predict_model(model, data=data_unseen)

    prediction = prediction.Label[0]
    if prediction == 'Yes':
        predict_text = 'Will not come!'
    elif prediction == 'No':
        predict_text = 'Will come!'
    return render_template('home.html', pred=predict_text)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
