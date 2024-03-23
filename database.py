import sqlite3

cursor: sqlite3.Cursor
connection: sqlite3.Connection

def initdb():
	global connection
	global cursor
	connection = sqlite3.connect('NebulaOffline.db')
	cursor = connection.cursor()
	cursor.execute('''
				CREATE TABLE IF NOT EXISTS question
				(
				id INTEGER PRIMARY KEY,
				title TEXT,
				link TEXT,
				score INTEGER,
				isAnswered INTEGER
				)
				''')
	cursor.execute('''
				CREATE TABLE IF NOT EXISTS tag
				(
				tag TEXT PRIMARY KEY
				)
				''')
	cursor.execute('''
				CREATE TABLE IF NOT EXISTS hasTag
				(
				question INTEGER,
				tag TEXT,
				PRIMARY KEY (question, tag),
				FOREIGN KEY(question) REFERENCES question(id),
				FOREIGN KEY(tag) REFERENCES tag(tag)
				)
				''')
	cursor.execute('''
				CREATE TABLE IF NOT EXIST answer
				(
				id INTEGER PRIMARY KEY,
				question INTEGER,
				body TEXT,
				score INTEGER,
				isAccepted INTEGER,
				FOREIGN KEY question REFERENCES question(id)
				)
				''')
	connection.commit()
#initdb

def insertQuestion(id: int, title: str, link: str, score: int, answered: bool, tags: list[str]):
	global connection
	global cursor
	answered: bool = 1 if answered else 0
	cursor.execute("INSERT OR IGNORE INTO question (id, title, link, score, answered) VALUES (?, ?, ?, ?, ?)", (id, title, link, score, answered))
	for tag in tags:
		cursor.execute("INSERT OR IGNORE tag (tag) VALUES (?)", (tag))
		cursor.execute("INSERT OR IGNORE hasTag (question, tag) VALUES (?, ?)", (id, tag))
	connection.commit()
#insertQuestion

def insertAnswer(id: int, question: int, body: str, score: int, accepted: bool):
	global connection
	global cursor
	accepted: bool = 1 if accepted else 0
	cursor.execute("INSERT OR IGNORE INTO answer (id, question, body, score, isAccepted) VALUES (?, ?, ?, ?, ?)", (id, question, body, score, accepted))
	connection.commit()
#insertAnswer


