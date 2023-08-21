class Unit:
    """
    instance attribute : name, hp, shield, attack
    class attribute
    """

    count = 0

    def __init__(self, name, hp, shield, damage):
        self.name = name
        self.hp = hp
        self.shield = shield
        self.damage = damage
        Unit.count += 1
        print(f"[{self.name}] is created.")

    def __str__(self):
        return f"[{self.name} hp : {self.hp} shield : {self.shield} attack : {self.damage}]"

    # instance method
    # medthod that can access to instance attribute

    def hit(self, damage):
        if self.shield >= damage:
            self.shield -= damage
            damage = 0
        else:
            damage -= self.shield
            self.shield = 0

        if damage > 0:
            if self.hp > damage:
                self.hp -= damage
            else:
                self.hp = 0

    # class method
    # method that can access to class attribute
    @classmethod
    def print_count(cls):
        print(f"created unit number : [{cls.count}]")


probe = Unit("probe", 20, 20, 5)
zealot = Unit("zealot", 100, 60, 16)
dragon = Unit("dragon", 100, 80, 20)

probe.hit(16)
print(probe)
probe.hit(16)
print(probe)
probe.hit(16)
print(probe)


Unit.print_count()
