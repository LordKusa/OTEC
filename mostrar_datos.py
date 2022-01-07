from dao.empresa import EmpresaDAO
from dao.planta import PlantaDAO
from dao.relevamiento_planta import RelevamientoPlantaDAO
from dao.personas import PersonaDAO

def cargar_empresas(campo = '', valor = ''):

    cabecera = [
        'ID Empresa', 
        'CUIT', 
        'Nombre legal', 
        'Nombre fantasía', 
        'Tipo societario', 
        'Página web', 
        'Rubro',
        'Actividad primaria',
        'Actividad secundaria',
        'MiPyME local',
        'Categoría PyME',
        'Habilitación municipal'
    ]

    if campo == '':
        datos = EmpresaDAO.seleccionar()
    else:
        atributos = [
            'id_empresa',
            'cuit',
            'nombre_legal',
            'nombre_fantasia',
            'tipo_societario',
            'pagina_web',
            'rubro',
            'actividad_primaria',
            'actividad_secundaria',
            'mipyme_local',
            'categoria_pyme',
            'habilitacion_municipal'
        ]

        indice = cabecera.index(campo)
        campo = atributos[indice]

        datos = EmpresaDAO.seleccionar_uno((campo, valor))
        datos = list(datos)

    return cabecera, datos, 'tabla_empresa'

def cargar_plantas(campo = '', valor = ''):
    cabecera = [
        'ID Planta',
        'ID Empresa',
        'Nombre',
        'Certificación AA - OPDS',
        'Categoría CAA',
        'Puntaje',
        'Potencia eléctrica contratada (KW)',
        'Normas y estándares certificados',
        'Dirección legal - Calle',
        'Dirección legal - Número',
        'Dirección legal - Localidad',
        'Dirección legal - Código postal',
        'Dirección administrativa - Calle',
        'Dirección administrativa - Número',
        'Dirección administrativa - Localidad',
        'Dirección administrativa - Código postal',
        'Dirección productiva - Calle',
        'Dirección productiva - Número',
        'Dirección productiva - Localidad',
        'Dirección productiva - Código postal',
        'Teléfono',
        'Email',
        'Página web',
        'GPS West',
        'GPS North'
    ]

    if campo == '':
        datos = PlantaDAO.seleccionar()
    else:
        atributos = [
            'id_planta',
            'id_empresa',
            'nombre',
            'certificado_aa_opds',
            'categoria_caa',
            'puntaje',
            'potencia_electrica',
            'normas_certificadas',
            'dl_calle',
            'dl_numero',
            'dl_localidad',
            'dl_cp',
            'da_calle',
            'da_numero',
            'da_localidad',
            'da_cp',
            'dp_calle',
            'dp_numero',
            'dp_localidad',
            'dp_cp',
            'telefono',
            'email',
            'pagina_web',
            'gps_west',
            'gps_north'
        ]

        indice = cabecera.index(campo)
        campo = atributos[indice]

        datos = PlantaDAO.seleccionar_uno((campo, valor))
        datos = list(datos)

    return cabecera, datos, 'tabla_plantas'

def cargar_relevamiento_planta():
    cabecera = [
        'ID Relevamiento',
        'ID Planta', 
        'Fecha', 
        'Potencia promedio consumida (KW)', 
        'Capacidad instalada en uso aproximado', 
        'Cantidad de personal total', 
        'Cantidad de personal en producción', 
        'Cantidad de personal administrativo', 
        'Cantidad de personal en otras actividades'
    ]

    datos = RelevamientoPlantaDAO.seleccionar()

    return cabecera, datos

def cargar_personas(campo = '', valor = ''):

    cabecera = [
        'ID Persona', 
        'ID Empresa', 
        'Nombre', 
        'Teléfono fijo', 
        'Teléfono celular', 
        'Mail', 
        'Tipo relación',
        'Observaciones'
    ]

    if campo == '':
        datos = PersonaDAO.seleccionar()
    else:
        atributos = [
            'id_persona',
            'id_empresa',
            'nombre',
            'telefono_fijo',
            'telefono_celular',
            'mail',
            'tipo_relacion',
            'observaciones'
        ]

        indice = cabecera.index(campo)
        campo = atributos[indice]

        datos = PersonaDAO.seleccionar_uno((campo, valor))
        datos = list(datos)

    return cabecera, datos, 'tabla_persona'

if __name__ == '__main__':
    pass