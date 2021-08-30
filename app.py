import json
from typing import Union

import numpy as np
import pandas as pd
from flask import Flask, render_template, request

from database.queries import Queries
from utils.processor import InputProcessor

app = Flask(__name__)
db_query = Queries()
cols = ['author', 'edition', 'category']


def __init__():
    db_query.create_tables()


@app.route("/", methods=["GET"])
def home() -> str:
    """
    Homepage for this API.
    :return: Basic info about the API
    """
    return render_template("home.html")


@app.route("/predict", methods=["POST"])
def predict() -> Union[str, int]:
    """
    Reads and validates the data from POST request, predicts bookdepository.com book price.
    :return: http response with json
    """
    continue_execution = True
    try:
        request_data = json.loads(request.data)
        print(request_data)
        continue_execution = False
    except ValueError as error:
        pass
    else:
        input_processor = InputProcessor(request_data)

    if continue_execution:
        try:
            features =  [x for x in request.form.values()]
            print(features)
            request_data = dict(zip(cols, features))
            input_processor = InputProcessor(request_data)
        except ValueError:
            return json.dumps({"response": "error", "message": "Invalid json format"})
        else:
            input_processor = InputProcessor(request_data)

    validation = input_processor.validate
    if validation["response"] == "ok":
        prediction = input_processor.predict
        db_query.log_prediction(request_data, prediction)
        pred = json.dumps(prediction), 200
        return render_template('home.html',pred=f"Expected book price is: US${prediction['predicted_price']}")
    return json.dumps(validation), 400


@app.route("/history", defaults={"amount": 10}, methods=["GET"])
@app.route("/history/<amount>", methods=["GET"])
def show_history(amount: int) -> Union[str, int]:
    """
    Returns a specified number of successful price predictions. Default =  10.
    :param amount
    :return: http response with json
    """
    return json.dumps({"prediction_history": db_query.get_last_records(amount)}), 200
