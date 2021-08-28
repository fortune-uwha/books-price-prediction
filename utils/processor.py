import pickle
import numpy as np
import pandas as pd
from utils.validator import InputValidator

import pickle
import numpy as np

with open("pipe.pkl", "rb") as model:
    model = pickle.load(model)


class InputProcessor:
    """
    Validates and transforms input data and make predictions about prices.
    """

    def __init__(self, input_data: dict) -> None:
        self.__input_data = input_data
        self.__model = model


    @property
    def validate(self) -> dict:
        """
        Uses the InputValidator class to validate the data.
        :param: None
        :return: json response - ok or errors
        """
        validate = InputValidator(self.__input_data)

        if not validate.validate_keys["response"] == "ok":
            return validate.validate_keys

        if not isinstance(validate.validate_input, bool):
            return validate.validate_input

        return {"response": "ok"}

    @property
    def input_to_df(self) -> pd.DataFrame:
        """
        Function which turns input from dict to dataframe.
        :param: None
        :return: dataframe of features.
        """
        data = pd.DataFrame.from_dict(self.__input_data, orient="index").T
        return data

    @property
    def predict(self) -> dict:
        """
        Predicts the book price using features provided from input data.
        :param: None
        :return: float predicted book price
        """
        processed_input = self.input_to_df
        predicted_price = self.__model.predict(processed_input)

        return {
            "response": "ok",
            "predicted_price": round(predicted_price[0],2)
        }
