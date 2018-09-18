from practico08.data import CapaDatos, Usuario
async def init_logic(app):
    logica = Logic()
    app['logic'] = logica


class Logic():
    """
    Clase que encapsula toda la logica
    """
    def __init__(self):
        self.datos = CapaDatos()

    def alta_usuario(self, usuario):
        """
        Comprueba al usuario, lo guarda y lo devuelve . Devuelve None si no pasa la comprobacion
        :type user:Usuario
        :rtype: Usuario
        """
        p = None
        if not self.buscar_usuario_por_nombre(usuario.nombre):
            p = self.datos.alta_usuario(usuario)
        return p

    def buscar_usuario_por_id(self, id):
        """
        Busca un usuario por id y lo devuelve. Si no lo encuentra devuelve None
        :type id:str
        :rtype: Usuario
        """
        u = self.datos.buscar_usuario_por_id(id)
        return u

    def buscar_usuario_por_nombre(self, nombre):
        """
        Busca un usuario por nombre
        :type nombre: str
        :rtype: Usuario
        """
        u = self.datos.buscar_usuario_por_nombre(nombre)
        return u

    def modificar_usuario(self, usuario):
        """
        Modifica un usuario realizando las comprobaciones correspondientes
        :type usuario:Usuario
        :rtype: Usuario
        """
        #if(isOk)
        u = self.datos.modificar_usuario(usuario)
        return u
    """
    Guarda una sala
    """
    def saveSala(self, sala):
        pass