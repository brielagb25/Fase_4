from abc import ABC, abstractmethod
from excepciones import DatoInvalidoError


class Entidad(ABC):
    """Clase abstracta para las entidades generales del sistema."""

    def __init__(self, identificador):
        if not identificador or not str(identificador).strip():
            raise DatoInvalidoError("El identificador es obligatorio.")
        self._identificador = str(identificador)

    @property
    def identificador(self):
        return self._identificador

    @abstractmethod
    def validar(self):
        """Cada entidad define sus propias validaciones."""
        pass


class Cliente(Entidad):
    """Representa un cliente con datos encapsulados."""

    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono
        self.validar()

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def validar(self):
        if not isinstance(self.__nombre, str) or len(self.__nombre.strip()) < 2:
            raise DatoInvalidoError("El nombre debe tener al menos 2 caracteres.")
        if not isinstance(self.__correo, str) or "@" not in self.__correo or "." not in self.__correo:
            raise DatoInvalidoError("El correo electrónico no es válido.")
        if not str(self.__telefono).isdigit() or len(str(self.__telefono)) < 7:
            raise DatoInvalidoError("El teléfono debe contener al menos 7 dígitos.")

    def __str__(self):
        return f"Cliente {self.identificador}: {self.nombre} | {self.correo}"
