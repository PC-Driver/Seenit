import sqlite3 as sql

conn = sql.connect('seenit.db')
c = conn.cursor()

def insert(id, name, email):
    query = "INSERT INTO user (u_id, u_name, email) VALUES (" + str(id) + ",'" + name + "','" + email + "')"
    print (query)
    with conn: 
        c.execute(query)

# admin
def delete(id):
    query = "DELETE FROM user WHERE u_id=" + str(id)
    print (query)
    with conn: 
        c.execute(query)


