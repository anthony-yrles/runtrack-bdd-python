import mysql.connector

mydb = mysql.connector.connect(
    host="LocalHost",
    user="root",
    password="SKenan30mg/",
    database="laplateforme",
)

cursor = mydb.cursor()
cursor.execute("SELECT * FROM etudiant")
results = cursor.fetchall()
print(results)

cursor.close()
mydb.close()