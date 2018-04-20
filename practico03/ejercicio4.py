import pymysql

conn= pymysql.connect(host="localhost", port=3306, db="tp3", user="root", password="")

cur= conn.cursor()

query = "SELECT * FROM personas where dni = 38770609"

cur.execute(query)
resultado = cur.fetchone()

print(resultado)
