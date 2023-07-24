import requests
def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}" # Kullanıcı pokemon adını büyük harflerle girerse gerekli önemleri alıyoruz.
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon_info = {
            "name": pokemon_data["name"],
            "height": pokemon_data["height"],
            "weight": pokemon_data["weight"],
        }
        return pokemon_info
    else:
        return None


pokemon_name = input("Bir pokemon adı giriniz: ")
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info['name']}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")
else:
    print("Pokemon Bulunamadı.. ")