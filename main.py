passwords = []
def add_password():
    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")

    new_password = {
        "website" : website, "username" : username, "password": password
    }
    passwords.append(new_password)
    print("Password added successfully!")
def view_passwords():
    if len(passwords) == 0:
        print("No passwords saved.")
        return 
    for item in passwords:
        print("-----------")
        print("Website:", item["website"])
        print("Username:", item["username"])
        print("Password:", item["password"])

def search_passwords():
    website_search = input("\n enter the website to search")
    found = False
    for item in passwords:
        if item["website"].lower() == website_search.lower():
            print("Website:", item["website"])
            print("Username:", item["username"])
            print("Password:", item["password"])
            found = True
        if found == False:
            print("No password found.")
def show_menu():
    print("""
    PASSWORD MANAGER
    1. Add Password
    2. View Passwords
    3. Search Password
    4. Exit""")
while True:
    show_menu()
    choice = input("Choose option: ")
    if choice == "1":
        add_password()
    elif choice == '2':
        view_passwords()
    elif choice == '3':
        search_passwords()
    elif choice == '4':
        print('Goodbye!')
        break
    else:
        print('Invalis Choice')

