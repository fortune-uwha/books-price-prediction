import pytest
from utils.validator import InputValidator
from utils.processor import InputProcessor
from database.database import Database
import requests


#Helpers
valid_input_sample = {
  "author": "Claire Freedman",
  "edition": "Paperback",
  "category": "love"
}

invalid_input_sample = {
  "author": 444,
  "edition": "Paperback",
  "category": 5
}


def test_validator_valid():
    validator = InputValidator(valid_input_sample)
    validate = validator.validate_input
    assert validate["response"] == "ok"


def test_validator_invalid():
    validator = InputValidator(invalid_input_sample)
    validate = validator.validate_input
    assert validate["response"] == "error"


def test_processor_validate():
    input_processor = InputProcessor(valid_input_sample)
    validation = input_processor.validate
    assert validation["response"] == "ok"


def test_predict():
    input_processor = InputProcessor(valid_input_sample)
    result = input_processor.predict
    assert pytest.approx(True, 14) == result["predicted_price"]


def test_get_history():
    url = "https://books-price-prediction.herokuapp.com/history"
    response = requests.get(url)
    history = response.json()
    assert (len(history["prediction_history"]) == 10)