class Casa:
    """
    Clase que representa una casa.
    """

    def __init__(self, _id, tipo, ubicacion, precio, nombre, habitaciones, banos):
        """
        Constructor de la clase Casa.

        Args:
            _id (str): ID de la casa.
            tipo (str): Tipo de propiedad ('casa').
            ubicacion (str): Ubicación de la casa.
            precio (str): Precio de la casa.
            nombre (str): Nombre de la casa.
            habitaciones (str): Número de habitaciones de la casa.
            banos (str): Número de baños de la casa.
        """
        self._id = _id
        self.tipo = tipo
        self.ubicacion = ubicacion
        self.precio = precio
        self.nombre = nombre
        self.habitaciones = habitaciones
        self.banos = banos

    def toDBCollection(self):
        """
        Convierte el objeto Casa en un diccionario compatible con la base de datos.

        Returns:
            dict: Diccionario que representa la Casa.
        """
        return {
            '_id': self._id,
            'tipo': self.tipo,
            'ubicacion': self.ubicacion,
            'precio': self.precio,
            'nombre': self.nombre,
            'habitaciones': self.habitaciones,
            'banos': self.banos,
            'jardin': self.jardin
        }


class Departamento:
    """
    Clase que representa un departamento.
    """

    def __init__(self, _id, tipo, ubicacion, precio, nombre):
        """
        Constructor de la clase Departamento.

        Args:
            _id (str): ID del departamento.
            tipo (str): Tipo de propiedad ('departamento').
            ubicacion (str): Ubicación del departamento.
            precio (str): Precio del departamento.
            nombre (str): Nombre del departamento.
        """
        self._id = _id
        self.tipo = tipo
        self.ubicacion = ubicacion
        self.precio = precio
        self.nombre = nombre

    def toDBCollection(self):
        """
        Convierte el objeto Departamento en un diccionario compatible con la base de datos.

        Returns:
            dict: Diccionario que representa el Departamento.
        """
        return {
            '_id': self._id,
            'tipo': self.tipo,
            'ubicacion': self.ubicacion,
            'precio': self.precio,
            'nombre': self.nombre,
        }


class Edificio:
    """
    Clase que representa un edificio.
    """

    def __init__(self, _id, tipo, ubicacion, precio, nombre, pisos):
        """
        Constructor de la clase Edificio.

        Args:
            _id (str): ID del edificio.
            tipo (str): Tipo de propiedad ('edificio').
            ubicacion (str): Ubicación del edificio.
            precio (str): Precio del edificio.
            nombre (str): Nombre del edificio.
            pisos (str): Número de pisos del edificio.
        """
        self._id = _id
        self.tipo = tipo
        self.ubicacion = ubicacion
        self.precio = precio
        self.nombre = nombre
        self.pisos = pisos

    def toDBCollection(self):
        """
        Convierte el objeto Edificio en un diccionario compatible con la base de datos.

        Returns:
            dict: Diccionario que representa el Edificio.
        """
        return {
            '_id': self._id,
            'tipo': self.tipo,
            'ubicacion': self.ubicacion,
            'precio': self.precio,
            'nombre': self.nombre,
            'pisos': self.pisos,
        }
