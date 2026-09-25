import random

print("===== RPG Character Generator =====")

name = input("Enter Character Name: ")

character_class = input(
    "Choose Class (Warrior/Mage/Archer): "
).lower()

if character_class == "warrior":
    health = 150
    attack = 30
    defense = 25
    magic = 5

elif character_class == "mage":
    health = 80
    attack = 15
    defense = 10
    magic = 40

elif character_class == "archer":
    health = 100
    attack = 25
    defense = 15
    magic = 15

else:
    print("Invalid Class!")
    exit()

level = random.randint(1, 10)

print("\n" + "=" * 40)
print("         RPG CHARACTER")
print("=" * 40)
print(f"Name      : {name}")
print(f"Class     : {character_class.title()}")
print(f"Level     : {level}")
print(f"Health    : {health}")
print(f"Attack    : {attack}")
print(f"Defense   : {defense}")
print(f"Magic     : {magic}")
print("=" * 40)