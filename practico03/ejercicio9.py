import pymysql
import datetime


conector = pymysql.connect(host='localhost', db='tp3', user='root', password='')
cursor = conector.cursor()

sql= "select * from Persona p left join PersonaPeso pp on p.idPersona = pp.idPersona where p.DNI=%s"
cursor.execute(sql, 39951593)
select = cursor.fetchall()
columnas = [columna[0] for columna in cursor.description]
for fila in select:
    print(dict(zip(columnas, fila)))
conector.commit()
conector.close()