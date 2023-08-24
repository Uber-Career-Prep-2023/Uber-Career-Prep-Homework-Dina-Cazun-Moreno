from collections import deque

class Pet:
    def __init__(self, name, species, time):
        self.name = name
        self.species = species
        self.time = time

catQueue = deque()
dogQueue = deque()

initialPets = [
    Pet("Fluffy", "cat", 3),
    Pet("Buddy", "dog", 5),
    Pet("Mittens", "cat", 1)
]

for pet in initialPets:
    if pet.species == "cat":
        catQueue.append(pet)
    else:
        dogQueue.append(pet)
