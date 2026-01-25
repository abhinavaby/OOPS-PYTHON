#methods that dont use self parameter
class student:
    @staticmethod #decorator
    def welcome():
        print("welcome")
s1=student
s1.welcome()
