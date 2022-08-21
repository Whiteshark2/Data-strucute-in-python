from datetime import date
class Student:

    passingPercentage = 40

    def __init__(self,name,age = 4, percentage= 80):
        self.name = name
        self.age = age
        self.percentage = percentage

    @classmethod
    def frombirthyear(cls,name,year,percentage):
        return cls(name, date.today().year-year,percentage)

    def Studentdetails(self):
        print("Name =",self.name)
        print("Age = ",self.age)
        print("Percentage = ",self.percentage)

    def isPassed(self):
        if self.percentage > Student.passingPercentage:
            print("Student is passed")
        else:
            print("Student is failed")

    @staticmethod
    def welcometoschool():
        print("Welcome is School")

    @staticmethod
    def isTeen(age):
        return age>16

s1 = Student("Parikh")
s1 = Student.frombirthyear("Parikh",1996,70)
s1.Studentdetails()
s1.isPassed()

