from practico08.data import DatosSingleton
from practico08.data import Sala


class DatosSala(DatosSingleton):
    def alta(self, sala):

        """
        Da de alta a una sala y la devuelve
        :type sala: Sala
        :rtype: Sala
        """
        self.session.add(sala)
        self.session.commit()
        return sala

    def buscar_por_link(self, link_invitacion):
        """
        Busca una sala por link_invitacion y la devuelve. Si no la encuentra devuelve None
        :type codigo: string
        :rtype:Sala
        """
        s = self.session.query(Sala).filter(Sala.link_invitacion == link_invitacion).first()
        return s

    def buscar_por_id(self, id_sala):
        """
        Busca un usuario por id y lo devuelve
        :type id_sala:int
        :rtype: Sala
        """
        s = self.session.query(Sala).filter(Sala.id == id_sala).first()
        return s

    def modificar(self, sala):
        s = self.buscar_por_id(sala.id)
        s.votacion_vigente = sala.votacion_vigente
        s.link_invitacion = sala.link_invitacion
        self.session.commit()
        return s
