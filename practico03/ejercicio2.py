import pymysql
import datetime


conn= pymysql.connect(host="localhost", port=3306, db="tp3", user="root", password="")

cur= conn.cursor()

print('Antes de ejecutar la consulta:')
cur.execute("SELECT * FROM personas")
result= cur.fetchall()
columns = [column[0] for column in cur.description]
for row in result:
    print(dict(zip(columns, row)))

date = datetime.datetime.today()
d= date.strftime('%Y-%m-%d %H:%M:%S')
query = "INSERT into personas values (%s,%s,%s,%s,%s)"

cur.execute(query, [0 ,"Juan", d , 15437424, 1])
conn.commit()

print('Luego de ejecutar la consulta:')
cur.execute("SELECT * FROM personas")
result= cur.fetchall()
columns = [column[0] for column in cur.description]
for row in result:
    print(dict(zip(columns, row)))

