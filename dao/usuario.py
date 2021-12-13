from cursor_del_pool import CursorDelPool

class UsuarioDAO:
    _seleccionar = 'SELECT * FROM  usuarios where usuario = %s'

    @classmethod
    def seleccionar(cls, usuario):
        dic = None
        with CursorDelPool() as cursor:
            cursor.execute(cls._seleccionar, (usuario,))
            tupla = cursor.fetchone()
            if cursor.rowcount != 0:
                dic = {
                    'usuario' : tupla[1],
                    'clave' : tupla[2]
                }
        return dic
