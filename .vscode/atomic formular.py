from formula import parse_formula

# Compound dictionary
periodic_table_dict = {
    # symbol: [name, atomic_mass]
    "Ac": ["Actinium", 227],
    "Ag": ["Silver", 107.8682],
    "Al": ["Aluminum", 26.9815386],
    # ... rest of the periodic table entries
}

# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the elements listed in symbol_quantity_list."""
    total_molar_mass = 0.0

    for element in symbol_quantity_list:
        symbol = element[SYMBOL_INDEX]
        quantity = element[QUANTITY_INDEX]

        atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
        element_molar_mass = atomic_mass * quantity

        total_molar_mass += element_molar_mass

    return total_molar_mass


def main():
    formula = input("Enter the molecular formula of the sample: ")
    mass = float(input("Enter the mass in grams of the sample: "))

    # Call the make_periodic_table function if needed

    symbol_quantity_list = parse_formula(formula)
    molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table_dict)
    number_of_moles = mass / molar_mass

    print(f"Molar mass: {molar_mass:.5f} grams/mole")
    print(f"Number of moles: {number_of_moles:.5f} moles")


if name == "main":
    main()