import json
import database as db

def queryStack(query: str) -> str:
	rows = db.queryQuestions(query)
	if rows is None:
		with open("examplequery.json") as f:
			content = f.read()
		parse_json = json.loads(content)
		for question in parse_json['items']:
			db.insertQuestion(question['question_id'], question['title'], question['link'], question['score'], question['is_answered'], question['tags'])

	rows = db.queryQuestions(query)
	# print(rows)
	return
	for question in parse_json['items']:
		title = str(question['title'])
		for key in keywords:
			if key in title:
				if title not in list(questions.keys()):
					questions[title] = 1
				else:
					questions[title] = questions[title] + 1

	relevent = list(questions.keys())[0]
	for title in list(questions.keys()):
		if questions[title] > questions[relevent]:
			relevent = title
	return relevent

	keywords = query.strip().split(" ")

	with open("examplequery.json") as f:
		content = f.read()
	parse_json = json.loads(content)
	questions = {}

	
#queryStack



