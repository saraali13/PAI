class Animal:
    def __init__(self, name, age, habitat, available):
        self._name = name
        self._age = age
        self._habitat = habitat
        self._is_available = available

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_age(self):
        return self._age

    def set_age(self, value):
        self._age = value

    def get_habitat(self):
        return self._habitat

    def set_habitat(self, value):
        self._habitat = value

    def change_availability_status(self, available):
        self._is_available = available

    def display_info(self):
        print("Displaying Animal's Info:")
        print(f"Name: {self._name}\nAge: {self._age}\nHabitat: {self._habitat}")
        if self._is_available:
            print("Status: Available for viewing")
        else:
            print("Status: In quarantine")


class Mammal(Animal):
    def __init__(self, name, age, habitat, available, fur, diet):
        super().__init__(name, age, habitat, available)
        self._fur_length = fur
        self._diet_type = diet

    def get_fur_length(self):
        return self._fur_length

    def set_fur_length(self, value):
        self._fur_length = value

    def get_diet_type(self):
        return self._diet_type

    def set_diet_type(self, value):
        self._diet_type = value

    def display_info(self):
        super().display_info()
        print(f"Fur Length: {self._fur_length}\nDiet Type: {self._diet_type}\n")


class Bird(Animal):
    def __init__(self, name, age, habitat, available, wingspan, flight):
        super().__init__(name, age, habitat, available)
        self._wingspan = wingspan
        self._flight_altitude = flight

    def get_wingspan(self):
        return self._wingspan

    def set_wingspan(self, value):
        self._wingspan = value

    def get_flight_altitude(self):
        return self._flight_altitude

    def set_flight_altitude(self, value):
        self._flight_altitude = value

    def display_info(self):
        super().display_info()
        print(f"Wingspan: {self._wingspan}\nFlight Altitude: {self._flight_altitude}\n")


class Reptile(Animal):
    def __init__(self, name, age, habitat, available, scale, venomous):
        super().__init__(name, age, habitat, available)
        self._scale_pattern = scale
        self._venomous_status = venomous

    def get_scale_pattern(self):
        return self._scale_pattern

    def set_scale_pattern(self, value):
        self._scale_pattern = value

    def get_venomous_status(self):
        return self._venomous_status

    def set_venomous_status(self, value):
        self._venomous_status = value

    def display_info(self):
        super().display_info()
        print(f"Scale Pattern: {self._scale_pattern}\nVenomous Status: {self._venomous_status}\n")


# Sample Zoo
M1 = Mammal("Elephant", 15, "Jungle", True, "Short", "Herbivore")
M2 = Mammal("Whale", 12, "Ocean", True, "tiny", "Omnivore")
B1 = Bird("Eagle", 9, "Mountains", False, 6.5, 4000)
R1 = Reptile("Cobra", 7, "Jungle", True, "Smooth", "Venomous")
R2 = Reptile("Crocodile", 8, "Land and water", True, "Rough", "Not Venomous")

print("Zoo Management System:")
print(M1.display_info())
print(M2.display_info())
print(B1.display_info())
print(R1.display_info())
print(R2.display_info())

# Updating availability status
M2.change_availability_status(False)
R1.change_availability_status(False)
B1.change_availability_status(True)


print("\nInformation after update: ")
print("Zoo Management System:")
print(M1.display_info())
print(M2.display_info())
print(B1.display_info())
print(R1.display_info())
print(R2.display_info())
