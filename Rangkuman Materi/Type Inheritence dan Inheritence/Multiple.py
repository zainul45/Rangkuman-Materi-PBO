class person:
    def __init__(self):
        self.name=input("nama :")
    def display(self):
        print("\n\nName:", self.name)
class marks:
    def __init__(self):
        self.npm=input("NPM :")
        print("Nilai")
        self.math = int(input("Math :"))
        self.biology=int(input("Biologi :"))

    def display(self):
        print("NPM :",self.npm)
        print("Nilai :",self.math+self.biology)
class student(person,marks):
    def __init__(self):
        person.__init__(self)
        marks.__init__(self)

    def result(self):
        person.display(self)
        marks.display(self)

stu1= student()
stu2= student()
stu1.result()
stu2.result()
