import sqlite3

def init():
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
				isAccepter INTEGER,
				FOREIGN KEY question REFERENCES question(id)
				)
				''')



