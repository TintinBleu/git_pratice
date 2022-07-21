class User:
    """docstring for user ."""

    def __init__(self, first_name, last_name,sex,age=None):
        self.first_name=first_name
        self.last_name=last_name
        self.sex=sex
        self.age=age
        self.login_attempts=0


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


    def increment_login_attempts(self):
        self.login_attempts +=1
        print(f"You have tried {self.login_attempts} times.")

    def reset_login_attempts(self):
        self.login_attempts=0
        print(f"Reset {self.login_attempts}")


class Admin(User):

    def __init__(self, first_name, last_name,sex):
        super().__init__(first_name,last_name,sex)



class Privileges:
    def __init__(self, p):
        self.p=p
        self.privileges = ["can add post","can delete post","can ban user"]
    def show_privileges(self):
        print(f"This admin {self.privileges[self.p]}. ")


admin01=Admin("james","bond","M")
admin01.describe_user()
privilege01=Privileges(1)
privilege01.show_privileges()



'''user01=User("james", "bond","m", 30)
user01.describe_user()
user01.greet_user()
user01.increment_login_attempts()
user01.reset_login_attempts()

user02=User("Mary","Carrie","f")
user02.describe_user()
user02.greet_user()
user02.increment_login_attempts()
user02.increment_login_attempts()

user02.reset_login_attempts()


user03=User("Lilian","Kala","f",45)
user03.describe_user()
user03.greet_user()
user03.increment_login_attempts()
user03.increment_login_attempts()
user03.increment_login_attempts()
user03.reset_login_attempts()'''
