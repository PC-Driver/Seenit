import sqlite3 as sql

conn = sql.connect('seenit.db')
c = conn.cursor()

# register-insert new user
def insert(id, name, email):
    query = "INSERT INTO user (u_id, u_name, email) VALUES (" + str(id) + ",'" + name + "','" + email + "')"
    # print (query)
    with conn:
        try:
            c.execute(query)
            print ("insert successfully")
            conn.commit()
        except:
            conn.rollback()
            print ("insert error")

# login-get user id with name input
def read_one(name):
    query = "SELECT u_id FROM user WHERE u_name='" + name + "'"
    with conn: 
        try:
            c.execute(query)
            users = c.fetchall()
            _id = users[0][0]
            print ("read successfully")
            return _id 
        except:
            print("read error")        

# admin delete account
def delete(id):
    query = "DELETE FROM user WHERE u_id=" + str(id)
    # print (query)
    with conn:
        try:
            c.execute(query)
            print ("delete successfully")
            conn.commit()
        except:
            conn.rollback()
            print ("delete error")

# get all users
def read_all():
    with conn:
        try:
            c.execute('SELECT * FROM user')
            users = c.fetchall()
            print ("read successfully")
            return users
        except:
            print("read error") 

# update account info
def update(id, name, email):
    query = "UPDATE user SET u_name='" + name + "', email='" + email + "' WHERE u_id=" + str(id)
    print (query)
    with conn:
        try:
            c.execute(query)
            print ("update successfully")
            conn.commit()
        except:
            conn.rollback()
            print ("update error")

# insert(7,'b','b@email')



