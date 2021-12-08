import urllib3
import json

http = urllib3.PoolManager()
url = 'https :// prevision -meteo.ch/services/json/strasbourg'
reponse =reponse.request('GET',url)
dico = json.loads(reponse.data.decode('utf -8'))
print(dico)