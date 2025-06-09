import sqlite3

class ConexionBD:
    def __init__(self):
        self.baseDatos = 'database/DBHistorial.db'
        self.conexion = sqlite3.connect(self.baseDatos)
        self.cursor = self.conexion.cursor()

    def cerrarConexion(self):
        self.conexion.commit()
        self.conexion.close()