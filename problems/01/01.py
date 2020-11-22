from math import floor
from utils.utils import read_file

# Part 1
mod_mass = read_file("input_01.py")


def calc_fuel(mass):
    return floor(mass / 3) - 2

fuel_mass_per_mod = [calc_fuel(modm) for modm in mod_mass]
print(f'Sum of fuel per module mass: {sum(fuel_mass_per_mod)}')


# Part 2
def fuels_fuel(fuel_mass):
    total_fuel = fuel_mass
    while fuel_mass > 0:
        new_fuel = calc_fuel(fuel_mass)
        if new_fuel > 0:
            total_fuel += new_fuel
        fuel_mass = new_fuel
    return total_fuel

total_fuel_per_mod = [fuels_fuel(fuel_mass) for fuel_mass in fuel_mass_per_mod]

print(f'Sum of fuel needed, including fuel to support the fuel... : {sum(total_fuel_per_mod)}')
