class ErrorSistema(Exception):
    """Excepción base del sistema Software FJ."""


class DatoInvalidoError(ErrorSistema):
    """Se genera cuando un dato no cumple las validaciones."""


class ServicioNoDisponibleError(ErrorSistema):
    """Se genera cuando un servicio no está disponible."""


class ReservaError(ErrorSistema):
    """Se genera cuando una reserva no puede procesarse."""
