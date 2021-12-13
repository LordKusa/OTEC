from cursor_del_pool import CursorDelPool

class ClaeDAO:

    _seleccionar = 'SELECT * FROM clae ORDER BY actividad ASC'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._seleccionar)
            registros = cursor.fetchall()
            lista_clae = []
            for registro in registros:
                lista_clae.append(registro)
            return lista_clae

if __name__ == '__main__':
    lista_clae = ClaeDAO.seleccionar()