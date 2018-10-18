import unittest

from practico08.util import getRandomsString
from practico08.data import *
from practico08.data import Usuario, Sala, Voto, Votacion, Sesion


class TestDatos(unittest.TestCase):

    def setUp(self):
        super(TestDatos, self).setUp()
        self.dsa = DatosSala()
        self.du = DatosUsuarios()
        self.dv = DatosVotos()
        self.dse = DatosSesion()
        self.dvv = DatosVotacion()
        self.datos = [self.dsa, self.du, self.dv, self.dse, self.dvv]

    def tearDown(self):
        super(TestDatos, self).tearDown()
        for e in self.datos:
            e.borrar_todos()

    # TODO TEST USUARIOS
    def test_usuario_alta(self):
        # Precondición: No existes usuarios registrados
        self.assertEqual(len(self.du.todos()), 0)

        # Ejecucion
        u = Usuario(nombre="Tomaas", password="tomasu")
        exito = self.du.alta(u)

        # Post condicion: 1 usuario registrado
        self.assertTrue(exito)
        self.assertEqual(len(self.du.todos()), 1)

    def test_usuario_todos(self):
        # Precondicion: 5 usuarios registrados
        users = [Usuario(nombre="tomaas", password="contraseña"),
                 Usuario(nombre="tomaaso", password="contraseña"),
                 Usuario(nombre="marcela", password="contraseña"),
                 Usuario(nombre="eltomas", password="contrasela"),
                 Usuario(nombre="lamarcela", password="contraseña")]

        for u in users:
            self.du.alta(u)

        users = self.du.todos()
        self.assertTrue(len(users) >= 5)

    def test_usuarios_baja(self):
        # Precondicion: 1 usuario registrado
        u = Usuario(nombre="Tomaas", password="tomasu")
        exito = self.du.alta(u)
        leng = len(self.du.todos())
        self.assertTrue(leng >= 1)

        # Ejecucion
        exito = self.du.baja(u)

        # postcondicion 1 usuario desregistrado (?)
        self.assertTrue(exito)
        self.assertTrue(leng > len(self.du.todos()))

    def test_usuarios_buscar_por_nombre(self):
        # Precondicion 1 usuario con nombre warewax
        u = self.du.alta(Usuario(nombre="warewax", password="xaweraw"))

        wanted = self.du.buscar_por_nombre("warewax")
        self.assertEqual(wanted.nombre, "warewax")
        self.assertNotEqual(wanted.nombre, "pedrito")

    def test_usuario_buscar_por_id(self):
        # Precondicion: 1 usuario registrado
        u = self.du.alta(Usuario(nombre="Tomaas", password="tomasu"))

        wanted = self.du.buscar_por_id(u.id)

        self.assertEqual(u.id, wanted.id)

    def test_usuario_baja_todos(self):
        self.du.borrar_todos()
        todos = self.du.todos()
        self.assertEqual(len(todos),0)
        self.assertNotEqual(len(todos),1)

    # TODO TEST SALA
    def test_sala_alta(self):
        # Precondicion 1 usuario
        u = self.du.alta(Usuario(nombre="bautista", password="contraseña"))

        s = self.dsa.alta(Sala(id_admin=u.id, id_playlist="asdf"))
        total = len(self.dsa.todos())
        self.assertTrue(total > 0)
        self.assertFalse(total == 0)

    def test_sala_buscar_por_id(self):
        u = self.du.alta(Usuario(nombre="bautista", password="contraseña"))
        s = self.dsa.alta(Sala(id_admin=u.id, id_playlist="asdf"))
        wanted = self.dsa.buscar_por_id(s.id)
        self.assertEqual(s, wanted)

    def test_sala_buscar_por_link(self):
        u = self.du.alta(Usuario(nombre="bautista", password="contraseña"))
        s = self.dsa.alta(Sala(id_admin=u.id, id_playlist="asdf", link_invitacion=getRandomsString()))
        wanted = self.dsa.buscar_por_link(s.link_invitacion)
        self.assertEqual(s, wanted)

    def test_sala_baja(self):
        # precondicion 1 usuario y 1 sala
        u = self.du.alta(Usuario(nombre="bautista", password="contraseña"))
        s = self.dsa.alta(Sala(id_admin=u.id, id_playlist="asdf"))
        total_antes = len(self.dsa.todos())
        pass

    def test_sala_borrar_todos(self):
        antes = len(self.dsa.todos())
        self.dsa.borrar_todos()
        despues = len(self.dsa.todos())
        self.assertEqual(antes,despues)

    # TODO TEST SESION
    def test_sesion_alta(self):
        # Precondicion 1 usuario y una sala
        u = self.du.alta(Usuario(nombre="bautista", password="contraseña"))
        s = self.dsa.alta(Sala(id_admin=u.id, id_playlist="asdf"))
        antes = len(self.dse.todos())
        sala = self.dse.alta(Sesion(id_usuario=u.id, id_sala=s.id))
        despues = len(self.dse.todos())
        self.assertTrue(despues - antes == 1)

    def test_sesion_baja(self):
        u = self.du.alta(Usuario(nombre="bautista", password="contraseña"))
        s = self.dsa.alta(Sala(id_admin=u.id, id_playlist="asdf"))
        sala = self.dse.alta(Sesion(id_usuario=u.id, id_sala=s.id))
        antes = len(self.dse.todos())
        self.dse.baja(sala)
        despues = len(self.dse.todos())
        self.assertTrue(antes - despues == 1)

    def test_sesion_buscar(self):
        u = self.du.alta(Usuario(nombre="bautista", password="contraseña"))
        s = self.dsa.alta(Sala(id_admin=u.id, id_playlist="asdf"))
        sala = self.dse.alta(Sesion(id_usuario=u.id, id_sala=s.id))
        wanted = self.dse.buscar(id_usuario=u.id, id_sala=s.id)
        self.assertEqual(sala,wanted)

    def test_sesion_borrar_todos(self):
        self.dse.borrar_todos()
        self.assertTrue(len(self.dse.todos()) == 0)

    # TODO TEST VOTACION

    def test_votacion_alta(self):
        u = self.du.alta(Usuario(nombre="bautista", password="contraseña"))
        s = self.dsa.alta(Sala(id_admin=u.id, id_playlist="asdf"))
        sala = self.dse.alta(Sesion(id_usuario=u.id, id_sala=s.id))
        antes = len(self.dvv.todos())
        votacion = self.dvv.alta(Votacion(id_sala=s.id, tiempo_vida=0))
        despues = len(self.dvv.todos())
        self.assertTrue(despues - antes == 1)

    def test_votacion_baja(self):
        u = self.du.alta(Usuario(nombre="bautista", password="contraseña"))
        s = self.dsa.alta(Sala(id_admin=u.id, id_playlist="asdf"))
        sala = self.dse.alta(Sesion(id_usuario=u.id, id_sala=s.id))
        votacion = self.dvv.alta(Votacion(id_sala=s.id, tiempo_vida=0))
        antes = len(self.dvv.todos())
        self.dvv.baja(votacion)
        despues = len(self.dvv.todos())
        self.assertTrue(antes - despues == 1)

    def test_votacion_buscar_por_id_sala(self):
        u = self.du.alta(Usuario(nombre="bautista", password="contraseña"))
        s = self.dsa.alta(Sala(id_admin=u.id, id_playlist="asdf"))
        sala = self.dse.alta(Sesion(id_usuario=u.id, id_sala=s.id))
        votacion = self.dvv.alta(Votacion(id_sala=s.id, tiempo_vida=0))
        wanted = self.dvv.buscar_por_id_sala(votacion.id_sala)
        self.assertEqual(votacion, wanted)

    def test_votacion_buscar_por_id(self):
        u = self.du.alta(Usuario(nombre="bautista", password="contraseña"))
        s = self.dsa.alta(Sala(id_admin=u.id, id_playlist="asdf"))
        sala = self.dse.alta(Sesion(id_usuario=u.id, id_sala=s.id))
        votacion = self.dvv.alta(Votacion(id_sala=s.id, tiempo_vida=0))
        wanted = self.dvv.buscar_por_id(votacion.id)
        self.assertEqual(votacion, wanted)

    def test_votacion_borrar_todos(self):
        self.dvv.borrar_todos()
        self.assertTrue(len(self.dvv.todos()) == 0)

    # TODO TEST VOTOS
    def test_voto_alta(self):
        u = self.du.alta(Usuario(nombre="bautista", password="contraseña"))
        s = self.dsa.alta(Sala(id_admin=u.id, id_playlist="asdf"))
        sala = self.dse.alta(Sesion(id_usuario=u.id, id_sala=s.id))
        votacion = self.dvv.alta(Votacion(id_sala=s.id, tiempo_vida=0))
        antes = len(self.dv.todos())
        voto = self.dv.alta(Voto(id_usuario=sala.id_usuario,id_votacion=votacion.id, id_cancion="la macarena"))
        despues = len(self.dv.todos())
        self.assertTrue(despues - antes == 1)

    def test_voto_baja(self):
        u = self.du.alta(Usuario(nombre="bautista", password="contraseña"))
        s = self.dsa.alta(Sala(id_admin=u.id, id_playlist="asdf"))
        sala = self.dse.alta(Sesion(id_usuario=u.id, id_sala=s.id))
        votacion = self.dvv.alta(Votacion(id_sala=s.id, tiempo_vida=0))
        voto = self.dv.alta(Voto(id_usuario=sala.id_usuario, id_votacion=votacion.id, id_cancion="la macarena"))
        antes = len(self.dv.todos())
        self.dv.baja(voto)
        despues = len(self.dv.todos())
        self.assertTrue(antes - despues == 1)

    def test_voto_buscar_por_id(self):
        u = self.du.alta(Usuario(nombre="bautista", password="contraseña"))
        s = self.dsa.alta(Sala(id_admin=u.id, id_playlist="asdf"))
        sala = self.dse.alta(Sesion(id_usuario=u.id, id_sala=s.id))
        votacion = self.dvv.alta(Votacion(id_sala=s.id, tiempo_vida=0))
        voto = self.dv.alta(Voto(id_usuario=sala.id_usuario, id_votacion=votacion.id, id_cancion="la macarena"))
        wanted = self.dv.buscar_por_id(voto.id)
        self.assertEqual(voto, wanted)

    def test_voto_buscar_por_todo_por_id_votacion(self):
        u = self.du.alta(Usuario(nombre="bautista", password="contraseña"))
        s = self.dsa.alta(Sala(id_admin=u.id, id_playlist="asdf"))
        sala = self.dse.alta(Sesion(id_usuario=u.id, id_sala=s.id))
        votacion = self.dvv.alta(Votacion(id_sala=s.id, tiempo_vida=0))
        # TODO VER COMO TESTEAR LOS TODOS

    def test_voto_borrar_todos(self):
        self.dv.borrar_todos()
        self.assertTrue(len(self.dv.todos()) == 0)