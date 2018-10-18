from practico08.data import DatosUsuarios
from practico08.logic import LogicSingleton
from practico08.logic.LogicSala import LogicSala

class UsuarioException(Exception):
    pass


class LogicUsuario(LogicSingleton):
    def alta(self, usuario):
        """
        Comprueba al usuario, lo guarda y lo devuelve . Devuelve None si no pasa la comprobacion
        Y comprueba las reglas
        :type user:Usuario
        :rtype: Usuario
        """
        if self.isUsuarioUnico(usuario.nombre) and self.isLongitudValida(usuario.nombre):
            p = DatosUsuarios().alta(usuario)
            return p
        else:
            return False

    def isUsuarioUnico(self,nombre):
        if not DatosUsuarios().buscar_por_nombre(nombre):
            return True
        else:
            raise UsuarioException("usuario repetido")

    def isLongitudValida(self,nombre):
        long = len(nombre)
        if 20 >= long >= 6:
            return True
        else:
            raise UsuarioException("Longitud invalida")

    def buscar_por_id(self, id):
        """
        Busca un usuario por id y lo devuelve. Si no lo encuentra devuelve None
        :type id:int
        :rtype: Usuario
        """
        u = DatosUsuarios().buscar_por_id(id)
        if u:
            return u
        else:
            return False

    def buscar_por_nombre(self, nombre, password):
        """
        Busca un usuario por nombre
        :type nombre: str
        :rtype: Usuario
        """
        u = DatosUsuarios().buscar_por_nombre(nombre)
        if u and u.password == str(password):
            return u
        else:
            return False

    def buscar_por_id_sala(self, id_sala):
        sala = LogicSala().buscar_por_id(id_sala)
        user = DatosUsuarios().buscar_por_id(sala.id_admin)
        return user

    def modificar(self, usuario):
        """
        Modifica un usuario realizando las comprobaciones correspondientes
        :type usuario:Usuario
        :rtype: Usuario
        """
        p = DatosUsuarios().modificar(usuario)
        return p

    def borrar_todos(self):
        DatosUsuarios().borrar_todos()
