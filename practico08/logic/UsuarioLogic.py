from practico08.logic.Logic import Logic


class UsuarioLogic(Logic):
    def __init__(self, datos):
        super().__init__(datos)

    def alta_usuario(self, usuario):
        """
        Comprueba al usuario, lo guarda y lo devuelve . Devuelve None si no pasa la comprobacion
        Y comprueba las reglas
        :type user:Usuario
        :rtype: Usuario
        """

        try:

            if self.isUsuarioUnico(usuario.nombre) and self.isLongitudValida(usuario.nombre):
                p = self.datos.alta_usuario(usuario)
                return p
            else:
                return False
        except Exception as e:
            return e

    def isUsuarioUnico(self,nombre):
        if not self.buscar_usuario_por_nombre(nombre):
            return True
        else:
            raise UsuarioRepetido("usuario repetido")

    def isLongitudValida(self,nombre):
        long = len(nombre)
        if 20 >= long >= 6:
            return True
        else:
            raise UsuarioLongitudInvalida("Longitud invalida")

    def buscar_usuario_por_id(self, id):
        """
        Busca un usuario por id y lo devuelve. Si no lo encuentra devuelve None
        :type id:int
        :rtype: Usuario
        """
        u = self.datos.buscar_usuario_por_id(id)
        if u:
            return u
        else:
            return False

    def buscar_usuario_por_nombre(self, nombre):
        """
        Busca un usuario por nombre
        :type nombre: str
        :rtype: Usuario
        """
        u = self.datos.buscar_usuario_por_nombre(nombre)
        if u:
            return u
        else:
            return False

    def buscar_usuario_por_id_sala(self, id_sala):
        sala = self.datos.buscar_sala_por_id(id_sala)
        user = self.datos.buscar_usuario_por_id(sala.id_admin)
        return user

    def modificar_usuario(self, usuario):
        """
        Modifica un usuario realizando las comprobaciones correspondientes
        :type usuario:Usuario
        :rtype: Usuario
        """
        try:
            if self.isUsuarioUnico(usuario.nombre) and self.isLongitudValida(usuario.nombre):
                p = self.datos.modificar_usuario(usuario)
                return p
        except Exception as e:
            return e


class UsuarioRepetido(Exception):
    pass


class UsuarioLongitudInvalida(Exception):
    pass
