from practico08.logic.Logic import Logic


class SalaLogic(Logic):
    def __init__(self, datos):
        super().__init__(datos)

    def alta_sala(self, sala):
        s = None
        #validar que tiene una sala activa a la vez?
        s = self.datos.alta_sala(sala)
        return s

    def buscar_sala_por_id(self, id):
        s = self.datos.buscar_sala_por_id(id)
        return s

    def buscar_sala_por_codigo(self, link):
        """
        Busca una sala por link de invitacion. Si no lo encuentra devuelve None
        :type id:str
        :rtype: Usuario
        """
        s = self.datos.buscar_sala_por_link(link)
        return s

    def modificar_sala(self, sala):
        sala = self.datos.modificar_sala(sala)
        return sala