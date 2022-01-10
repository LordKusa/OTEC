from flask import Flask, render_template, session, url_for, request, redirect, flash
import os
from dao.clae import ClaeDAO
from dao.usuario import UsuarioDAO
from dao.empresa import EmpresaDAO
from dao.planta import PlantaDAO
from dao.personas import PersonaDAO
from mostrar_datos import *

METHODS = ['GET', 'POST']

app = Flask(__name__)
app.secret_key = b'test'
app.config['UPLOAD_FOLDER'] = os.path.abspath('./uploads/')
app.jinja_env.add_extension('jinja2.ext.do')

@app.route('/', methods=METHODS)
def index():
    return render_template('index.html')

@app.route('/login', methods=METHODS)
def login():
    exito = False
    if request.method == 'POST':
        dic = {
            'usuario' : request.form['username'],
            'clave' : request.form['clave']
        }

        db = UsuarioDAO.seleccionar(dic['usuario'])

        if db != None and dic['clave'] == db['clave']:
            session['username'] = request.form['username']
            html = redirect(url_for('index'))
            exito = True
        else: 
            flash("Usuario o contraseña invalido")

    if not(exito):
        html = render_template('login.html')
    return html

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Deslogueado con éxito')
    return redirect(url_for('login'))

@app.route('/empresa', methods=METHODS)
def empresa():
    clae = ClaeDAO.seleccionar()
    tipos = ['Sociedades Comerciales', 'Sociedad colectiva', 'Sociedad en Comandita Simple', 'Sociedad de Capital e Industria', 
             'Sociedad de Responsabilidad Limitada', 'Sociedad Anónima', 'Sociedad Anónima con Participación', 'Sociedad Anónima con Participación Estatal Mayoritaria', 
             'Sociedad en Comandita por Acciones', 'Sociedad Unipersonal', 'Sociedades de constitución no regular', 'Sociedades de Hecho', 
             'Sociedades Irregulares']
    actividades = []
    categorias = ['Micro', 'Pequeña', 'Mediana tramo 1', 'Mediana tramo 2']
    habilitaciones = ['Si', 'En trámite', 'Precaria', 'Definitiva', 
                      'HSM', 'PUP', 'Otros']

    for i in clae:
        actividades.append(i[1])
    
    if request.method == 'POST':
        dic = {}
        dic = request.form.to_dict()

        actividad1 = dic['actividad_primaria']
        actividad2 = dic['actividad_secundaria']

        for i in clae:
            if actividad1 == i[1]:
                dic['actividad_primaria'] = i[0]
            if actividad2 == i[1]:
                dic['actividad_secundaria'] = i[0]

        EmpresaDAO.insertar(dic)

    return render_template('empresa.html', mod=False, tipos=tipos, actividades=actividades, categorias=categorias, habilitaciones=habilitaciones)

@app.route('/modificar/empresa/<id>', methods=METHODS)
def modificar_empresa(id):
    clae = ClaeDAO.seleccionar()
    tipos = ['Sociedades Comerciales', 'Sociedad colectiva', 'Sociedad en Comandita Simple', 'Sociedad de Capital e Industria', 'Sociedad de Responsabilidad Limitada', 'Sociedad Anónima', 
             'Sociedad Anónima con Participación', 'Sociedad Anónima con Participación Estatal Mayoritaria', 'Sociedad en Comandita por Acciones', 'Sociedad Unipersonal', 
             'Sociedades de constitución no regular', 'Sociedad de Hecho', 'Sociedades Irregulares', 'Monotributo']
    actividades = []
    categorias = ['Micro', 'Pequeña', 'Mediana tramo 1', 'Mediana tramo 2']
    habilitaciones = ['Si', 'En trámite', 'Precaria', 'Definitiva', 'HSM', 'PUP', 'Otros']

    for i in clae:
        actividades.append(i[1])

    empresa = list(EmpresaDAO.seleccionar_uno(('id_empresa', id))[0])
    print(empresa[6])

    return render_template('mod_empresa.html', mod=True, tipos=tipos, actividades=actividades, categorias=categorias, habilitaciones=habilitaciones, empresa=empresa)

@app.route('/planta', methods=METHODS)
def planta():
    if request.method == 'POST':
        dic = request.form.to_dict()
        PlantaDAO.insertar(dic)

    return render_template('planta.html')

@app.route('/persona', methods=METHODS)
def persona():
    if request.method == 'POST':
        dic = request.form.to_dict()
        PersonaDAO.insertar(dic)

    return render_template('persona.html')

@app.route('/upload', methods=METHODS)
def upload():
    html = render_template('upload.html')
    if request.method == 'POST':
        archivo = request.files['archivo']
        archivo.save(os.path.join(app.config['UPLOAD_FOLDER'], archivo.filename))
        html = redirect(url_for('index'))
    return html

@app.route('/ver_datos', methods=METHODS)
def ver_datos():
    lista = ['Empresas', 'Plantas', 'Relevamiento de plantas', 'Personas']
    cabecera, datos, tabla = cargar_empresas()

    if request.method == 'POST':
        if 'mostrar' == request.form['identificador']:
            if 'Plantas' == request.form['lista']:
                cabecera, datos, tabla = cargar_plantas()
            elif 'Relevamiento de plantas' == request.form['lista']:
                cabecera, datos = cargar_relevamiento_planta()
            elif 'Personas' == request.form['lista']:
                cabecera, datos, tabla =  cargar_personas()

        else:
            if 'tabla_empresa' == request.form['tipotabla']:
                cabecera, datos, tabla = cargar_empresas(request.form['lista'], request.form['texto'])
            elif 'tabla_plantas' == request.form['tipotabla']:
                cabecera, datos, tabla = cargar_plantas(request.form['lista'], request.form['texto'])
            elif 'tabla_persona' == request.form['tipotabla']:
                cabecera, datos, tabla = cargar_plantas(request.form['lista'], request.form['texto'])
              
    return render_template('ver_datos.html', lista=lista, cabecera=cabecera, datos=datos, tabla=tabla)

@app.route('/dashboard')
def dashboard():
    tipo_societario = {}
    pagina_web = 0
    rubro = {}
    mipyme_local = 0
    categoria_pyme = {}
    habilitacion_municipal = 0

    datos = EmpresaDAO.dashboard()
    for elemento in datos:
        if tipo_societario.get(elemento[0]) == None:
            tipo_societario[elemento[0]] = 1
        else:
            tipo_societario[elemento[0]] += 1
        
        if elemento[1] != '' and not(elemento[1] in 'no tiene') and not(elemento[1] in 'No tiene') and elemento[1] != '0':
            pagina_web += 1

        if rubro.get(elemento[2]) == None:
            rubro[elemento[2]] = 1
        else:
            rubro[elemento[2]] += 1

        if elemento[3] == 'Si':
            mipyme_local += 1

        if categoria_pyme.get(elemento[4]) == None:
            categoria_pyme[elemento[4]] = 1
        else:
            categoria_pyme[elemento[4]] += 1

        if elemento[5] == 'Si':
            habilitacion_municipal += 1

    return render_template('dashboard.html', tipo_societario=tipo_societario, pagina_web=pagina_web, actividad=rubro, mipyme_local=mipyme_local, 
                            categoria_pyme=categoria_pyme, habilitacion_municipal=habilitacion_municipal)

@app.route('/buscar', methods=METHODS)
def buscar():
    html = render_template('buscar.html')
    if request.method == 'POST':
        html = redirect(url_for('resultado', tabla='cuit', id=request.form['cuit']))
    return html

@app.route('/buscar/<tabla>/<id>')
def resultado(tabla, id):
    empresa = EmpresaDAO.seleccionar_uno((tabla, id))
    empresa = empresa[0]
    plantas = PlantaDAO.seleccionar_uno(('id_empresa', empresa[0]))

    return render_template('datos_empresa.html', empresa=empresa, plantas=plantas)

@app.before_request
def antes_de_cada_peticion():
    ruta = request.path
    if not 'username' in session and ruta != "/login" and not ruta.startswith("/static"):
        flash("Inicia sesión para continuar")
        return redirect("/login")


app.run(host='localhost', port=1234, debug=True)