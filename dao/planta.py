from cursor_del_pool import CursorDelPool

class PlantaDAO:
    _seleccionar = 'SELECT * FROM planta'
    _seleccionar_uno = 'SELECT * FROM planta WHERE'
    _insertar = 'INSERT INTO planta(id_empresa, nombre, certificado_aa_opds, categoria_caa, puntaje, potencia_electrica, normas_certificadas, dl_calle, dl_numero, dl_localidad, dl_cp, da_calle, da_numero, da_localidad, da_cp, dp_calle, dp_numero, dp_localidad, dp_cp, telefono, email, pagina_web, gps_west, gps_north) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._seleccionar)
            registros = cursor.fetchall()
            plantas = []
            for registro in registros:
                planta = []
                for i in range(17):
                    planta.append(registro[i])
                plantas.append(planta)
            return plantas

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
                    for i in range(17):
                        empresa.append(registro[i])
                    empresas.append(empresa)
            else:
                empresas = list(registros)
            return empresas

    @classmethod
    def insertar(cls, planta):
        with CursorDelPool() as cursor:
            if type(planta) == dict:
                valores = []
                for clave in planta:
                    valores.append(planta[clave])
            elif type(planta) == list:
                valores = planta
            valores = tuple(valores)
            cursor.execute(cls._insertar, valores)