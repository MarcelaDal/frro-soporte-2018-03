from practico08.logic.Logic import Logic


class VotoLogic(Logic):
    def __init__(self, datos):
        super().__init__(datos)

    def buscar_votacion_por_id(self,id):
        """
        :param id:
        :rtype:Votacion
        """
        votacion = self.datos.buscar_votacion_por_id(id)
        return votacion

    def votos_get_all(self,id):
        votos = self.datos.votos_get_all(id)
        return votos

    def baja_votacion(self, votacion):
        self.datos.baja_votacion(self.buscar_votacion_por_id(votacion))