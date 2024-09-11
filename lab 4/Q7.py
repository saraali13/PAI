class Vehicle:
    def __init__(self, seating):
        self.seating_capacity = seating

    def fare(self):
        total_fare = self.seating_capacity*100
        return total_fare

class Bus(Vehicle):
     def __init__(self, seating):
        self.seating_capacity = seating

     def fare_Bus(self):
        fare = self.fare() + (self.fare() * 10/100)
        print(f"Total fare: {fare}")



B1=Bus(34)
print(B1.fare())
B1.fare_Bus()
