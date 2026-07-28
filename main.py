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
    for i in passwords:
        print("-----------")
        print("Website:", i["website"])
        print("Username:", i["username"])
        print("Password:", i["password"])
def show_menu():
    print("""
    PASSWORD MANAGER
    1. Add Password
    2. View Passwords
    3. Exit""")
while True:
    show_menu()
    choice = input("Choose option: ")
    if choice == "1":
        add_password()
    elif choice == '2':
        view_passwords()
    elif choice == '3':
        print('Goodbye!')
        break
    else:
        print('Invalis Choice')
        