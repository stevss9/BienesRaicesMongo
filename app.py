#Completado
from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase
from product import Casa, Departamento, Edificio
from personas import Cliente, Empleado
from ventas import Venta
from bson import ObjectId
from datetime import datetime
from pymongo.errors import DuplicateKeyError

db = dbase.dbConnection()

transacciones_collection = db['Transacciones']
collection = db['Comentarios']
usuarios_collection = db['usuarios']
empleados_collection = db['empleados']
transacciones = db['Transacciones']

app = Flask(__name__, static_folder='static')

# Rutas de la aplicación
@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/casa')
def casa():
    return render_template('casa.html')

@app.route('/login')
def logueo():

    return render_template('login.html')

@app.route('/principal')
def principal():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['Name']
    email = request.form['Email']
    subject = request.form['Subject']
    comment = request.form['Comment']

    collection.insert_one({
        'name': name,
        'email': email,
        'subject': subject,
        'comment': comment
    })

    return render_template('inicio.html')

@app.route('/login', methods=['POST'])
def login():
    correo = request.form.get('correo')
    clave = request.form.get('clave')

    usuario = usuarios_collection.find_one({'correo': correo, 'clave': clave})

    if usuario:
       return render_template('index.html')
    else:
        return render_template('login.html')


@app.route('/login_failed')
def login_failed():
    return render_template('login_failed.html')

@app.route('/registrarse', methods=['POST'])
def registrarse():
    nombre = request.form.get('nombre')
    telefono = request.form.get('telefono')
    correo = request.form.get('correo')
    clave = request.form.get('clave')

    usuario = {
        'nombre': nombre,
        'telefono': telefono,
        'correo': correo,
        'clave': clave
    }

    usuarios_collection.insert_one(usuario)
    return render_template('login.html')

@app.route('/modificarCasa')
def modificarCasa():
    propiedades = db['propiedades']
    propiedades_recibidas = propiedades.find({"tipo": "casa"})

    return render_template('modificarCasa.html', propiedades=propiedades_recibidas)

@app.route('/modificarEdificio')
def modificarEdificio():
    propiedades = db['propiedades']
    propiedades_recibidas = propiedades.find({"tipo": "edificio"})

    return render_template('modificarEdificio.html', propiedades=propiedades_recibidas)

@app.route('/modificarDepartamento')
def modificarDepartamento():
    propiedades = db['propiedades']
    propiedades_recibidas = propiedades.find({"tipo": "departamento"})

    return render_template('modificarDepartamento.html', propiedades=propiedades_recibidas)



@app.route('/search', methods=['GET'])
def search():
    ubicacion = request.args.get('ubicacion')
    propiedades = db['propiedades'].find({'ubicacion': ubicacion})

    return render_template('bienes.html', propiedades=propiedades)

@app.route('/searchC', methods=['GET'])
def searchC():
    nombre = request.args.get('nombre')
    propiedades = db['propiedades'].find({'tipo': 'casa','nombre': nombre})

    return render_template('modificarCasa.html', propiedades=propiedades)

@app.route('/searchD', methods=['GET'])
def searchD():
    nombre = request.args.get('nombre')
    propiedades = db['propiedades'].find({'tipo': 'departamento','nombre': nombre})

    return render_template('modificarDepartamento.html', propiedades=propiedades)

@app.route('/searchEmpleados', methods=['GET'])
def searchEmpleados():
    nombre = request.args.get('nombre')
    empleados = db['empleados'].find({'nombre': nombre})

    return render_template('empleadoslista.html', empleados=empleados)

@app.route('/searchCliente', methods=['GET'])
def searchCliente():
    nombre = request.args.get('nombre')
    clientes = db['clientes'].find({'nombre': nombre})

    return render_template('clienteslista.html', clientes=clientes)

@app.route('/searchVenta', methods=['GET'])
def searchVenta():
    id_venta = request.args.get('_id')
    ventas = db['Transacciones'].find({'_id': id_venta})

    return render_template('historialventa.html', ventas=ventas)


@app.route('/departamento')
def departamento():
    return render_template('departamento.html')

@app.route('/edificio')
def edificio():
    return render_template('edificio.html')

@app.route('/registroventa')
def registroventa():
    return render_template('registroventa.html')

@app.route('/vistaventa')
def vistaventa():
    return render_template('vistaventas.html')

@app.route('/editE')
def editE():
    return render_template('editE.html')

@app.route('/editC')
def editC():
    return render_template('editC.html')

@app.route('/editPropiedad')
def editPropiedad():
    return render_template('editPropiedad.html')

@app.route('/historialventa')
def historialventa():
    transacciones = transacciones_collection.find()

    return render_template('historialventa.html', transacciones=transacciones)

@app.route('/addPropiedad')
def addPropiedad():
    return render_template('addPropiedad.html')

@app.route('/empleado')
def empleado():
    return render_template('empleado.html')

@app.route('/cliente')
def cliente():
    return render_template('cliente.html')

@app.route('/bienes')
def bienes():
    propiedades = db['propiedades'].find()

    return render_template('bienes.html', propiedades=propiedades)

@app.route('/registrarVenta')
def registrarVenta():
    propiedades = db['propiedades'].find()

    return render_template('registroventa.html', propiedades=propiedades)

@app.route('/darIdPropiedad/<string:propiedad_id>')
def darIdPropiedad(propiedad_id):
    propiedades = db['propiedades'].find({'_id': propiedad_id})

    return render_template('registrarventa.html', propiedades=propiedades)


@app.route('/getClientes')
def getClientes():
    clientes = db['clientes'].find()

    return render_template('clienteslista.html', clientes=clientes)

@app.route('/getClientesVenta')
def getClientesVenta():
    clientes = db['clientes'].find()

    return render_template('registrarventa.html', clientes=clientes)

@app.route('/getEmpleados')
def getEmpleados():
    empleados = db['empleados'].find()

    return render_template('empleadoslista.html', empleados=empleados)

@app.route('/getEmpleadosVenta')
def getEmpleadosVenta():
    empleados = db['empleados'].find()

    return render_template('registrarventa.html', empleados=empleados)

@app.route('/casa', methods=['POST'])
def addCasa():
    propiedades = db['propiedades']
    _id = request.form['_id']
    tipo = 'casa'
    ubicacion = request.form['ubicacion']
    precio = request.form['precio']
    nombre = request.form['nombre']
    habitaciones = request.form.get('habitaciones')
    banos = request.form.get('banos')

    if _id and ubicacion and precio and nombre:
        propiedad = {
            '_id': _id,
            'tipo': tipo,
            'ubicacion': ubicacion,
            'precio': precio,
            'nombre': nombre,
            'habitaciones': habitaciones,
            'banos': banos
        }
        propiedades.insert_one(propiedad)
        return redirect(url_for('addPropiedad'))
    else:
        return notFound()

@app.route('/departamento', methods=['POST'])
def addDepartamento():
    propiedades = db['propiedades']
    _id = request.form['_id']
    tipo = 'departamento'
    ubicacion = request.form['ubicacion']
    precio = request.form['precio']
    nombre = request.form['nombre']

    if _id and ubicacion and precio and nombre:
        propiedad = {
            '_id': _id,
            'tipo': tipo,
            'ubicacion': ubicacion,
            'precio': precio,
            'nombre': nombre,
        }
        propiedades.insert_one(propiedad)
        return redirect(url_for('addPropiedad'))
    else:
        return notFound()

@app.route('/edificio', methods=['POST'])
def addEdificio():
    propiedades = db['propiedades']
    _id = request.form['_id']
    tipo = 'edificio'
    ubicacion = request.form['ubicacion']
    precio = request.form['precio']
    nombre = request.form['nombre']
    pisos = request.form.get('pisos')

    if _id and ubicacion and precio and nombre:
        propiedad = {
            '_id': _id,
            'tipo': tipo,
            'ubicacion': ubicacion,
            'precio': precio,
            'nombre': nombre,
            'pisos': pisos
        }
        propiedades.insert_one(propiedad)
        return redirect(url_for('addPropiedad'))
    else:
        return notFound()

@app.route('/empleado', methods=['POST'])
def addEmpleado():
    empleados = db['empleados']
    _id = request.form['_id']
    nombre = request.form['nombre']
    salario = request.form['salario']
    cargo = request.form['cargo']

    if _id and nombre and salario and cargo:
        empleado = {
            '_id': _id,
            'nombre': nombre,
            'salario': salario,
            'cargo': cargo
        }
        empleados.insert_one(empleado)
        return redirect(url_for('editE'))
    else:
        return notFound()

@app.route('/cliente', methods=['POST'])
def addCliente():
    clientes = db['clientes']
    _id = request.form['_id']
    nombre = request.form['nombre']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    email = request.form['email']

    if _id and nombre and direccion and telefono and email:
        cliente = {
            '_id': _id,
            'nombre': nombre,
            'direccion': direccion,
            'telefono': telefono,
            'email': email
        }
        clientes.insert_one(cliente)
        return redirect(url_for('editC'))
    else:
        return notFound()

@app.route('/delete/empleado/<string:empleado_id>')
def deleteEmpleado(empleado_id):
    empleados = db['empleados']
    empleados.delete_one({'_id': empleado_id})

    return redirect(url_for('getEmpleados'))

@app.route('/delete/cliente/<string:cliente_id>')
def deleteCliente(cliente_id):
    clientes = db['clientes']
    clientes.delete_one({'_id': cliente_id})

    return redirect(url_for('getClientes'))


@app.route('/delete/<string:propiedad_id>')
def delete(propiedad_id):
    propiedades = db['propiedades']
    propiedades.delete_one({'_id': propiedad_id})

    return redirect(url_for('bienes'))

@app.route('/edit/casa/<string:propiedad_id>', methods=['POST'])
def editCasa(propiedad_id):
    propiedades = db['propiedades']
    _id = request.form['_id']
    tipo = 'casa'
    ubicacion = request.form['ubicacion']
    precio = request.form['precio']
    nombre = request.form['nombre']
    habitaciones = request.form.get('habitaciones')
    banos = request.form.get('banos')

    if _id and ubicacion and precio and nombre:
        propiedades.update_one(
            {'_id': propiedad_id},
            {'$set': {'_id': _id, 'tipo': tipo, 'ubicacion': ubicacion, 'precio': precio, 'nombre': nombre,
                      'habitaciones': habitaciones, 'banos': banos}}
        )
        return redirect(url_for('modificarCasa'))
    else:
        return notFound()

@app.route('/edit/departamento/<string:propiedad_id>', methods=['POST'])
def editDepartamento(propiedad_id):
    propiedades = db['propiedades']
    _id = request.form['_id']
    tipo = 'departamento'
    ubicacion = request.form['ubicacion']
    precio = request.form['precio']
    nombre = request.form['nombre']

    if _id and ubicacion and precio and nombre:
        propiedades.update_one(
            {'_id': propiedad_id},
            {'$set': {'_id': _id, 'tipo': tipo, 'ubicacion': ubicacion, 'precio': precio, 'nombre': nombre}}
        )
        return redirect(url_for('modificarDepartamento'))
    else:
        return notFound()

@app.route('/edit/edificio/<string:propiedad_id>', methods=['POST'])
def editEdificio(propiedad_id):
    propiedades = db['propiedades']
    _id = request.form['_id']
    tipo = 'edificio'
    ubicacion = request.form['ubicacion']
    precio = request.form['precio']
    nombre = request.form['nombre']
    pisos = request.form.get('pisos')

    if _id and ubicacion and precio and nombre:
        propiedades.update_one(
            {'_id': propiedad_id},
            {'$set': {'_id': _id, 'tipo': tipo, 'ubicacion': ubicacion, 'precio': precio, 'nombre': nombre,
                      'pisos': pisos}}
        )
        return redirect(url_for('modificarEdificio'))
    else:
        return notFound()


@app.route('/propiedades/<propiedad_id>', methods=['POST'])
def registrar_venta(propiedad_id):
    casa = request.form.get('casa')
    nombre_empleado = request.form.get('nombreE')
    nombre_cliente = request.form.get('nombreC')
    fecha_compra = request.form.get('fecha')
    valor = request.form.get('valor')

    # Crea un documento con los datos del formulario
    documento = {
        'propiedad_id': propiedad_id,
        'casa': casa,
        'nombre_empleado': nombre_empleado,
        'nombre_cliente': nombre_cliente,
        'fecha_compra': fecha_compra,
        'valor': valor
    }

    # Inserta el documento en la colección 'Transacciones'
    transacciones.insert_one(documento)

    # Redirecciona o realiza alguna acción después de insertar los datos
    return redirect(url_for('historialventa'))


@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404

    return response

@app.errorhandler(DuplicateKeyError)
def handle_duplicate_key_error(error):
    message = {
        'message': 'Clave duplicada',
        'status': '409 Conflict'
    }
    response = jsonify(message)
    response.status_code = 409

    return response

# Punto de entrada principal del programa
if __name__ == '__main__':
    app.run(debug=True, port=4000)