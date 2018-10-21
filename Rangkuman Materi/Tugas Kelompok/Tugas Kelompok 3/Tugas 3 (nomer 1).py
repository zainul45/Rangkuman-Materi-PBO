class user:
    def __init__(self, name):
        self.name = name
    def printname(self):
        print("name = " + self.name)
        
class programer(user):
    def __init__(self, firstname, lastname):
        self.lastname = lastname
        self.firstname = firstname
    def printlastname(self):
        print("first name = " + self.lastname)
    def printfirstname(self):
        print("last name = " + self.firstname)
    def dopython(self):
        print("programing python")
        
class programer1(user):
    pass 

User = user("brian")
User.printname()

Programer = programer1("diana")
Programer.printname()

dita = programer("dita","diana")
dita.printfirstname()
dita.printlastname()
dita.dopython()
