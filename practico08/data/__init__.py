from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from practico08.data.models import Base, Usuario, Sala, Voto, Votacion


class CapaDatos():
    def __init__(self):
        engine = create_engine('mysql+pymysql://spotifesta:spotifesta@localhost/spotifesta')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()

    def alta_usuario(self, usuario):
        """
        Da de alta a un usuario y lo devuelve
        :type usuario: Usuario
        :rtype: Usuario
        """
        self.session.add(usuario)
        self.session.commit()
        return usuario

    def buscar_usuario_por_nombre(self, nombre):
        """
        Busca un usuario por nombre y lo devuelve, devuelve None si no lo encuetra
        :type nombre:str
        :rtype: Usuario
        """
        u = self.session.query(Usuario).filter(Usuario.nombre == nombre).first()
        return u

    def buscar_usuario_por_id(self, id):
        """
        Busca un usuario por id y lo devuelve. Si no lo encuentra devuelve None
        :type id: int
        :rtype:Usuario
        """
        u = self.session.query(Usuario).filter(Usuario.id == id).first()
        return u

    def buscar_votacion_por_id(self, id):
        v = self.session.query(Votacion).filter(Votacion.id == id).first()
        return v

    def buscar_votacion_por_id_sala(self, id_sala):
        v = self.session.query(Votacion).filter(Votacion.id_sala == id_sala).first()
        return v

    def votos_get_all(self, id):
        votos = self.session.query(Voto).filter(Voto.id_votacion ==id).all()
        return votos

    def baja_votacion(self, votacion):
        self.session.delete(votacion)
        self.session.commit()

    def modificar_usuario(self, usuario):
        """
        Modifica un usuario y lo devuelve
        :type usuario:Usuario
        :return: Usuario
        """
        u = self.buscar_usuario_por_id(usuario.id)
        u.id = usuario.id
        u.nombre = usuario.nombre
        u.token = usuario.token
        u.refresh_token = usuario.refresh_token
        self.session.commit()

    def alta_sala(self, sala):

        """
        Da de alta a una sala y la devuelve
        :type sala: Sala
        :rtype: Sala
        """
        self.session.add(sala)
        self.session.commit()
        return sala

    def buscar_sala_por_link(self, link_invitacion):
        """
        Busca una sala por link_invitacion y la devuelve. Si no la encuentra devuelve None
        :type codigo: string
        :rtype:Sala
        """
        s = self.session.query(Sala).filter(Sala.link_invitacion == link_invitacion).first()
        return s

    def buscar_sala_por_id(self, id_sala):
        """
        Busca un usuario por id y lo devuelve
        :type id_sala:int
        :rtype: Sala
        """
        s = self.session.query(Sala).filter(Sala.id == id_sala).first()
        return s

    def alta_voto(self, voto):
        """
        Da de alta un voto si no puede devuelve none
        :type voto: Voto
        :rtype:Voto
        """
        self.session.add(voto)
        self.session.commit()
        return voto

    def modificar_sala(self, sala):
        s = self.buscar_sala_por_id(sala.id)
        s.votacion_vigente = sala.votacion_vigente
        s.link_invitacion = sala.link_invitacion
        self.session.commit()
        return s

    def alta_votacion(self, votacion):
        self.session.add(votacion)
        self.session.commit()
        return votacion

def test():
    datos = CapaDatos()
    usuario = datos.alta_usuario(Usuario(nombre="tito"))
    print(usuario.id)
    sala = datos.alta_sala(Sala(id_admin=usuario.id, link_invitacion=usuario.nombre)) # De momento le metemos el id, pero tendria que ser algo como un hash


if __name__ == '__main__':
    test()
