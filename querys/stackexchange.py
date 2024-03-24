import json, requests
import database as db
from bs4 import BeautifulSoup
import globals as globals

key = ""
try:
	with open(".secret_key", encoding="utf-8") as f:
		key = f.read()
except:
	""

# Function to remove tags
def remove_tags(html):
	# parse html content
	soup = BeautifulSoup(html, "html.parser")
	for data in soup(['style', 'script']):
		# Remove tags
		data.decompose()
	# return data by retrieving the tag content
	return ' '.join(soup.stripped_strings)
#remove_tags

def rank_strings(search_query, string_list):
	# Tokenize the search query
	query_tokens = set(search_query.lower().split())
	
	# Calculate relevance score for each string
	scored_strings = []
	for string in string_list:
		# Tokenize and lowercase the string
		string_tokens = set(string.lower().split())
		
		# Calculate overlap between query tokens and string tokens
		overlap = len(query_tokens.intersection(string_tokens))
		
		# Calculate relevance score as the ratio of overlap to total tokens in the string
		relevance_score = overlap / len(string_tokens)
		
		scored_strings.append((string, relevance_score))
	
	# Sort the strings by relevance score
	ranked_strings = sorted(scored_strings, key=lambda x: x[1], reverse=True)
	
	# Return the list of strings sorted by relevance
	return [item[0] for item in ranked_strings]
#rank_strings

def queryStack(query: str) -> str:
	answer_body = ""
	question = __queryQuestion(query)

	try:
		answer_body = __queryAnswer(question['id'])
	except:
		answer_body = None

	if question is None:
		return "An error has occured"

	question_title = question['title']
	question_body = question['body']
	if answer_body is None:
		answer_body = "Unable to find an answer"
	return f"TITLE: {remove_tags(question_title)}\nQUESTION: {remove_tags(question_body)}\n\nANSWER: {remove_tags(answer_body)}"
#queryStack

def __queryQuestion(query: str):
	rows = db.queryQuestions(query)
	if (rows is None or not db.hasQueried(query)) or globals.force_api_usage:
		# with open("examplequery.json", encoding="utf-8") as f:
		# 	content = f.read()
		print("QUESTION REQUEST")
		db.insertQuery(query)
		request = requests.get(f'https://api.stackexchange.com/2.3/similar?order=desc&sort=activity&title={query}&site=stackoverflow&filter=!nNPvSNPI7A&key={key}')
		parse_json = json.loads(request.text)
		print(f"Remaining API Quota: {parse_json['quota_remaining']}")
		question = parse_json['items'][0] if len(parse_json['items']) > 0 else None
		if question == None:
			return None
		rows = [(question['question_id'], question['title'], question['body'], question['link'], question['score'], question['answer_count'], question['is_answered'])]
		for question in parse_json['items']:
			db.insertQuestion(question['question_id'], question['title'], question['body'], question['link'], question['score'], question['answer_count'], question['is_answered'], question['tags'])

	if not globals.force_api_usage:
		rows = db.queryQuestions(query)

	if rows is None:
		return None
	questions = {}
	relevence = []
	for row in rows:
		questions[row[1]] = {'id': row[0], 'title': row[1], 'body': row[2], 'link': row[3], 'score': row[4], 'answers': row[5], 'answered': row[6]}
	
	relevence = rank_strings(query, questions)
	# for title in list(questions.keys()):
	# 	body = questions[title]['body']
	# 	for word in query:
	# 		if word in title.lower().split(" "):
	# 			if title in list(relevence.keys()):
	# 				relevence[title] = relevence[title] + 2
	# 			else:
	# 				relevence[title] = 2
	# 		# if word in body.lower().split(" "):
	# 		# 	if title in list(relevence.keys()):
	# 		# 		relevence[title] = relevence[title] + 1
	# 		# 	else:
	# 		# 		relevence[title] = 1
	if len(list(relevence)) == 0:
		return None

	mostrelevent = None
	for q in relevence:
		if mostrelevent is None and questions[q]['answered']:
			mostrelevent = q
			break
	if mostrelevent is None:
		for q in relevence:
			if mostrelevent is None and questions[q]['answers'] > 0:
				mostrelevent = q
				break
	if mostrelevent is None:
		for q in relevence:
			if mostrelevent is None:
				mostrelevent = q
				break

	return questions[mostrelevent]
#__queryQuestions

def __queryAnswer(query: int):
	rows = db.queryAnswers(query)
	if rows is None and not db.hasQueried(query):
		# with open("example_answers.json", encoding="utf-8") as f:
		# 	content = f.read()
		print("ANSWER REQUEST")
		db.insertQuery(query)
		request = requests.get(f'https://api.stackexchange.com/2.3/questions/{query}/answers?order=desc&sort=activity&site=stackoverflow&filter=withbody&key={key}')
		parse_json = json.loads(request.text)
		print(f"Remaining API Quota: {parse_json['quota_remaining']}")
		for question in parse_json['items']:
			db.insertAnswer(question['answer_id'], question['question_id'], question['body'], question['score'], question['is_accepted'])

	rows = db.queryAnswers(query)
	if rows is None:
		return None
	relevent = ""
	score = None
	answers = []
	for row in rows:
		answers.append({'id': row[0], 'question': row[1], 'body': row[2], 'score': row[3], 'accepted': row[4]})
	for a in answers:
		if score is None or a['score'] > score:
			relevent = a['body']
			score = a['score']
	
	return relevent if score is not None else None
#__queryAnswers
	
#queryStack



