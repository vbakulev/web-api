from flask import *

app = Flask(__name__)


cols = ['Gender', 'Age']


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/predict', methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    prediction = '1'
    prediction = int(prediction)
    return render_template('home.html', pred='Expected Bill will be {}'.format(prediction))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
