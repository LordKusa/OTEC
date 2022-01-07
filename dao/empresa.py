from cursor_del_pool import CursorDelPool

class EmpresaDAO:
    _seleccionar = 'SELECT * FROM empresa'
    _seleccionar_uno = 'SELECT * FROM empresa WHERE'
    _insertar = 'INSERT INTO empresa(cuit, nombre_legal, nombre_fantasia, tipo_societario, pagina_web, rubro, actividad_primaria, actividad_secundaria, mipyme_local, categoria_pyme, habilitacion_municipal) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    _dashboard = 'SELECT tipo_societario, pagina_web, rubro, mipyme_local, categoria_pyme, habilitacion_municipal FROM empresa'
    # _actualizar = 'UPDATE empresa SET'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._seleccionar)
            registros = cursor.fetchall()
            empresas = []
            for registro in registros:
                empresa = []
                for i in range(12):
                    empresa.append(registro[i])
                empresas.append(empresa)
            return empresas

    @classmethod
    def seleccionar_uno(cls, valores):
        with CursorDelPool() as cursor:
            query = f'{cls._seleccionar_uno} {valores[0]} = \'{valores[1]}\''
            cursor.execute(query)
            registros = cursor.fetchall()
            if cursor.rowcount != 1:
                empresas = []
                for registro in registros:
                    empresa = []
                    for i in range(12):
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

    # @classmethod
    # def actualizar(cls, empresa):
    #     with CursorDelPool() as cursor:
    #         valores = (
    #             empresa.cuit, 
    #             empresa.nombre_legal, 
    #             empresa.nombre_fantasia, 
    #             empresa.tipo_societario, 
    #             empresa.pagina_web, 
    #             empresa.rubro, 
    #             empresa.actividad_primaria, 
    #             empresa.actividad_secundaria, 
    #             empresa.mipyme_local, 
    #             empresa.categoria_pyme,
    #             empresa.habilitacion_municipal
    #         )
    #         cursor.execute(cls._actualizar, valores)

if __name__ == '__main__':
    print(EmpresaDAO.seleccionar())