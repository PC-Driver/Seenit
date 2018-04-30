import sqlite3 as sql

conn = sql.connect('seenit.db')
c = conn.cursor()

def insert(id, category, creater_id):
    query = "INSERT INTO seenit (s_id, category, creater_id) VALUES (" + str(id) + ",'" + category + "','" + str(creater_id) + "')"
    # print (query)
    with conn:
        try:
            c.execute(query)
            print ("insert successfully")
            conn.commit()
        except:
            conn.rollback()
            print ("insert error")

def read_one(id):
    query = "SELECT * FROM seenit WHERE s_id=" + str(id)
    with conn: 
        try:
            c.execute(query)
            items = c.fetchall()
            item = items[0]
            print ("read successfully")
            return item 
        except:
            print("read error")        

def delete(id):
    query = "DELETE FROM seenit WHERE s_id=" + str(id)
    # print (query)
    with conn:
        try:
            c.execute(query)
            print ("delete successfully")
            conn.commit()
        except:
            conn.rollback()
            print ("delete error")

def read_all():
    with conn:
        try:
            c.execute('SELECT * FROM seenit')
            items = c.fetchall()
            print ("read successfully")
            return items
        except:
            print("read error") 

def update(id, category):
    query = "UPDATE seenit SET category='" + category + "' WHERE u_id=" + str(id)
    # print (query)
    with conn:
        try:
            c.execute(query)
            print ("update successfully")
            conn.commit()
        except:
            conn.rollback()
            print ("update error")






