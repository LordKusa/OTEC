from cursor_del_pool import CursorDelPool

class ClaeDAO:

    _seleccionar = 'SELECT * FROM clae ORDER BY actividad ASC'
    _insertar = 'INSERT INTO clae(id_clae, actividad) VALUES(%s, %s)'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._seleccionar)
            registros = cursor.fetchall()
            lista_clae = []
            for registro in registros:
                lista_clae.append(registro)
            return lista_clae

    @classmethod
    def insertar(cls, clae):
        with CursorDelPool() as cursor:
            valores = []
            for clave in clae:
                valores.append(clae[clave])
            valores = tuple(valores)
            cursor.execute(cls._insertar, valores)

if __name__ == '__main__':
    lista_clae = ClaeDAO.seleccionar()