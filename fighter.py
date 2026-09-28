from components import Engine, Shield, Weapon


class Fighter:
    def __init__(self):
        self.engine = Engine(900, 100)
        self.shield = Shield(60)
        self.weapon = Weapon(150, "Laser Cannon")

    def attack(self):
        print("Fighter attacking!")
        print(self.engine.activate())
        print(self.weapon.fire())

    def defend(self):
        print(self.shield.activate())