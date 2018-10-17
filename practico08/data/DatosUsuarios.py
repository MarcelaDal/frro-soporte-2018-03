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

    def baja(self, usuario):
        """
        Da de baja un usuario
        Devuelve True si la baja fue exitosa
        :type usuario:Usuario
        :rtype:
        """
        try:
            self.session.delete(usuario)
            return True
        except:
            return False

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

    def todos(self):
        """
        Devuelve
        :return:
        """
        s = self.session.query(Usuario).all()
        return s

    def borrar_todos(self):
        """
        Borra todos los socios de la base de datos.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        try:
            usuarios = self.todos()
            for usuario in usuarios:
                self.baja(usuario)
            self.session.commit()
        except Exception:
            return False
        return True
