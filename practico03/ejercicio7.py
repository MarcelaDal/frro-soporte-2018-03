import pymysql

conector = pymysql.connect(host='localhost', db='tp3', user='root', password='')
cursor = conector.cursor()

sql="CREATE TABLE IF NOT EXISTS PersonaPeso(idPersona integer," \
    " Fecha date, Peso integer, FOREIGN KEY (idPersona) REFERENCES Persona(idPersona));"
cursor.execute(sql)
conector.commit()
sql = 'SELECT * FROM PersonaPeso'
cursor.execute(sql)
select = cursor.fetchall();
conector.close()

assert select == ()
