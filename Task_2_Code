import sys

def initial_phonebook():
    rows, cols = int(input("Please enter initial number of contacts: ")), 5
    phone_book = []

    for _ in range(rows):
        print(f"\nEnter contact {_+1} details in the following order (ONLY):")
        print("NOTE: * indicates mandatory fields")
        print("....................................................................")
        temp = []
        for j in range(cols):
            if j == 0:
                temp.append(input("Enter name*: "))
                if not temp[j].strip():
                    sys.exit("Name is a mandatory field. Process exiting due to blank field...")
            elif j == 1:
                temp.append(int(input("Enter number*: ")))
            elif j == 2:
                temp.append(input("Enter e-mail address: ") or None)
            elif j == 3:
                temp.append(input("Enter date of birth(dd/mm/yy): ") or None)
            elif j == 4:
                temp.append(input("Enter category(Family/Friends/Work/Others): ") or None)
        phone_book.append(temp)
    return phone_book

def menu():
    print("********************************************************************")
    print("\t\t\tSMARTPHONE DIRECTORY")
    print("********************************************************************")
    print("\tYou can now perform the following operations on this phonebook\n")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit phonebook")
    choice = int(input("Please enter your choice: "))
    return choice

def add_contact(pb):
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(input("Enter name: "))
        elif i == 1:
            dip.append(int(input("Enter number: ")))
        elif i == 2:
            dip.append(input("Enter e-mail address: "))
        elif i == 3:
            dip.append(input("Enter date of birth(dd/mm/yy): "))
        elif i == 4:
            dip.append(input("Enter category(Family/Friends/Work/Others): "))
    pb.append(dip)
    return pb

def remove_existing(pb):
    query = input("Please enter the name of the contact you wish to remove: ")
    temp = 0
    for i in range(len(pb)):
        if query == pb[i][0]:
            temp += 1
            print(pb.pop(i))
            print("This query has now been removed")
            return pb
    if temp == 0:
        print("Sorry, you have entered an invalid query. Please recheck and try again later.")
        return pb

def delete_all(pb):
    return pb.clear()

def search_existing(pb):
    choice = int(input("Enter search criteria\n\n1. Name\n2. Number\n3. Email-id\n4. DOB\n5. Category(Family/Friends/Work/Others)\nPlease enter: "))
    temp = []
    check = -1

    if choice in range(1, 6):
        query = input(f"Please enter the {choice_map[choice]} of the contact you wish to search: ")
        for contact in pb:
            if query == contact[choice - 1]:
                check = pb.index(contact)
                temp.append(contact)
    else:
        print("Invalid search criteria")
        return -1

    if check == -1:
        return -1
    else:
        display_all(temp)
        return check

def display_all(pb):
    if not pb:
        print("List is empty: []")
    else:
        for contact in pb:
            print(contact)

def thanks():
    print("********************************************************************")
    print("Thank you for using our Smartphone directory system.")
    print("Please visit again!")
    print("********************************************************************")
    sys.exit("Goodbye, have a nice day ahead!")

choice_map = {
    1: "name",
    2: "number",
    3: "e-mail ID",
    4: "DOB",
    5: "category"
}

print("....................................................................")
print("Hello dear user, welcome to our smartphone directory system")
print("You may now proceed to explore this directory")
print("....................................................................")

ch = 1
pb = initial_phonebook()
while ch in (1, 2, 3, 4, 5):
    ch = menu()
    if ch == 1:
        pb = add_contact(pb)
    elif ch == 2:
        pb = remove_existing(pb)
    elif ch == 3:
        pb = delete_all(pb)
    elif ch == 4:
        d = search_existing(pb)
        if d == -1:
            print("The contact does not exist. Please try again")
    elif ch == 5:
        display_all(pb)
    else:
        thanks()

