"""  Leo Quezada
     Program #4: The Phonebook program
"""

def printMenu(): #DONE, print's menu
    print("1. Print Contact List\n2. Add New Contact\n3. Delete Contact\n4. Modify Contact\n5. Exit")

def readFromFile(filename): #DONE, reads file
    file = open(filename, "r")
    contacts = file.read()
    people = contacts.split("\n")
    global newArray
    newArray = [] 
    for i in range(len(people)):
        newArray.append(people[i].split())
    return newArray

def printContactList(contactList): #DONE, prints contact list
    for i in range(len(contactList)):
        print("Contact #", i+1)
        print("First name:", contactList[i][0] + ", Last name:", contactList[i][1] + ", Phone number:", contactList[i][2]+ ", Birthday:", contactList[i][3])

def addContact(newArray): #DONE, this function receives as a parameter the list of contacts, adds contact, and does not return any value. 
    first = input("Enter the First Name: ")
    last = input("Enter the Last Name: ")
    number = input("Enter the Phone Number: ")
    birthday = input("Enter the Birthday: ")
    newPerson = [first, last, number, birthday]
    newArray.append(newPerson)

def deleteContact(newArray): #DONE, this function receives as a parameter the list of contacts, deletes contact, and does not return any value. 
    contactIndex = int(input("Select the contact to be deleted: "))
    if contactIndex < 1 or contactIndex > 4:
        print("Incorrect contact number")
    else:
        newArray.remove(newArray[contactIndex-1])
        print("Contact", contactIndex, "deleted")

def modifyContact(newArray): #DONE, this function receives as a parameter the list of contacts, modifies contact, and does not return any value. 
    person = int(input("Select the contact to be changed: "))
    first = input("Enter the First Name: ")
    last = input("Enter the Last Name: ")
    number = input("Enter the Phone Number: ")
    birthday = input("Enter the Birthday: ")
    newArray[person-1] = [first, last, number, birthday]
    print("Contact", person, "was changed")

###################################
filename = input("Enter the file name: ")
contactList = readFromFile(filename)
menuOption = 0
while menuOption != 5:
    printMenu()
    menuOption = int(input("Enter your option: "))
    if menuOption == 1:
        printContactList(contactList)
    elif menuOption == 2:
        addContact(contactList)
    elif menuOption == 3:
        deleteContact(contactList)
    elif menuOption == 4:
        modifyContact(contactList)
    elif menuOption != 5:
        print("Invalid option")
