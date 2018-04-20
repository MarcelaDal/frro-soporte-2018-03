import pymysql
import datetime


conector = pymysql.connect(host='localhost', db='tp3', user='root', password='')
cursor = conector.cursor()

date = datetime.datetime.today().strftime('%y-%m-%d %H:%M:%S')
sql = 'UPDATE Persona SET nombre=%s, fecha_nacimiento=%s, dni=%s , altura=%s WHERE idPersona=3'

cursor.execute(sql, ["Marcela", date, 38770609,175])
cursor.execute('SELECT * FROM Persona')
select = cursor.fetchall()
columnas = [columna[0] for columna in cursor.description]
for fila in select:
    print(dict(zip(columnas, fila)))
conector.commit()
conector.close()