class Animal:
    def animal(self):
        print("This is Class for animal")

class Mammals(Animal):
    def mammals(se):
        print("Mammals are the part of Animal Kingdom")

class Herbivores():
    def herb(self):
        print("The animal which depends on green foods or herbs are part of this Family")

class Cow(Mammals, Herbivores):
    def __init__(se):
        print("The Cow is a Herbivore Mammal")

class Horse(Mammals, Herbivores):
    def __init__(se):
        print("The Horse is a Herbivore Mammal")

print("------------------CoW------------------")
cw1 = Cow()
cw1.animal()
cw1.mammals()
cw1.herb()

print("-----------------Horse-------------------")
h = Horse()
h.animal()
h.mammals()
h.herb()

class Carnivores(Mammals):
    def __init__(self):
        print("This is construtor of class Carnivores")
    def carnivore(carnage):
        print("Carnivores eat flesh")

class Cat_Family():
    def cats(catt):
        print("Cats are Carnivores")


class Tiger(Cat_Family, Carnivores):
    def __init__(tig):
        print("This is Tiger")
    def tig(t):
        print("Tigers are cats")

print("-----------------Tiger-------------------")
tiger1 = Tiger()
tiger1.animal()
tiger1.mammals()
tiger1.carnivore()
tiger1.cats()
tiger1.tig()

class Pets1(Animal):
    def __init__(pet):
        print("-------------------------------------")
        print("Pets are harmless")

class Dogs1(Pets1):
    def doggy1(d):
        pet_type = "Dogs"
        return pet_type + " are pets"

class Fish1(Pets1):
    def fishhy1(f1):
        pet_type = "Fishes"
        print(pet_type, "are pets")

class Parrot1(Pets1):
    def parrot1(p1):
        pet_type = "Parrots"
        print(pet_type, "are pets")

dogg1 = Dogs1()
print(dogg1.doggy1())
fishh1 = Fish1()
fishh1.fishhy1()
parrot1 = Parrot1()
parrot1.parrot1()