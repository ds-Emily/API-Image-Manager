import requests

class PokemonAPI:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_pokemon(self, pokemon_id):
        pokemon_url = f"{self.api_url}/{pokemon_id}"
        response = requests.get(pokemon_url)
        response.raise_for_status()
        return response.json()
