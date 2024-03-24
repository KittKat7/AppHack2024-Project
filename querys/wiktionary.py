import requests, json
import database as db
from PyDictionary import PyDictionary

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
	definition = None #__search_database(word)
	if definition is not None:
		return (f"Definition from database: {definition}")
	else:
		definition = __search_api(word)
		print(definition)
		# db.insertDefinition(word, definition)
		return (definition)
