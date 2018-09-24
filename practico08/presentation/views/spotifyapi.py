from aiohttp import ClientSession

# Añadir una cancion a una lista de reproducion especifica en una ubicacion especifica

#Esto se llamaria desde el "trabajo"
async with ClientSession() as session:
    auth_str = "Authorization: Bearer " + token
    async with session.post('https://api.spotify.com/v1/playlists/'+playlist_id+'/tracks',
                            headers={
                                'Authorization': auth_str,
                                'Content-Type': 'application/json'
                            },
                            json={
                                'uris': ['spotify:track:4EchqUKQ3qAQuRNKmeIpnf'],
                                'position': 3
                            }) as resp:
        json_resp = await resp.json()