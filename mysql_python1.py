import mysql.connector as my


def create_table():
            conn = my.connect(database = 'bookinfo' ,user ='root',  password = '1234',  host = 'localhost' , port= 3306 )
            cur = conn.cursor()
            cur.execute("CREATE TABLE  test  (id INT , f_name TEXT, lname TEXT)")
            conn.commit()
            conn.close()


create_table()



