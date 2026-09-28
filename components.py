class Engine:
    def __init__(self, speed, fuel):
        self.speed = speed
        self.fuel = fuel

    def activate(self):
        if self.fuel > 0:
            self.fuel -= 10
            return f"Engine activated. Speed: {self.speed} km/s"
        return "Not enough fuel!"


class Shield:
    def __init__(self, strength):
        self.strength = strength

    def activate(self):
        return f"Shields activated. Strength: {self.strength}%"


class Weapon:
    def __init__(self, damage, weapon_type):
        self.damage = damage
        self.weapon_type = weapon_type

    def fire(self):
        return f"Fired {self.weapon_type}. Damage: {self.damage}"


class CargoHold:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cargo = 0

    def load(self, amount):
        if self.cargo + amount <= self.capacity:
            self.cargo += amount
            return f"Loaded {amount} units. Cargo: {self.cargo}/{self.capacity}"
        return "Cargo hold is full!"