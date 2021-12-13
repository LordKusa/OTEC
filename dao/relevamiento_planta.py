from cursor_del_pool import CursorDelPool

class RelevamientoPlantaDAO:
    _seleccionar = 'SELECT * FROM relevamiento_planta'
    _insertar = 'INSERT INTO relevamiento_planta(id_planta, fecha, potencia_consumida, uso_capacidad, personal_total, personal_produccion, personal_administrativo, personal_otros) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._seleccionar)
            registros = cursor.fetchall()
            relevamientos = []
            for registro in registros:
                relevamiento = []
                for i in range(9):
                    relevamiento.append(registro[i])
                relevamientos.append(relevamiento)
            return relevamientos

    @classmethod
    def insertar(cls, relevamiento):
        with CursorDelPool() as cursor:
            valores = (
                relevamiento['id_planta'], 
                relevamiento['fecha'], 
                relevamiento['potencia_consumida'], 
                relevamiento['uso_capacidad'], 
                relevamiento['personal_total'], 
                relevamiento['personal_produccion'], 
                relevamiento['personal_administrativo'], 
                relevamiento['personal_otros']
            )
            cursor.execute(cls._insertar, valores)