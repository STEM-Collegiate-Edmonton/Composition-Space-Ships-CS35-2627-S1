from components import Engine, Shield, Weapon


class Cruiser:
    def __init__(self):
        self.engine = Engine(500, 300)
        self.shield = Shield(200)
        self.weapon = Weapon(400, "Plasma Cannon")

    def attack(self):
        print("Cruiser attacking!")
        print(self.engine.activate())
        print(self.weapon.fire())

    def defend(self):
        print(self.shield.activate())