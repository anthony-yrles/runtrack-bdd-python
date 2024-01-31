import mysql.connector

mydb = mysql.connector.connect(
    host="LocalHost",
    user="root",
    password="SKenan30mg/",
    database="zoo",
)

class Directeur:
    def __init__(self, db):
        self.__db = db
    
    def get_db(self):
        return self.__db
    def set_db(self, db):
        self.__db = db

    def add_animals(self, nom, race, id_cage, anniversaire, provenance):
        cursor = mydb.cursor()
        query = f"INSERT INTO animal (nom, race, id_cage, anniversaire, provenance) VALUES ('{nom}', '{race}', {id_cage}, '{anniversaire}', '{provenance}')"
        cursor.execute(query)
        self.__db.commit()
        results = cursor.fetchall()
        cursor.close()
        return results
    
    def add_cages(self, capacite, superficie):
        cursor = mydb.cursor()
        query = f"INSERT INTO cage (capacite, superficie) VALUES ({capacite}, {superficie})"
        cursor.execute(query)
        self.__db.commit()
        results = cursor.fetchall()
        cursor.close()
        return results
    
    def update_animals(self, valeur, new_valeur, condition):
        cursor = mydb.cursor()

        # Vérifie si la nouvelle valeur est une chaîne
        if isinstance(new_valeur, str):
            formatted_value = f"'{new_valeur}'"
        else:
            formatted_value = str(new_valeur)

        command_to_update = f"""
        UPDATE animal
        SET {valeur} = {formatted_value}
        WHERE {condition}
        """

        cursor.execute(command_to_update)
        results = cursor.fetchall()
        self.__db.commit()
        cursor.close()
        return results
    
    def update_cages(self, valeur, new_valeur, condition):
        cursor = mydb.cursor()
        command_to_update = f"""
        UPDATE cage
        SET {valeur} = '{new_valeur}'
        WHERE {condition}
        """
        cursor.execute(command_to_update)
        results = cursor.fetchall()
        self.__db.commit()
        cursor.close()
        return results
    
    def delete_animals(self, condition):
        cursor = mydb.cursor()
        command_to_delete = f"""
        DELETE FROM animal
        WHERE {condition}
        """
        cursor.execute(command_to_delete)
        results = cursor.fetchall()
        self.__db.commit()
        cursor.close()
        return results
    
    def delete_cage(self, condition):
        cursor = mydb.cursor()
        command_to_delete = f"""
        DELETE FROM cage
        WHERE {condition}
        """
        cursor.execute(command_to_delete)
        results = cursor.fetchall()
        self.__db.commit()
        cursor.close()
        return results
    
    def read_all_animals(self, valeur):
        cursor = mydb.cursor()
        query = f"SELECT {valeur} FROM animal"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results
    
    def read_from_cage(self, valeur):
        cursor = mydb.cursor()
        query = f"""
                SELECT {valeur}
                FROM animal 
                INNER JOIN cage ON animal.id_cage = cage.id
                """
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results
    
    def total_superficie(self):
        cursor = mydb.cursor()
        query = "SELECT SUM(superficie) FROM cage"
        cursor.execute(query)
        result = cursor.fetchone()[0]
        cursor.close()
        return result

    
directeur = Directeur(mydb)

directeur.add_animals('Léo', 'Lion', 1, '2022-01-30', 'Savane')
directeur.add_animals('Emma', 'Éléphant', 1, '2022-01-31', 'Forêt tropicale')
directeur.add_animals('Max', 'Tigre', 1, '2022-02-01', 'Jungle')
directeur.add_animals('Mia', 'Girafe', 1, '2022-02-02', 'Savane')
directeur.add_animals('Oscar', 'Singe', 1, '2022-02-03', 'Forêt tropicale')

directeur.add_animals('Zoé', 'Zèbre', 2, '2022-02-04', 'Savane')
directeur.add_animals('Charlie', 'Chimpanzé', 2, '2022-02-05', 'Forêt tropicale')
directeur.add_animals('Lola', 'Léopard', 2, '2022-02-06', 'Jungle')
directeur.add_animals('Lucas', 'Loup', 2, '2022-02-07', 'Forêt')
directeur.add_animals('Chloé', 'Chouette', 2, '2022-02-08', 'Forêt')

directeur.add_animals('Milo', 'Morse', 3, '2022-02-09', 'Océan Arctique')
directeur.add_animals('Zara', 'Zèbre', 3, '2022-02-10', 'Savane')
directeur.add_animals('Nina', 'Narval', 3, '2022-02-11', 'Océan Arctique')
directeur.add_animals('Leo', 'Lémurien', 3, '2022-02-12', 'Forêt tropicale')
directeur.add_animals('Bella', 'Bison', 3, '2022-02-13', 'Prairie')

directeur.add_cages(5, 100)
directeur.add_cages(5, 80)
directeur.add_cages(5, 120)
directeur.add_cages(5, 60)

directeur.update_animals('race', 'Lion Royal', 'id = 1')
directeur.update_animals('provenance', 'Savane Africaine', 'id = 6')
directeur.update_animals('anniversaire', '2022-02-15', 'id = 11')

directeur.update_animals('id_cage', 4, 'nom = "Bella"')

directeur.update_cages('capacite', 3, 'id = 1')
directeur.update_cages('superficie', 110, 'id = 2')

directeur.delete_animals('id_cage = 6 AND nom = "Animal6"')

directeur.delete_cage('id = 6')

animals = directeur.read_all_animals('*')
print(animals)
animals_cages = directeur.read_from_cage('*')
print(animals_cages)

result = directeur.total_superficie()
print(result)