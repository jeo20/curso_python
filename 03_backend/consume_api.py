import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org') # Coneccion a la API de Football Data
headers = { 'X-Auth-Token': 'bf69fe9bc3194ffb864adfead2ab5804' }   # key de autenticacion para Football Data
connection.request('GET', '/v2/competitions/DED', None, headers )  # Request GET que solicita competiciones de la liga alemana
response = json.loads(connection.getresponse().read().decode()) # Respuesta en formato JSON

# Funcion que devuelve los equipos con el nombre pasado por parametro, si no existe ninguno devuelve un mensaje de error
print (response)