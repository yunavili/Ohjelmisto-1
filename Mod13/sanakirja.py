import json
elokuva = {
    "nimi": "Inception",
    "vuosi": 2010,
    "nayttelijat": ["Sam Smith, Jane Doe"]
}

with open("movie.json", "w") as file:
    json.dump(elokuva, file, indent=4)

