import pymysql
import datetime

from builtins import print

conn = pymysql.connect(host="localhost", port=3306, db="tp3", user="root", password="")

cur = conn.cursor()
inputId = input("Ingrese el id de la persona: ")
query = "SELECT p.idPersona, max(pp.fecha), p.nombre FROM persona p LEFT JOIN personapeso pp on p.idPersona = pp.idPersona WHERE p.idPersona = %s"
cur.execute(query, [inputId])
result = cur.fetchone()
dateToday = datetime.date.today().strftime('%Y-%m-%d %H:%M:%S')

if result:
    if result[1] == None or str(result[1]) >= str(dateToday):
        inputPeso = int(input("Ingrese el peso para "+result[2]+" : "))
        query2 = "INSERT INTO personapeso values (%s, %s, %s)"
        cur.execute(query2, [result[0], dateToday, inputPeso])
        conn.commit()
        print("Registro agregado exitosamente.")
    else:
        print("Ya existe un registro para el peso de "+result[2]+" que es menor o igual a la fecha especificada.")
else:
    print("No existe ninguna persona con id "+inputId)

query3 = "SELECT * FROM personapeso"
cur.execute(query3)
result = cur.fetchall()

print(result)

assert result == ((0, datetime.date(2018, 5, 17), 80),)

