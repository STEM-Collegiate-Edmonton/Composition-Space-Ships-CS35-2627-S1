from fighter import Fighter
from cruiser import Cruiser
from cargo_ship import CargoShip


fighter = Fighter()
cruiser = Cruiser()
cargo_ship = CargoShip()


print("FIGHTER")
fighter.attack()
fighter.defend()

print("CRUISER")
cruiser.attack()
cruiser.defend()

print("CARGO SHIP")
cargo_ship.travel()
cargo_ship.load_cargo(500)
cargo_ship.load_cargo(600)