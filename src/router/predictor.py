from flask import Blueprint, request, jsonify, render_template
import time
import os
from model import RandomForest, ConvModel
from db import db, add_phishing_record
from const import FEATURES

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


model = RandomForest("model/weights/rf_data_balance.pkl")

predictor = Blueprint('predictor', __name__)


@predictor.route('/', methods=["GET", "POST"])
def survey():
    sublist = [list(FEATURES.keys())[n:n+3]
               for n in range(0, len(list(FEATURES.keys())), 3)]

    return render_template('index.html', data=sublist, features=FEATURES)


@predictor.route("/predict", methods=["POST"])
def predict():
    # Initialize the dictionary for the response.
    data = {"success": False}

    # Grab and process the incoming json.
    start = time.time()
    incoming = request.get_json()
    url = incoming["url"]

    if url == '':
        return jsonify({'message': 'Cannot connect to website. Your url might be incorrect, or the website is down'})

    data["predictions"] = []
    prediction, url_feature_vector = model.predict(url)

    if prediction is not None:
        prediction = prediction[0]
        print(url_feature_vector)
        phishing_record = {
            item[0]: item[1]
            for item in url_feature_vector
        }
        phishing_record["url"] = url
        phishing_record["prediction"] = int(prediction)
        add_phishing_record(phishing_record)
    else:
        return jsonify(data)
    end = time.time() - start

    if prediction > 0.5:
        result = "URL is probably phishing"
    else:
        result = "URL is probably NOT phishing"

    # Processes prediction probability.
    prediction = float(prediction)
    prediction = prediction * 100

    r = {"result": result, "phishing percentage": prediction, "url": url}
    data["predictions"].append(r)

    # Show that the request was a success.
    data["success"] = True
    data["time_elapsed"] = end

    return jsonify(data)
