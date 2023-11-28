primeiro = input()
segundo = input()
terceiro = input()

especie = {
    "vertebrado": {
        "ave": {"carnivoro": "aguia", "onivoro": "pomba"},
        "mamifero": {"onivoro": "homem", "herbivoro": "vaca"},
    },
    "invertebrado": {
        "inseto": {"hematofago": "pulga", "herbivoro": "lagarta"},
        "anelideo": {"hematofago": "sanguessuga", "onivoro": "minhoca"},
    },
}

animal = especie.get(primeiro, {}).get(segundo, {}).get(terceiro)

if animal:
    print(animal)
