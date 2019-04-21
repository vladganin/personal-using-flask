import requests
import operations_calc as op
import re
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/calculator', methods=['GET','POST'])
def computing():
	if request.method == 'POST':
		values = {"number1": None, "number2": None}
		number = request.form.get("number")
		number = int(number)
		if values["number1"] == None:
			values["number1"] = number
			temp = values["number1"]
			return render_template('calculator.html', arg2=temp, arg4=None)
		elif values["number2"] == None:
			values["number2"] = number
			result = values["number1"] + values["number2"]
			return render_template('calculator.html', arg4=result)
	else:
		return render_template('calculator.html')

@app.route('/in_deployment', methods=['GET', 'POST'])
def sorry():
	return render_template('sorry.html')

@app.route('/backgrounds_app', methods=['GET', 'POST'])
def backgroundsAppRun():
	return render_template('backgrounds/index.html')
if __name__ == '__main__':
	app.run()