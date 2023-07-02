
from psycopg2 import pool
import psycopg2 as bd
import sys

class Conexion:
    _DATABASE = 'usuarios'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtener_conexion(cls):
        try:
            conexion = bd.connect(host=cls._HOST,
                                  user=cls._USERNAME,
                                  password=cls._PASSWORD,
                                  port=cls._DB_PORT,
                                  database=cls._DATABASE)

            return conexion
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")
            sys.exit()

    @classmethod
    def obtener_cursor(cls, conexion):
        return conexion.cursor()

    @classmethod
    def obtener_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,
                                                      cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE)

                return cls._pool
            except Exception as e:
                print(f"Ha ocurrido un error: {e}")

                sys.exit()
        else:
            return cls._pool

if __name__ == '__main__':
    conexion1 = Conexion.obtener_conexion()
    conexion2 = Conexion.obtener_conexion()
    conexion3 = Conexion.obtener_conexion()
    conexion4 = Conexion.obtener_conexion()
    conexion5 = Conexion.obtener_conexion()
