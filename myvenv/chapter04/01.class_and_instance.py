class Unit:
    def __init__(self, name, hp, shield, damage):
        self.name = name
        self.hp = hp
        self.shield = shield
        self.damage = damage
        print(f"[{self.name}] is created.")

    def __str__(self):
        return f"[{self.name} hp : {self.hp} shield : {self.shield} attack : {self.damage}]"


probe = Unit("probe", 20, 20, 5)
zealot = Unit("zealot", 100, 60, 16)
dragon = Unit("dragon", 100, 80, 20)

print(probe)
print(zealot)
print(dragon)
