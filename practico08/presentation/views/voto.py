from practico08.presentation import Routes
#from practico08.data.models import Voto
from aiohttp.web import Request, json_response


@Routes.get('/voto')
def votar(request):
    """
    :type request: Request
    :rtype: json_response
    Para votar, parametros: sala, cancion, nombre de usuario listo :D
    """
    req = await request.json()
    cancion = req.get('cancion')
    sala_id = req.get('sala')
    usuario_id = req.get('usuario')
    if cancion and sala_id and usuario_id:
        logic = request.app['logic']
        usuario = logic.buscar_usuario_por_id(usuario_id)
        if not usuario:
            return json_response(status=400,data={'error':'usuario no registrado'})
        sala = logic.buscar_sala_por_codigo(sala_id)
        if not sala:
            return json_response(status=400, data={"error":"sala inexistente"})
        # Esta parte falta programar, primero se tiene que tener la sala lista
        # session = logic.buscar_session(usuario.id, sala.id)
        # if not session:
        #   return json_response(status=400, data={"error":"no hay session"}
        """
        Aca iria el post al voto
        Copiar la parte de ClientSession en auth y buscar en la referencia de la api de spotift como buscar una cancion :D
        """
        voto = logic.alta_voto(id_usuario=usuario.id, id_votacion=sala.votacion_vijente, id_cancion=cancion)
