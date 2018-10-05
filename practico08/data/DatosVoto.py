from practico08.data import DatosSingleton
from practico08.data import Voto


class DatosVotos(DatosSingleton):
    def alta(self, voto):
        """
        Da de alta un voto si no puede devuelve none
        :type voto: Voto
        :rtype:Voto
        """
        self.session.add(voto)
        self.session.commit()
        return voto

    def buscar_por_id(self, id):
        voto = self.session.query(Voto).filter(Voto.id == id).first()
        return voto

    def todos_por_id_votacion(self, id_votacion):
        votos = self.session.query(Voto).filter(Voto.id_votacion == id_votacion).all()
        return votos

    def todos(self):
        """
        Devuelve
        :rtype:list
        """
        s = self.session.query(Voto).all()
        return s

    def borrar_todos(self):
        """
        Borra todos los socios de la base de datos.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        try:
            votos = self.todos()
            for voto in votos:
                self.session.delete(votos)
            self.session.commit()
        except Exception:
            return False
        return True