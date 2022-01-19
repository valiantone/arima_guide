
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def myapp():
    message = "Welcome to our forecaster!"
    return message

def get_prepared_forecasts():
    # returns my_result2.values (A list of your results 12 forecasts for 2021)
    # add all your code here
    return

@app.route('/predict', methods = ['POST']) # this creates an endpoint for /predict
def predict():
    data = request.get_json()
    month_var = data["month"]
    year_var = data["year"]

    if year_var != 2021:
        return jsonify("invalid year input")

    if month_var > 12:
        return jsonify("invalid month input")

    my_result2 = [15]*12
    return jsonify(my_result2[month_var-1])