class Empleado:
    """
    Clase que representa un empleado.
    """

    def __init__(self, _id, nombre, salario, cargo):
        """
        Constructor de la clase Empleado.

        Args:
            _id (str): ID del empleado.
            nombre (str): Nombre del empleado.
            salario (float): Salario del empleado.
            cargo (str): Cargo del empleado.
        """
        self._id = _id
        self.nombre = nombre
        self.salario = salario
        self.cargo = cargo

    def toDBCollection(self):
        """
        Convierte el objeto Empleado en un diccionario compatible con la base de datos.

        Returns:
            dict: Diccionario que representa el Empleado.
        """
        return {
            '_id': self._id,
            'nombre': self.nombre,
            'salario': self.salario,
            'cargo': self.cargo,
        }


class Cliente:
    """
    Clase que representa un cliente.
    """

    def __init__(self, _id, nombre, direccion, telefono, email):
        """
        Constructor de la clase Cliente.

        Args:
            _id (str): ID del cliente.
            nombre (str): Nombre del cliente.
            direccion (str): Dirección del cliente.
            telefono (str): Teléfono del cliente.
            email (str): Correo electrónico del cliente.
        """
        self._id = _id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    def toDBCollection(self):
        """
        Convierte el objeto Cliente en un diccionario compatible con la base de datos.

        Returns:
            dict: Diccionario que representa el Cliente.
        """
        return {
            '_id': self._id,
            'nombre': self.nombre,
            'direccion': self.direccion,
            'telefono': self.telefono,
            'email': self.email,
        }
