import json

masterPassword = input("Master Password: ") #add password generator and password rules

for i in range(2):
    if masterPassword == "example":
        break

    elif masterPassword != "example":
        print("Wrong Password. Please try again.")
        masterPassword = input("Master Password: ")

        if i == 1 and masterPassword != "example":
            exit()


response = 0

try:
    with open("passwords.json", "r") as file:
        passwords = json.load(file)

except FileNotFoundError:
    passwords = []

while response != 5:

    print("\nWelcome to Password Manager!")
    print(" 1. Add Password")
    print(" 2. Remove Password")
    print(" 3. Change Password")
    print(" 4. View Passwords")
    print(" 5. Exit")

    while True:
            try:
                response = int(input("\nEnter your choice: "))

                if 1 <= response <= 5:
                    break

                print("\nSelection not available")
                print("Please select a valid option")

            except ValueError:
                print("\nPlease enter a number between 1 and 5.")

    if response == 1:
        web = input("Website/Company: ")
        user = input("Username: ")
        pword = input("Password: ")

        while len(pword) < 6:
            print("\nPassword too short")
            print("Please try again.")

            pword = input("Password: ")


        entry = [web, user, pword]
        passwords.append(entry)

        print("Password added.")


    elif response == 2:
        print("\nWhich would you like to remove?")

        for i in range(len(passwords)):
            print(i + 1, passwords[i])

        erase = int(input("Remove: ")) - 1 #add if incase input does not match index
        passwords.remove(passwords[erase])

        print("Removed.")

    elif response == 3:
        print("\nWhich would you like to change?")

        for i in range(len(passwords)):
            print(i + 1, passwords[i])

        swap = int(input("Change: ")) - 1

        web = input("Website/Company: ")
        user = input("Username: ")
        pword = input("Password: ")

        while len(pword) < 6:
            print("\nPassword too short")
            print("Please try again.")

            pword = input("Password: ")

        passwords[swap] = [web,user,pword]

        print("Password changed.")

    elif response == 4:
        print("\nHere are all your passwords:") #clean up viewer

        if len(passwords) == 0:
            print("No passwords saved.")

        else:
            for i in range(len(passwords)):
                print("Entry:", i + 1)
                print("Website:", passwords[i][0])
                print("Username:", passwords[i][1])
                print("Password:", passwords[i][2])

    elif response == 5:
        with open("passwords.json", "w") as file:
            json.dump(passwords, file)

        print("Exiting...")


