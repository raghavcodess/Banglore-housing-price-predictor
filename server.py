from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location', methods=['GET'])

def get_location():
	response = jsonify({
		'Locations': util.get_location()
		})
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response


@app.route('/predict_price', methods=['GET', 'POST'])
def predict_price():
	location = request.form['1']
	total_sqft = float(request.form['2'])
	bath = int(request.form['3'])
	size = int(request.form['4'])
	
	response = jsonify({
		'price' : util.predict_price(location,total_sqft,bath,size)
		})
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response


if __name__ == "__main__":
	app.run()
	