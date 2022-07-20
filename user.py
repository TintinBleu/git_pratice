class User:
    """docstring for user ."""

    def __init__(self, first_name, last_name,sex,age=None):
        self.first_name=first_name
        self.last_name=last_name
        self.sex=sex
        self.age=age


    def describe_user(self):
        if self.age:
            if self.sex in ['m','M','Male','male']:
                print(f"This is Mr.{self.first_name.title()} {self.last_name.title()}. He is {self.age} years old.")
            else:
                print(f"This is Ms.{self.first_name.title()} {self.last_name.title()}. She is {self.age} years old.")

        else:
            if self.sex in ['m','M','Male','male']:
                print(f"This is Mr.{self.first_name.title()} {self.last_name.title()}. ")
            else:
                print(f"This is Ms.{self.first_name.title()} {self.last_name.title()}. ")


    def greet_user(self):
        if self.sex in ['m','M','Male','male']:
            print(f"Welcome Mr.{self.first_name.title()} {self.last_name.title()}.")
        else:
            print(f"Welcome Ms.{self.first_name.title()} {self.last_name.title()}.")


user01=User("james", "bond","m", 30)
user01.describe_user()
user01.greet_user()

user02=User("Mary","Carrie","f")
user02.describe_user()
user02.greet_user()

user03=User("Lilian","Kala","f",45)
user03.describe_user()
user03.greet_user()