import json
import pickle
import numpy as np

__columns = None
__location = None
__model = None

def predict_price(location,total_sqft,bath,size):
	reading_data()

	try:
		loc_index = __columns.index(location.lower())
	except:
		loc_index=-1

	result = np.zeros(len(__columns))
	result[0] = size
	result[1] = total_sqft
	result[2] = bath
	if loc_index >= 0:
		result[loc_index] = 1
	return round(__model.predict([result])[0],2)

def get_location():
	reading_data()
	return __location


def reading_data():
	global __columns
	global __location

	with open('columns.json','rb') as f:
		__columns = json.load(f)['data_columns']
		__location = __columns[3:]
	global __model
	if __model is None:
		with open('banglore_home_prices_model.pickle','rb') as f:
			__model = pickle.load(f)

