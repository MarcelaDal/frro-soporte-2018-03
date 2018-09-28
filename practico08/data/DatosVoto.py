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