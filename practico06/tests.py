# Implementar los casos de prueba descriptos.

import unittest

from practico05.ejercicio_01 import Socio
from practico06.capa_negocio import NegocioSocio, LongitudInvalida


class TestsNegocio(unittest.TestCase):

    def setUp(self):
        super(TestsNegocio, self).setUp()
        self.ns = NegocioSocio()

    def tearDown(self):
        super(TestsNegocio, self).tearDown()
        self.ns.datos.borrar_todos()

    def test_alta(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)

        # post-condiciones: 1 socio registrado
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 1)

    def test_regla_1(self):
        #precondicion socio existente
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)

        self.assertTrue(exito)
        #válido
        valido = Socio(dni=111222333, nombre='Jane', apellido='Doe')
        self.assertTrue(self.ns.regla_1(valido))

        #inválido
        invalido = Socio(dni=12345678, nombre='Jane', apellido='Doe')
        self.assertFalse(self.ns.regla_1(invalido))

    def test_regla_2_nombre_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='J', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_nombre_mayor_15(self):
         # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Manuel Jose Joaquin', apellido='Belgrano')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Manuel', apellido='B')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_mayor_15(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Jose', apellido='de San Martin y Matorras')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_3(self):
        pass


    def test_buscar(self):
        #socio existente
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)
        self.assertTrue(self.ns.buscar(exito.id))

        #socio inexistente
        self.assertFalse(self.ns.buscar(33))

    def test_buscar_dni(self):
        #socio existente
         #socio existente
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)
        self.assertTrue(self.ns.buscar(exito.dni))

        #socio inexistente
        self.assertFalse(self.ns.buscar_dni(98765432))

    def test_todos(self):
        #precondición: 1 socio registrado
        self.ns.borrar_todos()
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)
        self.assertTrue(exito)

        #logica
        cant = self.ns.todos()
        self.assertEqual(cant, 1)

    def test_modificacion(self):
        # pre-condiciones: socio existe
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        res = self.ns.alta(socio)
        self.assertTrue(res)

        # ejecuto la logica
        res.nombre = 'Juan Carlos'
        exito = self.ns.modificacion(res)
        self.assertEqual(socio, exito)

        #inválido por longitud de nombre
        socio.nombre = 'Jose Manuel del corazon de Jesus'
        invalido = self.ns.modificacion(socio)
        self.assertFalse(invalido)

        #inválido por longitud de apellido
        socio.apellido = 'de San Martin y Matorras'
        invalido = self.ns.modificacion(socio)
        self.assertFalse(invalido)

    def test_baja(self):
        # pre-condiciones: 1 socio registrado
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 1)

        # ejecuto la logica
        exito = self.ns.baja(1)

        # post-condiciones: 0 socios registrados
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 0)
