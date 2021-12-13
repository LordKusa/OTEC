from cursor_del_pool import CursorDelPool

class EmpresaDAO:
    _seleccionar = 'SELECT * FROM empresa ORDER BY cuit'
    _insertar = 'INSERT INTO empresa(cuit, nombre_legal, nombre_fantasia, tipo_societario, pagina_web, rubro, actividad_primaria, actividad_secundaria, mipyme_local, categoria_pyme, habilitacion_municipal) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    _ultimo = 'SELECT * FROM empresa ORDER BY id_empresa DESC LIMIT 1'
    _dashboard = 'SELECT tipo_societario, pagina_web, actividad_primaria, actividad_secundaria, mipyme_local, categoria_pyme, habilitacion_municipal FROM empresa'
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
    def ultimo(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._ultimo)
            registros = cursor.fetchall()
            for registro in registros:
                id = registro[0]
            return id

    @classmethod
    def dashboard(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._dashboard)
            registros = cursor.fetchall()
            empresas = []
            for registro in registros:
                empresa = []
                for i in range(7):
                    empresa.append(registro[i])
                empresas.append(empresa)
            return empresas

    @classmethod
    def insertar(cls, empresa):
        with CursorDelPool() as cursor:
            valores = (
                empresa['cuit'], 
                empresa['nombre_legal'], 
                empresa['nombre_fantasia'], 
                empresa['tipo_societario'], 
                empresa['pagina_web'], 
                empresa['rubro'], 
                empresa['actividad_primaria'], 
                empresa['actividad_secundaria'], 
                empresa['mipyme_local'], 
                empresa['categoria_pyme'],
                empresa['habilitacion_municipal']
            )
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
    print(EmpresaDAO.ultimo())