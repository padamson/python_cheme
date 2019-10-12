"""Demonstrate uses of python in chemical engineering applications

Notes
-----
- [python_cheme] refers to the base directory of the python_cheme repository.

Examples
--------
TBD

"""
from pandas import DataFrame


def mole_fraction_a(weight_fraction_a, molecular_mass_a, molecular_mass_b):
    return (weight_fraction_a/molecular_mass_a)/(weight_fraction_a/molecular_mass_a +
            (1 - weight_fraction_a)/molecular_mass_b)


def mole_fractions(weight_fraction_a, molecular_mass_a, molecular_mass_b):
    mole_fraction_a = ((weight_fraction_a/molecular_mass_a) /
            (weight_fraction_a/molecular_mass_a + (1 - weight_fraction_a)/molecular_mass_b) )
    mole_fraction_b = 1 - mole_fraction_a
    return (mole_fraction_a, mole_fraction_b)
