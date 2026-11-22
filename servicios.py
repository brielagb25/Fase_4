from abc import ABC, abstractmethod
from entidades import Entidad
from excepciones import DatoInvalidoError, ServicioNoDisponibleError


class Servicio(Entidad, ABC):
    """Clase abstracta que define el comportamiento de un servicio."""

    def __init__(self, identificador, nombre, tarifa_hora, disponible=True):
        super().__init__(identificador)
        self.nombre = nombre
        self.tarifa_hora = tarifa_hora
        self.disponible = disponible
        self.validar()

    def validar(self):
        if not self.nombre or not self.nombre.strip():
            raise DatoInvalidoError("El nombre del servicio es obligatorio.")
        if not isinstance(self.tarifa_hora, (int, float)) or self.tarifa_hora <= 0:
            raise DatoInvalidoError("La tarifa por hora debe ser mayor que cero.")

    def comprobar_disponibilidad(self):
        if not self.disponible:
            raise ServicioNoDisponibleError(
                f"El servicio '{self.nombre}' no está disponible."
            )

    # En Python se simula la sobrecarga mediante parámetros opcionales.
    # Puede llamarse con solo horas, con impuesto o con impuesto y descuento.
    def calcular_costo(self, horas, impuesto=0, descuento=0):
        self.comprobar_disponibilidad()
        if not isinstance(horas, (int, float)) or horas <= 0:
            raise DatoInvalidoError("La duración debe ser mayor que cero.")
        if not 0 <= impuesto <= 100 or not 0 <= descuento <= 100:
            raise DatoInvalidoError("Impuesto y descuento deben estar entre 0 y 100.")
        subtotal = self.tarifa_hora * horas
        total = subtotal + subtotal * impuesto / 100
        total -= total * descuento / 100
        return round(total, 2)

    @abstractmethod
    def describir(self):
        pass


class ReservaSala(Servicio):
    def __init__(self, identificador, nombre, tarifa_hora, capacidad, disponible=True):
        self.capacidad = capacidad
        super().__init__(identificador, nombre, tarifa_hora, disponible)

    def validar(self):
        super().validar()
        if not isinstance(self.capacidad, int) or self.capacidad <= 0:
            raise DatoInvalidoError("La capacidad de la sala debe ser un entero positivo.")

    def describir(self):
        return f"Sala: {self.nombre}, capacidad para {self.capacidad} personas."


class AlquilerEquipo(Servicio):
    def __init__(self, identificador, nombre, tarifa_hora, cantidad, disponible=True):
        self.cantidad = cantidad
        super().__init__(identificador, nombre, tarifa_hora, disponible)

    def validar(self):
        super().validar()
        if not isinstance(self.cantidad, int) or self.cantidad <= 0:
            raise DatoInvalidoError("La cantidad de equipos debe ser positiva.")

    def describir(self):
        return f"Alquiler de equipo: {self.nombre}, unidades disponibles: {self.cantidad}."


class Asesoria(Servicio):
    def __init__(self, identificador, nombre, tarifa_hora, especialidad, disponible=True):
        self.especialidad = especialidad
        super().__init__(identificador, nombre, tarifa_hora, disponible)

    def validar(self):
        super().validar()
        if not self.especialidad or not self.especialidad.strip():
            raise DatoInvalidoError("La especialidad de la asesoría es obligatoria.")

    def describir(self):
        return f"Asesoría especializada en {self.especialidad}: {self.nombre}."
