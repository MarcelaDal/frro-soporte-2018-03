import pymysql
import datetime

conector = pymysql.connect(host='localhost', db='tp3', user='root', password='')
cursor = conector.cursor()

sql = 'delete from Persona where idPersona=1'

cursor.execute(sql)
cursor.execute('SELECT * FROM Persona')
select = cursor.fetchall()
conector.commit()
conector.close()

assert  select == ((0, 'Juan', datetime.date(2018, 5, 17), '15437424', 2),)
