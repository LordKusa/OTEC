from psycopg2 import pool
import sys

class Conexion:

    _database = 'test_db'
    _username = 'postgres'
    _password = 'admin'
    _host = '127.0.0.1'
    _port = '5432'
    _min_con = 1
    _max_con = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._min_con,
                    cls._max_con,
                    host = cls._host,
                    user = cls._username,
                    password = cls._password,
                    port = cls._port,
                    database = cls._database
                )
            except Exception as e:
                print('no se pudo obtener el pool')
                sys.exit

        return cls._pool

    @classmethod
    def obtenerConexion(cls):
        return cls.obtenerPool().getconn()

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()

if __name__ == "__main__":
    conexion1 = Conexion.obtenerConexion()  
    Conexion.liberarConexion(conexion1)
    conexion1 = Conexion.obtenerConexion()