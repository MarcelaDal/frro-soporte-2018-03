from practico08.data import CapaDatos
from practico08.data.models import Usuario, Voto


async def init_logic(app):
    logica = Logic()
    app['logic'] = logica


class Logic():
    """
    Clase que encapsula toda la logica
    """
    def __init__(self):
        self.datos = CapaDatos()

    def alta_usuario(self, usuario):
        """
        Comprueba al usuario, lo guarda y lo devuelve . Devuelve None si no pasa la comprobacion
        Y comprueba las reglas
        :type user:Usuario
        :rtype: Usuario
        """

        try:

            if not self.isUsuarioRepetido(usuario.nombre) and self.isLongitudValida(usuario.nombre):
                p = self.datos.alta_usuario(usuario)
                if p:
                    return p
                else:
                    return False
            else:
                False
        except Exception as e:
            return e

    def isUsuarioRepetido(self,nombre):
        if self.buscar_usuario_por_nombre(nombre):
            return True
        else:
            raise UsuarioRepetido("usuario repetido")

    def isLongitudValida(self,nombre):
        long = len(nombre)
        if 20 > long > 6:
            return True
        else:
            raise UsuarioLongitudInvalida("Longitud invalida")

    def buscar_usuario_por_id(self, id):
        """
        Busca un usuario por id y lo devuelve. Si no lo encuentra devuelve None
        :type id:str
        :rtype: Usuario
        """
        u = self.datos.buscar_usuario_por_id(id)
        return u

    def buscar_usuario_por_nombre(self, nombre):
        """
        Busca un usuario por nombre
        :type nombre: str
        :rtype: Usuario
        """
        u = self.datos.buscar_usuario_por_nombre(nombre)
        return u

    def modificar_usuario(self, usuario):
        """
        Modifica un usuario realizando las comprobaciones correspondientes
        :type usuario:Usuario
        :rtype: Usuario
        """
        #if(isOk)
        u = self.datos.modificar_usuario(usuario)
        return u
    """
    Guarda una sala
    """
    def alta_sala(self, sala):
        s = None
        #validar que tiene una sala activa a la vez?
        s = self.datos.alta_sala(sala)
        return s

    def buscar_sala_por_codigo(self, link):
        """
        Busca una sala por link de invitacion. Si no lo encuentra devuelve None
        :type id:str
        :rtype: Usuario
        """
        s = self.datos.buscar_sala_por_link(link)
        return s

    def alta_voto(self, voto):
        v = self.datos.alta_voto(voto)


class UsuarioRepetido(Exception):
    pass


class UsuarioLongitudInvalida(Exception):
    pass


