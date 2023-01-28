import requests
def find_character(name):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    req = requests.get(url)
    for info in req.json():
        if info["name"] == name:
            return info


def compare_intelligence(character_1, character_2, character_3):
    characters = {}
    characters[character_1["name"]] = character_1["powerstats"]["intelligence"]
    characters[character_2["name"]] = character_2["powerstats"]["intelligence"]
    characters[character_3["name"]] = character_3["powerstats"]["intelligence"]
    print(f"Из введенных персонажей наибольший интеллект у персонажа {max(characters.keys())} он равняется {max(characters.values())}")

hulk = find_character("Hulk")
thanos = find_character("Thanos")
cap = find_character("Captain America")
compare_intelligence(hulk, thanos, cap)
