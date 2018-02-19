def add_entry(phonebook, name, phoneNumber):
    if name not in phonebook:
        if(checkNumberValid(phoneNumber):
            phonebook[name] = phoneNumber
        else:
            print("Entry could not be added: Invalid Phone Number.")
    else:
        print("Entry for " + name + ": " + phonebook[name] + " could not be added: Name already exists within phone book.")

def checkNumberValid(phoneNumber):
    if (len(phoneNumber)==10 and phoneNumber.isnumeric() == True):
        return True
    else:
        return False

def lookup(phonebook, name):
    return phonebook[name]

def print_all(phonebook):
    for key in phonebook:
        print(key + ": " + phonebook[key])

def main():
    phonebook = {}
    file = open("Lab 13 - phonebook.txt", "r")
    for line in file:
        currentLine = file.readline()
        cLineList = currentLine.split(" ")
        name = cLineList[1]
        phoneNumber = cLineList[2].rstrip()
        add_entry(phonebook, name, phoneNumber)
    while(name != "quit"):
        name = input("Enter a name to lookup: ")
        if (name != "quit"):
            number = lookup(phonebook, name)
            print("Results for: " + name + ": " + "\n" + name + ": " + number)

    print_all(phonebook)

main()