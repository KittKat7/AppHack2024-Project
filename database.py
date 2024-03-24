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
				answered INTEGER
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
				CREATE TABLE IF NOT EXISTS answer
				(
				id INTEGER PRIMARY KEY,
				question INTEGER,
				body TEXT,
				score INTEGER,
				accepted INTEGER,
				FOREIGN KEY(question) REFERENCES question(id)
				)
				''')
	cursor.execute('''
				CREATE TABLE IF NOT EXISTS definition
				(
				term TEXT PRIMARY KEY,
				definition TEXT
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
		cursor.execute("INSERT OR IGNORE INTO tag (tag) VALUES (?)", (tag))
		cursor.execute("INSERT OR IGNORE INTO hasTag (question, tag) VALUES (?, ?)", (id, tag))
	connection.commit()
#insertQuestion

def insertAnswer(id: int, question: int, body: str, score: int, accepted: bool):
	global connection
	global cursor
	accepted: bool = 1 if accepted else 0
	cursor.execute("INSERT OR IGNORE INTO answer (id, question, body, score, accepted) VALUES (?, ?, ?, ?, ?)", (id, question, body, score, accepted))
	connection.commit()
#insertAnswer

def queryQuestions(q: str):
	global connection
	global cursor
	rows: list = []
	for key in q:
		cursor.execute("""
		SELECT *
		FROM question
		WHERE title LIKE '%' || ? || '%'
		""", (key,))
		nrows = cursor.fetchall()
		for r in nrows:
			rows.append(r)
	return rows if len(rows) > 0 else None
#queryQuestions

def queryDefinition(word: str) -> str:
	global connection
	global cursor
	cursor.execute("""SELECT * FROM definition WHERE term = ?""", (word,))
	rows = cursor.fetchall()
	connection.commit()
	return rows[0] if len(rows) > 0 else None
#queryDefinition

def insertDefinition(word: str, definition: str):
	global connection
	global cursor
	cursor.execute("INSERT OR IGNORE INTO definition (term, definition) VALUES (?, ?)", (word, definition,))
	connection.commit()
#insertDefintion