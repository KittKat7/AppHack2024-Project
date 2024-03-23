import json
import database

def __queryStack(query: str) -> str:

	with open("examplequery.json") as f:
		content = f.read()
	parse_json = json.loads(content)
	parsed = parse_json['items'][0]['tags']
	return parsed
#queryStack
