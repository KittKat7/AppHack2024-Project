import json, requests
import database as db
from querys.stackexchange import *
from querys.urbandictonary import *
from querys.weather import *
from querys.jokes import *
from querys.news import *


dbInInit: bool = False

def query(query: str) -> str:
	global dbInInit
	output = ""
	if not dbInInit:
		db.initdb()
	if query.startswith("define"):
		term = query[len("define "):]
		output = queryUrban(term)
	elif query.startswith("current weather"):
		city = query[len("current weather "):]
		if len(city) == 0:
			city = None
		output = queryWeather(city)
	elif query.startswith("tell me a joke"):
		output = queryJoke()
	elif query.startswith("news on"):
		topic = query[len("news on "):]
		output = queryNews(topic)
	else:
		output = queryStack(query)
	if output is None:
		output = "ERROR 404 - No output found"
	return output
#query

def __queryTest(query: str) -> str:
	response_API = requests.get('https://api.covid19india.org/state_district_wise.json')
	data = response_API.text
	parse_json = json.loads(data)
	active_case = parse_json['Andaman and Nicobar Islands']['districtData']['South Andaman']['active']
	return "Active cases in South Andaman: " + str(active_case)
#queryTest


if __name__ == "__main__":
	print(query("hi"))