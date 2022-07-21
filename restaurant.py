class Restaurant:
    def __init__(self,name,type):
        self.name=name
        self.type=type
        self.number_served=0
        self.number_update=0


    def describe_restaurant(self):
        print(f"This is {self.name} restaurant, a {self.type} food restaurant.")


    def open_restaurant(self):
        print(f"{self.name} restaurant is open, welcome!")


    def number_clients(self):
        print(f"They served already {self.number_served} people.")

    def update_number(self, update):
        self.number_update=update
        print(f"They served already {self.number_update} people.")


    def increment_number_served(self,number):
        self.number_update +=number
        print(f"They served already {self.number_update} people.")
