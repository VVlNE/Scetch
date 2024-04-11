import os
import flask
from flask import request

def predict(image):
    class_name = 0
    class_number = [0]
    probability = [1.0]
    return class_name, class_number, probability

app = flask.Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def connection_request():
    return "Successful Connection"

@app.route('/predictClass', methods=['GET', 'POST'])
def prediction_request():
    if request.method == 'POST':
        file = request.files['external_image']
        image_name = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name))
        class_name, class_number, probability = predict(image_name)

        for (name, number) in zip(class_name, class_number):
            print('{} ({}) {:.4f})'.format(name, number, probability))
        print()

        return class_name
    else:
        return []

app.config['UPLOAD_FOLDER'] = ""
app.run(host = "0.0.0.0", port = 5000, debug = False)