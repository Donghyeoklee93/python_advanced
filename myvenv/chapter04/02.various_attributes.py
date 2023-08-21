class Unit:
    """
    instance attribute : name, hp, shield, attack
    -> Attributes with different values for each object.

    class attribute
    -> Attributes shared by all objects.

    Private Attributes
    -> Attributes that can only be accessed within the class.

    """

    count = 0

    def __init__(self, name, hp, shield, damage):
        self.name = name
        self.__hp = hp
        self.shield = shield
        self.damage = damage
        Unit.count += 1
        print(f"[{self.name}] is created.")

    def __str__(self):
        return f"[{self.name} hp : {self.__hp} shield : {self.shield} attack : {self.damage}]"


probe = Unit("probe", 20, 20, 5)
zealot = Unit("zealot", 100, 60, 16)
dragon = Unit("dragon", 100, 80, 20)

print(probe)
print(zealot)
print(dragon)

# instance attribute
probe.damage += 1
print(probe)

# Private Attributes
probe.__hp = 9999
print(probe)

# name mangling
probe._Unit__hp = 9999
print(probe)

# class attribute
print(Unit.count)
