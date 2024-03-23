import requests, json
from querys.stackexchange import *

def query(query: str) -> str:
	return __queryTest(query)
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