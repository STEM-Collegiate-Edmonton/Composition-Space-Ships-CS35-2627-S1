from components import Engine, Shield, CargoHold


class CargoShip:
    def __init__(self):
        self.engine = Engine(300, 500)
        self.shield = Shield(100)
        self.cargo_hold = CargoHold(1000)

    def travel(self):
        print("Cargo ship travelling!")
        print(self.engine.activate())
        print(self.shield.activate())

    def load_cargo(self, amount):
        print(self.cargo_hold.load(amount))