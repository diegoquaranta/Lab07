from database import DB_connect
from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO
    def get_dati_biblioteche(self):
        cnx = DBConnect.get_connection()
        result= []

        query = """SELECT *
                   FROM biblioteca"""

        cursor = cnx.cursor()

        cursor.execute(query)

        for biblioteca in cursor:
            result.append(Biblioteca(*biblioteca))

        cursor.close()
        cnx.close()
        return result


