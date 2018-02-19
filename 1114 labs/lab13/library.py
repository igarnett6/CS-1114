import random
class Library:
    def __init__(self):
        self.available = {}
        self.patrons = {}

    def addBook(self, name):
        self.available[name] = "Available"

    def addPatron(self, name):
        patronExists = False
        for key in self.patrons:
            if patrons[key] == name:
                patronExists = True
        if  (patronExists == False):
            keyGen = genActNum()
            while keyGen in self.patrons:
                keyGen = genActNum()
            self.patrons[keyGen] = name
            print("Account created for: " + name)

        else:
            print("Patron already has an account")

    def checkOut(self, name):
        if name in self.patrons:
            if(self.available[name] == "Available"):
                self.available[name] = "Unavailable"
            else:
                print(name + "is currently unavailable for check-out")
        else:
            print("The account does not exist")

def genActNum(self, patrons):
       number = random.randint((10 ** 4), ((10 ** 4) - 1))
       return number

class Patron:
   def __init__(self, name):
       self.name = name
       self.booklist = []





def main():
    response = ""
    while (response != "4"):
        response = input("1. create account\n2. checkout\n3. Return book\n4. quit")
        if(response == "1"):
            name = input("Enter a name: ")
            Library.addPatron(name)
        elif(response =="2"):
            title = input("Enter the title of the book: ")
            Library.checkOut(title)
        elif(response == "3"):
            title = input("Enter the title of the book: ")
            Library.addBook(title)
        else:
            print("Invalid Response")
main()