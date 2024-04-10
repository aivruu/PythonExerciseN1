# Class Exercise N~1 - 09/04/2024

# We request the input for the user age, a then we convert the
# provided string to an int.
age = int(input("Por favor, introduce tu edad para empezar."))
# Check if the user is adult to could respond this pool.
if age < 18:
    print("Debes ser mayor de edad para responder este cuestionario.")
else:
    # Request the input for the first and last name of the
    # user.
    first_name = input("Introduce tu primer nombre.")
    last_name = input("Introduce tu primer apellido.")

    # Ask the user if is originary of some town.
    is_from_originary_town = input("Eres de algún pueblo originario?")
    if is_from_originary_town == "Yes":
        # We need to request the originary town name, and then
        # check if the name is "Mapuche".
        originary_town_name = input("Cuál es tu pueblo originario?")
        if originary_town_name == "Mapuche":
            print("Eres Mapuche, toma un Yan Yan!")

        print("Tu pueblo originario es: " + originary_town_name)

    # Request the user the amount of rooms, and persons on their house.
    rooms_amount = input("Cuántas habitaciones tiene tu casa?")
    persons_amount = input("Cuántas personas viven en tu casa?")
    # If the living persons amount in the house, is lower than the rooms amount.
    # The house will be expropriated.
    if persons_amount < rooms_amount:
        print("La cantidad de personas en el hogar no es suficiente para ocupar todas las habitaciones, tu casa será "
              "expropiada!")

    print("Ejecución Finalizada, los datos han sido subidos con éxito!")
