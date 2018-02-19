class Person:
    name = ""
    age = ""
    hobbies = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hobbies = []
    def addHobby(self, newHobby):
        self.hobbies.append(newHobby)
    def deleteHobby(self, oldHobby):
        delIndex = self.hobbies.index(oldHobby)
        self.hobbies.pop(delIndex)
    def incrementAge(self):
        self.age = str(int(self.age) + 1)
    def __repr__(self):
        output = ""
        output += ("Name: " + self.name)
        output +=("\nAge: " + self.age)
        output +=("\nHobbies: ")
        for i in range(len(self.hobbies)):
            output += "\n" + (self.hobbies[i])
        return output

def main():
    people = {}  #keys: value where key = name value = person object
    exit = False
    while(exit == False):
        print("1. Create a new Person")
        print("2. Add to an existing person's hobbies")
        print("3. Delete an existing person's hobby")
        print("4. Someone has a birthday")
        print("5. See a list of people")
        print("6. Exit")
        response = input()
        name = ""
        if(response == '1'):
            name = input("Please enter the name: ")
            age = input("Please enter the age: ")
            people[name] = Person(name, age)
        elif(response == '2'):
            name = input("Who is receiving a new hobby?")
            newHobby = input("What is this person's new hobby?")
            people[name].addHobby(newHobby)
        elif(response == '3'):
            name = input("Who is losing a hobby?")
            oldHobby = input("What hoby are you deleting?")
            people[name].deleteHobby(oldHobby)
        elif(response == '4'):
            name = input("Who is having a birthday?")
            print("Happy birthday, " + name + "!")
            people[name].incrementAge()
        elif(response == '5'):
            for key in people:
               print("\n\n" + repr(people[key]))
        elif(response == '6'):
            exit = True
        else:
            print("Invalid response")

main()