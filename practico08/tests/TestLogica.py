import unittest

from practico08.util import getRandomsString
from practico08.logic import *
from practico08.logic.LogicSala import SalaException
from practico08.logic.LogicUsuario import UsuarioException
from practico08.logic.LogicSesion import SesionException
from practico08.logic.LogicVoto import VotoException
from practico08.data import Usuario, Sala, Voto, Votacion, Sesion

class TestLogic(unittest.TestCase):

    def setUp(self):
        super(TestLogic, self).setUp()
        self.lsa = LogicSala()
        self.lu = LogicUsuario()
        self.lv = LogicVoto()
        self.lse = LogicSesion()
        self.lvv = LogicVotacion()
        self.datos = [self.lsa, self.lu, self.lv, self.lse, self.lvv]

    def tearDown(self):
        super(TestLogic, self).tearDown()
        self.lu.borrar_todos()
        self.lsa.borrar_todos()
        self.lse.borrar_todos()
        self.lv.borrar_todos()
    """    for e in self.datos:
            e.borrar_todos()"""

    # TEST LOGICA USUARIOS
    def test_usuario_alta(self):
        user = Usuario(nombre="leonardo", password="contraseña")
        u = LogicUsuario().alta(user)
        self.assertEqual(u, user)
        with self.assertRaises(UsuarioException):
            user2 = Usuario(nombre="leonardo", password="contraseña")
            u2 = LogicUsuario().alta(user2)
            user3 = Usuario(nombre="leo", password="contraseña")
            u3 = LogicUsuario().alta(user3)

    # TODO TEST LOGICA SALA
    def test_sala_alta(self):
        # Pre condicion 1 usuario registrado
        user = LogicUsuario().alta(Usuario(nombre="Matias", password="contraseña",token='hola'))

        sala = Sala(id_admin=user.id, link_invitacion=getRandomsString(), id_playlist="numero de playlist")
        s = self.lsa.alta(sala)
        self.assertEqual(s, sala)
        with self.assertRaises(SalaException):
            # Otra sala para un usuario
            self.lsa.alta(sala)

            # Usuario sin token
            user = LogicUsuario().alta(Usuario(nombre="Matiasu", password="contraseña"))
            sala = Sala(id_admin=user.id, link_invitacion=getRandomsString(), id_playlist="numero de playlist")
            s = self.lsa.alta(sala)

    # TODO TEST SESION
    def test_sesion_alta(self):
        # Pre condicion 1 usuario registrado
        user = self.lu.alta(Usuario(nombre="Matias", password="contraseña", token='hola'))
        sala = self.lsa.alta(Sala(id_admin=user.id, link_invitacion=getRandomsString(), id_playlist="numero de playlist"))

        sesion = Sesion(id_usuario=user.id, id_sala=sala.id)
        s = self.lse.alta(sesion)
        self.assertEqual(s, sesion)
        with self.assertRaises(SesionException):
            s = self.lse.alta(sesion)

    # TODO TEST VOTACION
    def test_voto_alta(self):
        user = self.lu.alta(Usuario(nombre="Matias", password="contraseña", token='hola'))
        sala = self.lsa.alta(Sala(id_admin=user.id, link_invitacion=getRandomsString(), id_playlist="numero de playlist"))
        sesion = self.lse.alta(Sesion(id_usuario=user.id, id_sala=sala.id))
        votacion = self.lvv.alta(Votacion(id_sala=sala.id, tiempo_vida=0))

        voto = Voto(id_usuario=sesion.id, id_votacion=votacion.id, id_cancion="tomitos")
        v = self.lv.alta(voto)
        self.assertEqual(v, voto)
        with self.assertRaises(VotoException):
            self.lv.alta(voto)