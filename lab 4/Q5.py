class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.booked_tables = []
        self.customer_orders = {}

    def add_item_to_menu(self, item, price):
        self.menu_items[item] = price

    def book_table(self, table_number):
        if table_number in self.booked_tables:
            print(f"Table {table_number} is already booked")
        else:
            self.booked_tables.append(table_number)
            self.customer_orders[table_number] = []

    def customer_order(self, table_number, item):
        if table_number not in self.customer_orders:
            self.customer_orders[table_number] = []
        self.customer_orders[table_number].append(item)

    def print_menu(self):
        if not self.menu_items:
            print("Menu is empty")
        else:
            print("Menu:")
            for item_name, price in self.menu_items.items():
                print(f"{item_name}: {price: }")

    def print_table_reservations(self):
        if not self.booked_tables:
            print("No tables are booked.")
        else:
            print("Booked Tables:")
            for table_number in self.booked_tables:
                print(f"Table {table_number}")

    def print_customer_orders(self):
        if not self.customer_orders:
            print("No customer orders.")
        else:
            print("Customer Orders:")
            for table_number, orders in self.customer_orders.items():
                print(f"Table {table_number}: {', '.join(orders)}")


R1 = Restaurant()

R1.add_item_to_menu("Burger", 300)
R1.add_item_to_menu("Pizza", 500)
R1.add_item_to_menu("Biryani", 350)

R1.book_table(1)
R1.book_table(2)

R1.customer_order(1, "Burger")
R1.customer_order(1, "Pizza")
R1.customer_order(2, "Biryani")
R1.customer_order(3, "Burger")

R1.book_table(2)

R1.print_menu()
R1.print_table_reservations()
R1.print_customer_orders()
