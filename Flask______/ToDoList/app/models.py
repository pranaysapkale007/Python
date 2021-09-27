import sqlite3

conn = sqlite3.connect('todo.db')

query = "<sqlite quey>"

result = conn.execute(query)