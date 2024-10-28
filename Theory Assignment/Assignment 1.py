class Animal:
    def __init__(self, name, age, habitat, available):
        self.name = name
        self.age = age
        self.habitat = habitat
        self.is_available = available

    def change_availability_status(self, available):
        self.is_available = available

    def display_info(self):
        print("Displaying Animal's Info:")
        print(f"Name: {self.name}\nAge: {self.age}\nHabitat: {self.habitat}")
        if self.is_available:
            print("Status: Available for viewing")
        else:
            print("Status: In quarantine")


class Mammal(Animal):
    def __init__(self, name, age, habitat, available, fur, diet):
        super().__init__(name, age, habitat, available)
        self.fur_length = fur
        self.diet_type = diet

    def display_info(self):
        super().display_info()
        print(f"Fur Length: {self.fur_length}\nDiet Type: {self.diet_type}\n")


class Bird(Animal):
    def __init__(self, name, age, habitat, available, wingspan, flight):
        super().__init__(name, age, habitat, available)
        self.wingspan = wingspan
        self.flight_altitude = flight

    def display_info(self):
        super().display_info()
        print(f"Wingspan: {self.wingspan}\nFlight Altitude: {self.flight_altitude}\n")


class Reptile(Animal):
    def __init__(self, name, age, habitat, available, scale, venomous):
        super().__init__(name, age, habitat, available)
        self.scale_pattern = scale
        self.venomous_status = venomous
        
    def display_info(self):
        super().display_info()
        print(f"Scale Pattern: {self.scale_pattern}\nVenomous Status: {self.venomous_status}\n")


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
