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
