import mysql.connector

mydb = mysql.connector.connect(
    host="LocalHost",
    user="root",
    password="SKenan30mg/",
    database="entreprise",
)

cursor = mydb.cursor()
# cursor.execute("SELECT * FROM employe WHERE salaire > 3000")
# results = cursor.fetchall()
# cursor.close()

# print(results)

# cursor = mydb.cursor()
# cursor.execute("SELECT * FROM employe INNER JOIN service ON employe.id_service = service.id")
# results = cursor.fetchall()
# cursor.close()

# print(results)


# mydb.close()

class Employe:
    def __init__(self, db):
        self.__db = db
    
    def get_db(self):
        return self.__db
    def set_db(self, db):
        self.__db = db

    def create_row(self, nom, prenom, salaire, id_service):
        cursor = mydb.cursor()
        query = f"INSERT INTO employe (nom, prenom, salaire, id_service) VALUES ('{nom}', '{prenom}', {salaire}, {id_service})"
        cursor.execute(query)
        self.__db.commit()
        results = cursor.fetchall()
        cursor.close()
        return results
    
    def read(self, valeur):
        cursor = mydb.cursor()
        query = f"SELECT {valeur} FROM employe"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results
    
    def update(self, valeur, new_valeur, condition):
        cursor = mydb.cursor()
        command_to_update = f"""
        UPDATE employe
        SET {valeur} = {new_valeur}
        WHERE {condition}
        """
        cursor.execute(command_to_update)
        results = cursor.fetchall()
        self.__db.commit()
        cursor.close()
        return results
    
    def delete(self, condition):
        cursor = mydb.cursor()
        command_to_delete = f"""
        DELETE FROM employe
        WHERE {condition}
        """
        cursor.execute(command_to_delete)
        results = cursor.fetchall()
        self.__db.commit()
        cursor.close()
        return results

employes = Employe(mydb)
results = employes.create_row('Vanni', 'Barbara', 1000000, 2)
read = employes.read('*')
print(read)
update = employes.update('salaire', 10, 'nom = "Vanni"')
read = employes.read('*')
print(read)
delete = employes.delete('nom = "Vanni"')
read = employes.read('*')
print(read)


