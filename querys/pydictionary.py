import requests, json
import database as db
from PyDictionary import PyDictionary

defineKeywords = [
	"he fine",
	"define",
	"fine",
	"feign",
	"vine",
	"line",
	"shine",
	"pine",
	"dine",
	"wine",
	"mine",
	"sign",
	"rhine",
	"thine",
	"shrine",
	"twine",
	"whine",
	"spine"
]

def __search_database(word):
	return db.queryDefinition(word)

def __search_api(word):
	dictionary = PyDictionary()
	ret = ""
	for key in list(dictionary.meaning(word).keys()):
		for v in dictionary.meaning(word)[key]:
			ret += f"{key}: {v}\n"
	return ret

def queryWiktionary(word):
	definition = __search_database(word)
	if definition is not None:
		return (f"Definition from local database: {definition[1]}")
	else:
		definition = __search_api(word)
		db.insertDefinition(word, definition)
		return (definition)
