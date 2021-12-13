from conexion import Conexion

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipoExcepcion, valorExcepcion, detalleExcepcion):
        if valorExcepcion:
            self._conexion.rollback()
            print(f'Ocurrió una excepción: {valorExcepcion} {tipoExcepcion} {detalleExcepcion}')
        else:
            self._conexion.commit()
        
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)