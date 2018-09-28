from practico08.data import DatosSingleton
from practico08.data import Votacion


class DatosVotacion(DatosSingleton):
    def buscar_por_id(self, id):
        v = self.session.query(Votacion).filter(Votacion.id == id).first()
        return v

    def buscar_por_id_sala(self, id_sala):
        v = self.session.query(Votacion).filter(Votacion.id_sala == id_sala).first()
        return v

    def baja(self, votacion):
        self.session.delete(votacion)
        self.session.commit()

    def alta(self, votacion):
        self.session.add(votacion)
        self.session.commit()
        return votacion