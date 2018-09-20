from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from practico08.data.models import Base, Usuario, Sala


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


def test():
    datos = CapaDatos()
    usuario = datos.alta_usuario(Usuario(nombre="tito"))
    print(usuario.id)


if __name__ == '__main__':
    test()
