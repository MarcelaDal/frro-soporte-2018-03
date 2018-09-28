from practico08.data import DatosSingleton
from practico08.data import Usuario


class DatosUsuarios(DatosSingleton):
    def alta(self, usuario):
        """
        Da de alta a un usuario y lo devuelve
        :type usuario: Usuario
        :rtype: Usuario
        """
        self.session.add(usuario)
        self.session.commit()
        return usuario

    def buscar_por_nombre(self, nombre):
        """
        Busca un usuario por nombre y lo devuelve, devuelve None si no lo encuetra
        :type nombre:str
        :rtype: Usuario
        """
        u = self.session.query(Usuario).filter(Usuario.nombre == nombre).first()
        return u

    def buscar_por_id(self, id):
        """
        Busca un usuario por id y lo devuelve. Si no lo encuentra devuelve None
        :type id: int
        :rtype:Usuario
        """
        u = self.session.query(Usuario).filter(Usuario.id == id).first()
        return u

    def modificar(self, usuario):
        """
        Modifica un usuario y lo devuelve
        :type usuario:Usuario
        :return: Usuario
        """
        u = self.buscar_por_id(usuario.id)
        u.id = usuario.id
        u.nombre = usuario.nombre
        u.token = usuario.token
        u.refresh_token = usuario.refresh_token
        self.session.commit()
        return u
