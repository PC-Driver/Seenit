import sqlite3 as sql

conn = sql.connect('seenit.db')
c = conn.cursor()

# register
# def insert(id, name, email):
#     query = "INSERT INTO user (u_id, u_name, email) VALUES (" + str(id) + ",'" + name + "','" + email + "')"
#     print (query)
#     with conn: 
#         c.execute(query)
# login
# def show_user(name, email):
#     query = "SELECT *"

# # admin
# def delete(id):
#     query = "DELETE FROM user WHERE u_id=" + str(id)
#     print (query)
#     with conn: 
#         c.execute(query)

def show_seenits():
    with conn:
        c.execute('SELECT * FROM seenit')
        seenits = c.fetchall()
        return seenits

# def update(id, name, email):
#     query = "UPDATE user SET u_name='" + name + "', email='" + email + "' WHERE u_id=" + str(id)
#     # query = "INSERT INTO user (u_id, u_name, email) VALUES (" + str(id) + ",'" + name + "','" + email + "')"
#     print (query)
#     with conn: 
#         c.execute(query)




