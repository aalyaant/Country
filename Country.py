#Alyce Gaines
#CSI261
#Country

FILENAME = "the country list program"

def display_menu():
    print("command menu")
    print()
    print("view - view country name")
    print("add - add a country")
    print("del - delete a country")
    print("exit - exit program")
    print()

def display_codes(countries):
    codes = list(countries.keys())
    codes.sort()
    codes_line = "Country codes: "
    for code in codes:
        codes_line += code + " "
    print(codes_line)

def view(countries):
    display_codes(countries)
    code = input("enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"country name: {name}.\n")
    else:
        print("invalid country code.\n")

def add(countries):
    code = input("enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"{name} is already in use.\n")
    else:
        name = input("enter country name: ")
        name = name.title()
        countries[code] = name
        print(f"{name} was added.\n")

def delete(countries):
    code = input("enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries.pop(code)
        print(f"{name} was deleted.\n")
    else:
        print("invalid country code.\n")

def main():
    countries = {"CG": "Republic of the Congo",
                 "EG": "Egypt",
                 "SD": "Sudan"}
    
    display_menu()
    while True:        
        command = input("Command: ")
        command = command.lower()
        if command == "view":
            view(countries)   
        elif command == "add":
            add(countries)
        elif command == "del":
            delete(countries)  
        elif command == "exit":
            print("sayonora!")
            break
        else:
            print("invalid. try again.\n")


if __name__ == "__main__":
    main()