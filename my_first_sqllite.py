import sqlite3


conn = sqlite3.connect("lite.db")  # Connect to database
cur = conn.cursor()  # create a cursor object
cur.execute("DROP TABLE IF EXISTS store")

def create():
    conn = sqlite3.connect("lite.db")  # Connect to database
    cur = conn.cursor()  # create a cursor object
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INT, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    #global conn, cur
    conn = sqlite3.connect("lite.db")  # Connect to database
    cur = conn.cursor()  # create a cursor object
    cur.execute("INSERT into store VALUES(?,?,?)", (str(item),int(quantity), float(price)))
    conn.commit()
    conn.close()




def select():
    conn = sqlite3.connect("lite.db")  # Connect to database
    cur = conn.cursor()  # create a cursor object
    query =cur.execute("SELECT * FROM store")
    results= query.fetchall()
    conn.close()
    return results

def delete(item):
    conn = sqlite3.connect("lite.db")  # Connect to database
    cur = conn.cursor()  # create a cursor object
    cur.execute("DELETE FROM store WHERE item =?",(item,))
    conn.commit()
    conn.close()


#delete('glass')

def update(item, quantity, price):
    conn = sqlite3.connect("lite.db")  # Connect to database
    cur = conn.cursor()  # create a cursor object
    cur.execute("UPDATE store SET quantity = ?, price = ? WHERE item =?",(quantity, price,item))
    conn.commit()
    conn.close()

create()
insert('glass',6,90.6)
insert('book',9,56.9)
update('glass',30, 34.89)
a= select()
print(a)
#UPDATE store set quantity= ? ,"
    #            " price =? WHERE item = ?", (item, quantity,price)