from excepciones import ReservaError, ServicioNoDisponibleError


class Reserva:
    ESTADOS = ("PENDIENTE", "CONFIRMADA", "CANCELADA")

    def __init__(self, identificador, cliente, servicio, duracion):
        if cliente is None or servicio is None:
            raise ReservaError("La reserva debe tener cliente y servicio.")
        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ReservaError("La duración debe ser mayor que cero.")
        self.identificador = str(identificador)
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "PENDIENTE"

    def confirmar(self):
        if self.estado != "PENDIENTE":
            raise ReservaError("Solo se pueden confirmar reservas pendientes.")
        self.servicio.comprobar_disponibilidad()
        self.estado = "CONFIRMADA"
        return f"Reserva {self.identificador} confirmada."

    def cancelar(self):
        if self.estado == "CANCELADA":
            raise ReservaError("La reserva ya está cancelada.")
        self.estado = "CANCELADA"
        return f"Reserva {self.identificador} cancelada."

    def procesar(self, impuesto=0, descuento=0):
        try:
            if self.estado == "CANCELADA":
                raise ReservaError("No se puede procesar una reserva cancelada.")
            costo = self.servicio.calcular_costo(
                self.duracion, impuesto, descuento
            )
        except ServicioNoDisponibleError as error:
            raise ReservaError("No fue posible procesar: servicio no disponible.") from error
        return costo

    def __str__(self):
        return (f"Reserva {self.identificador} | {self.cliente.nombre} | "
                f"{self.servicio.nombre} | {self.duracion} horas | {self.estado}")
