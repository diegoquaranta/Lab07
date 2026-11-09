from idlelib import query

from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO
    def get_dati_generi(self):
        cnx = DBConnect.get_connection()

        result = []

        query = """SELECT DISTINCT genere
                   FROM libro"""

        cursor = cnx.cursor()
        cursor.execute(query)

        for genere in cursor:
            result.append(genere[0])

        cursor.close()
        cnx.close()

        return result

    def get_dati_libri_filtrati(self, biblioteca, genere):
        cnx = DBConnect.get_connection()

        result = []

        if biblioteca is None or biblioteca == "nessuno":
            biblioteca = None

        if genere is None or genere == "nessuno":
            genere = None

        query= """SELECT *
                  FROM libro
                  WHERE id_biblioteca = COALESCE(%s, id_biblioteca)
                  AND genere = COALESCE(%s, genere)"""

        cursor = cnx.cursor()
        cursor.execute(query,(biblioteca, genere))

        for libro in cursor:
            result.append(Libro(*libro))

        cursor.close()
        cnx.close()

        return result
