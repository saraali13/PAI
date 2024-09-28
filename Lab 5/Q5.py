class Vehicle:
    def __init__(self,make,model,price,available):
        self.make=make
        self.model=model
        self.rental_price=price
        self.availability_status=available
    def check_availability(self):
        pass
    def rental_cost(self,r_cost):
        pass
    def display(self):
        print(f"Make: {self.make}\nModel: {self.model}\nPrice/Day: {self.rental_price}")


class Car(Vehicle):
    def __init__(self,make,model,price,available):
        super().__init__(make,model,price,available)
        self.rent_cost = None

    def check_availability(self):
        if self.availability_status:
            print("The Car is available for rent")
            self.availability_status=False
            return True
        else:
            print("The Car is not available for rent")
            return False
    def rental_cost(self,r_days):
        self.rent_cost=r_days*self.rental_price
        print(f"The total cost of rent is: {self.rent_cost}")
    def display(self):
        super().display()


class SUV(Vehicle):
    def __init__(self,make,model,price,available):
        super().__init__(make,model,price,available)
        self.rent_cost = None

    def check_availability(self):
        if self.availability_status:
            print("The SUV is available for rent")
            self.availability_status=False
            return True
        else:
            print("The SUV is not available for rent")
            return False
    def rental_cost(self,r_days):
        self.rent_cost=r_days*self.rental_price
        print(f"The total cost of rent is: {self.rent_cost}")
    def display(self):
        super().display()


class Truck(Vehicle):
    def __init__(self,make,model,price,available):
        super().__init__(make,model,price,available)
        self.rent_cost = None

    def check_availability(self):
        if self.availability_status:
            print("The Truck is available for rent")
            self.availability_status=False
            return True
        else:
            print("The Truck is not available for rent")
            return False
    def rental_cost(self,r_days):
        self.rent_cost=r_days*self.rental_price
        print(f"The total cost of rent is: {self.rent_cost}")
    def display(self):
        super().display()


class RentalReservation:
    def __init__(self,s_date,e_date,cus,vehicle,r_days):
        self.start_date=s_date
        self.end_date=e_date
        self.customer=cus
        self.vehicle=vehicle
        self.rental_days=r_days

    def display_rent(self):
        print(f"Rent Details:\nCustomer name: {self.customer.name}\nStarting date: {self.start_date}\nEnding date: {self.end_date}")
        if self.vehicle.availability_status:
            print(f"Vehicle Details: ")
            self.vehicle.display()
            self.vehicle.rental_cost(self.rental_days)
        else:
            print("The desired Vehicle wasn't available")

class Customer:
    def __init__(self,name,c_no,r_veh):
        self.name=name
        self.cus_number=c_no
        self.rented_vehicle=r_veh
    def display_cus(self):
        print(f"Customer's Details:\nName: {self.name}\nContact info: {self.cus_number}")
        if self.rented_vehicle.availability_status:
            print(f"Rented Vehicle: {self.rented_vehicle.model}")
        else:
            print(f"Rented Vehicle: None")
def display_details(veh):
    if isinstance(veh, Vehicle):
        print(veh.display())
    elif isinstance(veh, RentalReservation):
        print(veh.display_rent())



C1=Car("Toyota","Prius",679990,True)
S1=SUV("Toyota","bZ4X",567890,False)
T1=Truck("Toyota","Tacoma",489320,True)

Cus1=Customer("Sara","03-9988798-0",C1)
Cus2=Customer("Ali","03-7437349-3",S1)

Rent1=RentalReservation("1-10-2024","21-10-2024",Cus1,C1,20)
Rent2=RentalReservation("12-11-2024","27-11-2024",Cus2,S1,15)

print("\n")
Cus1.display_cus()
Rent1.display_rent()
print("\n")

Cus2.display_cus()
Rent2.display_rent()
print("\n")

C1.check_availability()
S1.check_availability()
T1.check_availability()

C1.check_availability()

print("\n")
display_details(C1)
display_details(Rent1)
