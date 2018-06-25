# Implementar los metodos de la capa de negocio de socios.

from practico05.ejercicio_01 import Socio
from practico05.ejercicio_02 import DatosSocio


class DniRepetido(Exception):
    pass


class LongitudInvalida(Exception):
    pass


class MaximoAlcanzado(Exception):
    pass


class NegocioSocio(object):

    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """

        socio = self.datos.buscar(id_socio)
        if socio:
            return socio
        else:
            return None

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """

        socio = self.datos.buscar_dni(dni_socio)
        if socio:
            return socio
        else:
            return None

    def todos(self):
        """
        Devuelve listado de todos los socios.
        :rtype: list
        """
        socios = self.datos.todos()
        return socios

    def alta(self, socio):
        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type socio: Socio
        :rtype: bool
        """
        try:
            if (self.regla_1(socio) and self.regla_2(socio) and self.regla_3()):
                socio = self.datos.alta(socio)
                if socio:
                    return socio
                else:
                    return False
            else:
                return False
        except Exception as e:
            return e

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """

        resp = self.datos.baja(id_socio)
        if resp:
            return True
        else:
            return False

    def borrar_todos(self):
        """
        Borra todos los socios
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """

        resp = self.datos.borrar_todos()
        if resp:
            return True
        else:
            return False

    def modificacion(self, socio):
        """
        Modifica un socio.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type socio: Socio
        :rtype: bool
        """
        try:
            if self.regla_2(socio):
                p = self.datos.modificacion(socio)
                if p:
                    return True
                else:
                    return False
        except Exception as e:
            return False

    def regla_1(self, socio):
        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """
        socios = self.datos.todos()
        result = socio.dni not in [s.dni for s in socios]
        if result:
            return True
        else:
            raise DniRepetido


    def regla_2(self, socio):
        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """

        if len(socio.nombre) < self.MIN_CARACTERES or len(socio.nombre) > self.MAX_CARACTERES:
            raise LongitudInvalida('El nombre debe contener al menos 3 caracteres y no más de 15.')

        if len(socio.apellido) < self.MIN_CARACTERES or len(socio.apellido) > self.MAX_CARACTERES:
            raise LongitudInvalida('El apellido debe contener al menos 3 caracteres y no más de 15.')


        return True

    def regla_3(self):
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        socios = self.datos.todos()
        if len(socios) >= self.MAX_SOCIOS:
            raise MaximoAlcanzado('Se ha alcanzado el límite de socios permitido.')

        return True
