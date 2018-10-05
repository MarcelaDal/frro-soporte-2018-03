import unittest

from practico08.data import *
from practico08.data import Usuario, Sala, Voto, Votacion, Sesion


class TestDatos(unittest.TestCase):

    def setUp(self):
        super(TestDatos, self).setUp()
        self.dsa = DatosSala()
        self.du = DatosUsuarios()
        self.dv = DatosVotos()
        self.dse = DatosSesion()
        self.dv = DatosVotacion()
        self.datos = [self.dsa, self.du, self.dv, self.dse, self.dv]

    def tearDown(self):
        super(TestDatos, self).tearDown()
        for e in self.datos:
            e.borrar_todos()

    # TODO TEST USUARIOS
    def test_usuario_alta(self):
        # Precondición: No existes usuarios registrados
        self.assertEqual(len(self.du.todos()), 0)

        # Ejecucion
        u = Usuario(nombre="Tomaas")
        exito = self.du.alta(u)

        # Post condicion: 1 usuario registrado
        self.assertTrue(exito)
        self.assertEqual(len(self.du.todos()), 1)

    def test_usuarios_baja(self):
        # Precondicion: 1 usuario registrado
        u = Usuario(nombre="Tomaas")
        exito = self.du.alta(u)
        leng = len(self.du.todos())
        self.assertTrue(leng > 1)

        # Ejecucion
        exito = self.du.baja(u)

        # postcondicion 1 usuario desregistrado (?)
        self.assertTrue(exito)
        self.assertTrue(leng > len(self.du.todos()))
