class Venta:
    """
    Clase que representa una venta.
    """

    def __init__(self, nombre_propiedad, empleado, cliente, fecha_compra, valor):
        """
        Constructor de la clase Venta.

        Args:
            nombre_propiedad (str): Nombre de la propiedad vendida.
            empleado (str): Nombre del empleado que realizó la venta.
            cliente (str): Nombre del cliente que compró la propiedad.
            fecha_compra (str): Fecha de la compra en formato 'YYYY-MM-DD'.
            valor (float): Valor de la venta.
        """
        self.nombre_propiedad = nombre_propiedad
        self.empleado = empleado
        self.cliente = cliente
        self.fecha_compra = fecha_compra
        self.valor = valor

    def toDBCollection(self):
        """
        Convierte el objeto Venta en un diccionario compatible con la base de datos.

        Returns:
            dict: Diccionario que representa la Venta.
        """
        return {
            'nombre_propiedad': self.nombre_propiedad,
            'empleado': self.empleado,
            'cliente': self.cliente,
            'fecha_compra': self.fecha_compra,
            'valor': self.valor
        }
