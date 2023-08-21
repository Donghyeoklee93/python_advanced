class Item:
    def __init__(self, name):
        self.name = name

    def pick(self):
        print(f"[{self.name}] is picked")

    def discard(self):
        print(f"[{self.name}] is discarded")


class Weapon(Item):
    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage

    def attack(self):
        print(f"[{self.name}] is used. [{self.damage}] is attacked")


class HealingItem(Item):
    def __init__(self, name, recovery_amount):
        super().__init__(name)
        self.recover_amount = recovery_amount

    def use(self):
        print(f"[{self.name}] is used. [{self.recover_amount}] is recoverd.")


m16 = Weapon("m16", 110)
bandage = HealingItem("Bandage", 20)

m16.attack()
bandage.use()
