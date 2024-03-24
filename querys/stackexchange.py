import json, requests
import database as db

def queryStack(query: str) -> str:
	answer_body = ""

	try:
		question = __queryQuestion(query)
	except:
		question = None
		answer_body = "An error occured"
	
	if question is None:
		return None

	try:
		answer_body = __queryAnswer(question['id'])
	except:
		answer_body = None
	
	question_title = question['title']
	if answer_body is None:
		answer_body = "Unable to find an answer"
	return f"{question_title}\n{answer_body}"
#queryStack

def __queryQuestion(query: str):
	rows = db.queryQuestions(query)
	if rows is None and not db.hasQueried(query):
		# with open("examplequery.json", encoding="utf-8") as f:
		# 	content = f.read()
		print("QUESTION REQUEST")
		db.insertQuery(query)
		request = requests.get(f'https://api.stackexchange.com/2.3/similar?order=desc&sort=activity&title={query}&site=stackoverflow&filter=!nNPvSNdWme')
		print(request.text)
		parse_json = json.loads(request.text)
		for question in parse_json['items']:
			db.insertQuestion(question['question_id'], question['title'], question['link'], question['score'], question['is_answered'], question['tags'])
		if len(parse_json['items']):
			db.insertQuestion(question['question_id'], question['title'], question['link'], question['score'], question['is_answered'], question['tags'])
		print(rows["quota_remaining"])


	rows = db.queryQuestions(query)

	questions = {}
	relevence = {}
	query = query.split(" ")
	for row in rows:
		questions[row[1]] = {'id': row[0], 'title': row[1], 'link': row[2], 'score': row[3], 'answered': row[4]}
	for question in list(questions.keys()):
		title = question
		for word in query:
			if word in title.lower().split(" "):
				if title in list(relevence.keys()):
					relevence[title] = relevence[title] + 1
				else:
					relevence[title] = 1
	if len(list(relevence.keys())) == 0:
		return None
	mostrelevent = list(relevence.keys())[0]
	for q in relevence:
		if relevence[q] > relevence[mostrelevent]:
			mostrelevent = q

	return questions[mostrelevent]
#__queryQuestions

def __queryAnswer(query: int):
	rows = db.queryAnswers(query)
	if rows is None and not db.hasQueried(query):
		# with open("example_answers.json", encoding="utf-8") as f:
		# 	content = f.read()
		print("ANSWER REQUEST")
		db.insertQuery(query)
		request = requests.get(f'https://api.stackexchange.com/2.3/questions/{query}/answers?order=desc&sort=activity&site=stackoverflow&filter=withbody')
		parse_json = json.loads(request.text)
		for question in parse_json['items']:
			db.insertAnswer(question['answer_id'], question['question_id'], question['body'], question['score'], question['is_accepted'])
		print(rows["quota_remaining"])

	rows = db.queryAnswers(query)
	if rows is None:
		return None
	relevent = ""
	score = None
	answers = []
	for row in rows:
		answers.append({'id': row[0], 'question': row[1], 'body': row[2], 'score': row[3], 'answered': row[4]})
	for a in answers:
		if score is None or a['score'] > score:
			relevent = a['body']
			score = a['score']
	print(f"Remaining API Quota: {parse_json['quota_remaining']}")
	return relevent if score is not None else None
#__queryAnswers
	
#queryStack



