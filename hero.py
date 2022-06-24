from pprint import pprint
import requests
host = 'https://akabab.github.io/superhero-api/api'
def best_intelligence(list_hero):
  response = requests.get(f'{host}/all.json')
  list_id = []
  for hero in list_hero:
    for elem in response.json():
      if hero == elem['name']:
        list_id.append(elem['id'])
  intelligence = 0
  for id in list_id:
    resp = requests.get(f'{host}/powerstats/{id}.json')
    if resp.json()['intelligence'] > intelligence:
      intelligence = resp.json()['intelligence']
      name = requests.get(f'{host}/id/{id}.json')
      
      
  pprint(name.json()['name'])
      



best_intelligence(['Captain America','Thanos','Hulk'])
# 'Thanos''Hulk'