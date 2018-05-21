import pymysql
import datetime

conn= pymysql.connect(host="localhost", port=3306, db="tp3", user="root", password="")

cur= conn.cursor()

query = "SELECT * FROM persona where dni = 15437424"

cur.execute(query)
resultado = cur.fetchone()

assert resultado == (0, 'Juan', datetime.date(2018, 5, 17), '15437424', 2)
