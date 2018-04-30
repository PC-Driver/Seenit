import sqlite3 as sql

conn = sql.connect('seenit.db')
c = conn.cursor()

# register-insert new user
def insert(id, name, email):
    query = "INSERT INTO user (u_id, u_name, email) VALUES (" + str(id) + ",'" + name + "','" + email + "')"
    print (query)
    with conn: 
        c.execute(query)

# login-get user id with name input
def show_user(name):
    query = "SELECT u_id FROM user WHERE u_name='" + name + "'"
    with conn: 
        c.execute(query)
        users = c.fetchall()
        _id = users[0][0]
        return _id         

# admin delete account
def delete(id):
    query = "DELETE FROM user WHERE u_id=" + str(id)
    print (query)
    with conn: 
        c.execute(query)
# get all users
def show_users():
    with conn:
        c.execute('SELECT * FROM user')
        users = c.fetchall()
        return users
# update account info
def update(id, name, email):
    query = "UPDATE user SET u_name='" + name + "', email='" + email + "' WHERE u_id=" + str(id)
    # query = "INSERT INTO user (u_id, u_name, email) VALUES (" + str(id) + ",'" + name + "','" + email + "')"
    print (query)
    with conn: 
        c.execute(query)





