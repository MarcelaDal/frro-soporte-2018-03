from practico08.data import DatosSingleton
from practico08.data import Sesion


class DatosSesion(DatosSingleton):
    def alta(self, sesion):
        self.session.add(sesion)
        self.session.commit()
        return sesion

    def buscar(self, id_usuario, id_sala):
        sesion = self.session.query(Sesion).filter(Sesion.id_sala == id_sala and Sesion.id_usuario == id_usuario).first()
        return sesion

    def todos(self):
        """
        Devuelve
        :return:
        """
        s = self.session.query(Sesion).all()
        return s

    def baja(self):
        pass

    def borrar_todos(self):
        """
        Borra todos los socios de la base de datos.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        try:
            sesiones = self.todos()
            for sesion in sesiones:
                self.session.delete(sesion)
            self.session.commit()
        except Exception:
            return False
        return True

    def baja(self, sesion):
        """
        Da de baja un usuario
        Devuelve True si la baja fue exitosa
        :type sesion:Sesion
        :rtype:
        """
        try:
            self.session.delete(sesion)
            return True
        except:
            return False
