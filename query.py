import json, requests, random
import database as db
from querys.stackexchange import *
from querys.urbandictonary import *
from querys.weather import *
from querys.jokes import *
from querys.news import *
from querys.youtube import *
from querys.about import *
from querys.wiktionary import *

greetings = [
	"hello",
	"hi",
	"hey",
	"yo",
	"hiya",
	"howdy",
	"what's up",
	"greetings",
	"good morning",
	"good afternoon",
	"good evening",
	"hi there",
	"hey there",
	"hello there",
	"sup",
	"morning",
	"afternoon",
	"evening",
	"hola",
	"ciao"
]

def __activates(query: str, keys: list[str]):
	for key in keys:
		if query.startswith(key):
			return True
	return False

dbInInit: bool = False

previous_response = ""

def query(query: str) -> str:
	global previous_response
	if len(query.strip()) == 0:
		return ""
	global dbInInit
	output = ""
	if not dbInInit:
		db.initdb()
	if __activates(query, greetings):
		output = queryGreeting()
	elif query.startswith("define"):
		term = query[len("define "):]
		output = queryWiktionary(term)
	elif query.startswith("urban"):
		term = query[len("urban "):]
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
	elif query.startswith("play "):
		video = query[len("play "):]
		output = queryYoutube(video)
	elif __activates(query, aboutKeywords):
		output = queryAbout()
	elif query.startswith("repeat"):
		return previous_response
	elif query.startswith("say"):
		output = query[len("say "):]
	else:
		output = queryStack(query)
	if output is None:
		output = "ERROR 404 - No output found"
	previous_response = output
	return output
#query

def queryGreeting() -> str:
	greetings = ["Hi there!", "Hey!", "Good morning!", "Good afternoon!",
				"Greetings!", "Howdy!", "What's up?", "Yo!", "Hiya!", "Salutations!",
				"Well met!", "Hello there!", "Yer", "What's new?", "Bonjour!", "Ciao!"]
	return random.choice(greetings)

def __queryTest(query: str) -> str:
	response_API = requests.get('https://api.covid19india.org/state_district_wise.json')
	data = response_API.text
	parse_json = json.loads(data)
	active_case = parse_json['Andaman and Nicobar Islands']['districtData']['South Andaman']['active']
	return "Active cases in South Andaman: " + str(active_case)
#queryTest
