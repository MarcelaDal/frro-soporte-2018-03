import pymysql

conector = pymysql.connect(host='localhost', user='root', password='')
cursor = conector.cursor()
sql = 'CREATE DATABASE IF NOT EXISTS tp3;'
cursor.execute(sql)
conector = pymysql.connect(host='localhost',db='tp3', user='root', password='')
cursor = conector.cursor()
sql = 'CREATE TABLE Persona(idPersona integer PRIMARY KEY,nombre char(30),fecha_nacimiento Date,dni char(13),altura integer);'
cursor.execute(sql)
sql = 'SELECT * FROM Persona'
cursor.execute(sql)
select = cursor.fetchall()
print(select)




