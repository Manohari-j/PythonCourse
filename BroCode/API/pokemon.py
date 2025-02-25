import requests

base_url = "https://pokeapi.co/api/v2/"


def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        # convert json to python dictionary
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")


pokemon_name = "charmander"
poke_info = get_pokemon_info(pokemon_name)

if poke_info:
    print(f"Name: {poke_info['name']}")
    print(f"Id: {poke_info['id']}")
    print(f"Height: {poke_info['height']}")
    print(f"Weight: {poke_info['weight']}")
    i=1
    print("Moves:")
    for move_data in poke_info['moves']:
        print(f"{i} : {move_data['move']['name']}")
        i +=1

