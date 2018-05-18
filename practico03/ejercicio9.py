import pymysql
import datetime


conector = pymysql.connect(host='localhost', db='tp3', user='root', password='')
cursor = conector.cursor()

sql= "select * from Persona p left join PersonaPeso pp on p.idPersona = pp.idPersona where p.DNI=%s"
cursor.execute(sql, 12345678)
select = cursor.fetchall()
conector.commit()
conector.close()

assert select == ((0, 'Juan Mannuel', datetime.date(2018, 5, 17), '12345678', 175, 0, datetime.date(2018, 5, 17), 80),)
