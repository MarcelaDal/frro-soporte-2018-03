import pymysql
import datetime


conn= pymysql.connect(host="localhost", port=3306, db="tp3", user="root", password="")

cur= conn.cursor()

print('Antes de ejecutar la consulta:')
cur.execute("SELECT * FROM persona")
result= cur.fetchall()

date = datetime.datetime.today()
d = date.strftime('%Y-%m-%d %H:%M:%S')
query = "INSERT into persona values (%s,%s,%s,%s,%s)"
cur.execute(query, [0 ,"Juan", d, 15437424, 1.8])
cur.execute(query, [1 ,"Maria", d, 12345678, 1.6])
conn.commit()

print('Luego de ejecutar la consulta:')
cur.execute("SELECT * FROM persona")
result1 = cur.fetchall()

assert result1 == ((0, 'Juan', datetime.date(2018, 5, 17), '15437424', 2), (1, 'Maria', datetime.date(2018, 5, 17), '12345678', 2))

