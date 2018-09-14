from practico08.data import CapaDatos

async def init_logic(app):
    logica = Logic()
    app['logic'] = logica
"""
Clase que encapsula toda la logica
"""
class Logic():
    def __init__(self):
        self.datos = CapaDatos()
    """
    Dado un usuario lo guarda en el cazo de que no exista lo crea
    """
    def saveUser(self, user):
        pass
    """
    Busca un usuario por id
    """
    def getUserById(self, id):
        pass
    """
    Busca un usuario por nombre
    """
    def getUserByName(self, name):
        pass

    """
    Guarda una sala
    """
    def saveSala(self, sala):
        pass