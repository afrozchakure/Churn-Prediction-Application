import os
import json
import pickle
from flask import Flask, jsonify, request, render_template, Response, send_file
from serializer import serializerJson
import io
import base64


HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/explore')
def explore_is_up():
    return render_template('explore.html')


@app.route('/about')
def about_is_up():
    return render_template('about.html')


app.config['PDF_FOLDER'] = 'static/pdf/'
app.config['TEMPLATE_FOLDER'] = 'templates/'


@app.route('/conclusions')
def conclusion():
    return render_template('conclusion.html')


@app.route('/download')
def download_webpage():
    path = "EDA_and_Conclusion.pdf"
    return send_file(path, as_attachment=True)


@app.route('/', methods=['GET'])
def server_is_up():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def predict_churn():
    to_form = request.form

    to_predict = serializerJson(to_form)

    prediction = 'Congratulations! The customer will not churn 😀🙅‍♂️'
    if to_predict[1] == '1':
        prediction = 'Oh no! The customer will churn 😞'
    else:
        prediction = 'Congratulations! The customer will not churn 😀🙅‍♂️'
    return render_template('result.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
