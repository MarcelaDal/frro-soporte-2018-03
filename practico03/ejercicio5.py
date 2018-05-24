import pymysql
import datetime


conector = pymysql.connect(host='localhost', db='tp3', user='root', password='')
cursor = conector.cursor()

date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
sql = 'UPDATE Persona SET nombre=%s, fecha_nacimiento=%s, dni=%s , altura=%s WHERE idPersona=0'

cursor.execute(sql, ["Juan Mannuel", date, '12345678', 175])
cursor.execute('SELECT * FROM Persona')
select = cursor.fetchall()

conector.commit()
conector.close()
print(select)
assert select == ((0, 'Juan Mannuel', datetime.date(2018, 5, 17), '12345678', 175),)
