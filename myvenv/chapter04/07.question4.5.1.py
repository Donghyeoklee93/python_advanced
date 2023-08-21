unit_info = {
    "probe": {
        "name": "probe",
        "mineral": 50,
        "gas": 0,
        "hp": 20,
        "shield": 20,
        "damage": 5,
    },
    "zealot": {
        "name": "zealot",
        "mineral": 100,
        "gas": 0,
        "hp": 100,
        "shield": 60,
        "damage": 16,
    },
    "dragon": {
        "name": "dragon",
        "mineral": 125,
        "gas": 50,
        "hp": 100,
        "shield": 80,
        "damage": 20,
    },
}


class Unit:
    def __init__(self, name, hp, shield, damage):
        self.name = name
        self.hp = hp
        self.shield = shield
        self.damage = damage


class Player:
    def __init__(self, nickname, mineral, gas, unit_list=[]):
        self.nickname = nickname
        self.mineral = mineral
        self.gas = gas
        self.unit_list = unit_list

    def produce(self, name, mineral, gas, hp, shield, damage):
        if self.mineral - mineral < 0:
            print("Mineral is not enough.")
        elif self.gas - gas < 0:
            print("Gas is not enough.")
        else:
            self.mineral -= mineral
            self.gas -= gas
            unit = Unit(name, hp, shield, damage)
            self.unit_list.append(unit)
            print(f"[{name}] is generated")


player1 = Player("Bisu", 400, 50)

player1.produce(
    unit_info["probe"]["name"],
    unit_info["probe"]["mineral"],
    unit_info["probe"]["gas"],
    unit_info["probe"]["hp"],
    unit_info["probe"]["shield"],
    unit_info["probe"]["damage"],
)

player1.produce(
    unit_info["zealot"]["name"],
    unit_info["zealot"]["mineral"],
    unit_info["zealot"]["gas"],
    unit_info["zealot"]["hp"],
    unit_info["zealot"]["shield"],
    unit_info["zealot"]["damage"],
)

player1.produce(
    unit_info["dragon"]["name"],
    unit_info["dragon"]["mineral"],
    unit_info["dragon"]["gas"],
    unit_info["dragon"]["hp"],
    unit_info["dragon"]["shield"],
    unit_info["dragon"]["damage"],
)


for unit in player1.unit_list:
    print(
        f"[{unit.name}] hp : {unit.hp} shield : {unit.shield}, damage : {unit.damage}"
    )
