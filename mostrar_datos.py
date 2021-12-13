from dao.empresa import EmpresaDAO
from dao.planta import PlantaDAO
from dao.relevamiento_planta import RelevamientoPlantaDAO

def cargar_empresas():

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

    datos = EmpresaDAO.seleccionar()

    return cabecera, datos

def cargar_plantas():
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

    datos = PlantaDAO.seleccionar()

    return cabecera, datos

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