from practico08.logic.Logic import Logic


class SesionLogic(Logic):
    def __init__(self, datos):
        super().__init__(datos)

    def alta_sesion(self, session):
        s = self.datos.alta_sesion(session)
        return s

    def buscar_sesion(self, id_usuario, id_sala):
        s = self.datos.buscar_sesion(id_usuario, id_sala)
        return s
