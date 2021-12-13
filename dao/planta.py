from cursor_del_pool import CursorDelPool

class PlantaDAO:
    _seleccionar = 'SELECT * FROM planta'
    _insertar = 'INSERT INTO planta(id_empresa, nombre, certificado_aa_opds, categoria_caa, puntaje, potencia_electrica, normas_certificadas, dl_calle, dl_numero, dl_localidad, dl_cp, da_calle, da_numero, da_localidad, da_cp, dp_calle, dp_numero, dp_localidad, dp_cp, telefono, email, pagina_web, gps_west, gps_north) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    _ultimo = 'SELECT * FROM planta ORDER BY id_planta DESC LIMIT 1'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._seleccionar)
            registros = cursor.fetchall()
            plantas = []
            for registro in registros:
                planta = []
                for i in range(25):
                    planta.append(registro[i])
                plantas.append(planta)
            return plantas

    @classmethod
    def ultimo(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._ultimo)
            registros = cursor.fetchall()
            for registro in registros:
                id = registro[0]
            return id

    @classmethod
    def insertar(cls, planta):
        with CursorDelPool() as cursor:
            valores = (
                planta['id_empresa'],
                planta['nombre'],
                planta['certificacion_aa_opds'], 
                planta['categoria_caa'], 
                planta['puntaje'], 
                planta['potencia_electrica'], 
                planta['normas_certificadas'], 
                planta['dl_calle'], 
                planta['dl_numero'], 
                planta['dl_localidad'], 
                planta['dl_cp'], 
                planta['da_calle'], 
                planta['da_numero'], 
                planta['da_localidad'], 
                planta['da_cp'], 
                planta['dp_calle'], 
                planta['dp_numero'], 
                planta['dp_localidad'], 
                planta['dp_cp'], 
                planta['telefono'], 
                planta['email'], 
                planta['web'], 
                planta['gps_west'], 
                planta['gps_north']
            )
            cursor.execute(cls._insertar, valores)