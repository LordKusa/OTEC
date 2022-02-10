from cursor_del_pool import CursorDelPool

class EmpresaDAO:
    _atributos = ['id_empresa', 'cuit', 'nombre_legal', 'nombre_fantasia', 
                  'tipo_societario', 'pagina_web', 'rubro', 'actividad_primaria', 
                  'actividad_secundaria_uno', 'actividad_secundaria_dos', 'actividad_secundaria_tres', 'mipyme_local', 
                  'categoria_pyme', 'habilitacion_municipal']
    _seleccionar = 'SELECT * FROM empresa ORDER BY id_empresa'
    _seleccionar_uno = 'SELECT * FROM empresa WHERE'
    _insertar = 'INSERT INTO empresa(cuit, nombre_legal, nombre_fantasia, tipo_societario, pagina_web, rubro, actividad_primaria, actividad_secundaria, mipyme_local, categoria_pyme, habilitacion_municipal) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    _dashboard = 'SELECT tipo_societario, pagina_web, rubro, mipyme_local, categoria_pyme, habilitacion_municipal FROM empresa'
    _actualizar = 'UPDATE empresa SET'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._seleccionar)
            registros = cursor.fetchall()
            empresas = []
            for registro in registros:
                empresa = []
                for i in range(22):
                    empresa.append(registro[i])
                empresas.append(empresa)
            return empresas

    @classmethod
    def seleccionar_uno(cls, valores):
        with CursorDelPool() as cursor:
            query = f'{cls._seleccionar_uno} {valores[0]} = \'{valores[1]}%\' ORDER BY id_empresa'
            cursor.execute(query)
            registros = cursor.fetchall()
            if cursor.rowcount != 1:
                empresas = []
                for registro in registros:
                    empresa = []
                    for i in range(22):
                        empresa.append(registro[i])
                    empresas.append(empresa)
            else:
                empresas = list(registros)
            return empresas

    @classmethod
    def dashboard(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._dashboard)
            registros = cursor.fetchall()
            empresas = []
            for registro in registros:
                empresa = []
                for i in range(6):
                    empresa.append(registro[i])
                empresas.append(empresa)
            return empresas

    @classmethod
    def insertar(cls, empresa):
        with CursorDelPool() as cursor:
            if type(empresa) == dict:
                valores = []
                for clave in empresa:
                    valores.append(empresa[clave])
            elif type(empresa) == list:
                valores = empresa
            valores = tuple(valores)
            cursor.execute(cls._insertar, valores)

    @classmethod
    def actualizar(cls, empresa):
        with CursorDelPool() as cursor:
            valores = []
            
            query = f'{cls._actualizar}'
            for clave in empresa:
                print(clave)
                if clave == 'actividad_primaria' or clave == 'actividad_secundaria_uno' or clave == 'actividad_secundaria_dos' or clave == 'actividad_secundaria_tres':
                    empresa[clave] = empresa[clave][0:6]
                valores.append(empresa[clave])

            for i in range(1, 14):
                
                query = f"{query} {cls._atributos[i]} = '{valores[i]}'"
                if not(i == 13):
                    query = f'{query},'

            query = f'{query} WHERE {cls._atributos[0]} = {valores[0]}'

            cursor.execute(query)

if __name__ == '__main__':
    empresa = EmpresaDAO.seleccionar()
    for i in empresa:
        print(i)