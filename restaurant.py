class Restaurant:
    def __init__(self,name,type):
        self.name=name
        self.type=type


    def describe_restaurant(self):
        print(f"This is {self.name} restaurant, a {self.type} food restaurant.")


    def open_restaurant(self):
        print(f"{self.name} restaurant is open, welcome!")
