import sqlite3 as sql

conn = sql.connect('seenit.db')
c = conn.cursor()

def insert(id, category, creater_id):
    query = "INSERT INTO seenit (s_id, category, creater_id) VALUES (" + str(id) + ",'" + category + "','" + str(creater_id) + "')"
    # print (query)
    with conn:
        try:
            c.execute(query)
            print ("seenit insert successfully")
            conn.commit()
        except:
            conn.rollback()
            print ("seenit insert error")

def read_one(id):
    query = "SELECT * FROM seenit WHERE s_id=" + str(id)
    with conn: 
        try:
            c.execute(query)
            items = c.fetchall()
            item = items[0]
            print ("seenit read successfully")
            return item 
        except:
            print("seenit read error")        

def delete(id):
    query = "DELETE FROM seenit WHERE s_id=" + str(id)
    # print (query)
    with conn:
        try:
            c.execute(query)
            print ("seenit delete successfully")
            conn.commit()
        except:
            conn.rollback()
            print ("seenit delete error")

def read_all():
    with conn:
        try:
            c.execute('SELECT * FROM seenit')
            items = c.fetchall()
            print ("seenit read successfully")
            return items
        except:
            print("seenit read error") 

def update(id, category):
    query = "UPDATE seenit SET category='" + category + "' WHERE s_id=" + str(id)
    # print (query)
    with conn:
        try:
            c.execute(query)
            print ("seenit update successfully")
            conn.commit()
        except:
            conn.rollback()
            print ("seenit update error")

# update(6,'testtest')




