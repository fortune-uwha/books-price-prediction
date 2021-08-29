# Books Depository Price Prediction App
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Issues: 0](https://img.shields.io/badge/Issues-0-green.svg)](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue)
![](https://github.com/fortune-uwha/books_price_prediction/blob/main/assets/homepage%20api.jpg?raw=true)
An end-to-end machine learning project

## Table of Contents
* [General Information](#general-information)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
* [Contributing](#contributing)
* [License](#license)


## General Information
The web app is intended for predicting house prices in Boston, United States. Model was trained on the  predefined and cleaned [dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html#sklearn.datasets.load_boston) and can predict price by given parameters. Trained model is saved to model.pkl file.

## Setup
* Create Heroku project and Heroku PostgreSQL database
* Add your database credentials to .env file (make sure to rename .env_template to .env)
* Clone the repository and create a virtualenv. 
* Run `pip install -r requirements.txt` to install project requirements
* Type `flask run` to start the app

## Usage
The API endpoint is a Flask app hosted on heroku https://books-price-prediction.herokuapp.com/predict which you can access with any REST API client, such as Postman. There is only one main route:

* /predict - takes POST requests, predicts price by parameters provided.
* /history - takes GET requests and returns last 10 most recent requests and predictions from the database
* /history/amount - you can supply an optional number of results to return by adding an int amount, for example https://books-price-prediction.herokuapp.com/history/5

#### Input json format example:
```python
{
    "author": "Bethany Roberts",
    "edition": "Hardback",
    "category": "Medical"
}
```
#### Postman usage example:
![](https://github.com/fortune-uwha/books_price_prediction/blob/main/assets/postman_example.jpg?raw=true)

#### Using Jupyter Notebook

You can also use requests module and use the API in a Jupyter notebook to view history like this:
```python
import json
import requests

url = 'https://books-price-prediction.herokuapp.com/history'

response = requests.get(url, data=json.dumps(json_input))
print (f"response: {json.loads(response.content)}")
```
## Project Status
Project is: in progress

## Acknowledgements
This project was based on [Turing College](https://www.turingcollege.com) learning on building an end-to-end-machine learning project.

## Contact
Created by [@fortune_uwha](https://fortune-uwha.github.io/Fortune_Portfolio/) - feel free to contact me!

## Contributing
Feel free to submit an issue with your ideas or comments. I will be happy to see your way of scaffolding Flask applications.

## License
This project is open source and available under the terms of the [MIT](https://opensource.org/licenses/MIT) license.

