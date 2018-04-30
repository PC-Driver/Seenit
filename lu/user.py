import sqlite3 as sql

conn = sql.connect('seenit.db')
c = conn.cursor()

def insert(value):
    query = 'INSERT INTO user (u_id, u_name, email) VALUES {}'.format(value)
    with conn: 
        c.execute(query)
