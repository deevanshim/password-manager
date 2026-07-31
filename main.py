def add_password():
    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")

    new_password = {
        "website" : website, "username" : username, "password": password
    }
    passwords.append(new_password)
    save_passwords(passwords)
    print('password added successfully')
	
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

def delete_passwords():
	to_delete = input("enter website name to delete")
	found = False
	for i in passwords:
		if i['website'].lower() == to_delete.lower():
			passwords.remove(i)
			save_passwords(passwords)
			print('The password has been deleted')
			found = True
			break
	if found == False:
		print('No password found.')

def update_password():
	to_update = input('enter website to update')
	found = False
	for i in passwords:
		if to_update.lower() == i['website'].lower():
			new = input('enter new pass')
			i['password'] = new
			save_passwords(passwords)
			print('your password has been updated')
			found = True
			break
	if found == False:
		print('No password found.')

import json
def load_passwords():
	try:
		f = open('passwords.json' , 'r')
		passwords = json.load(f)
		f.close()
	except FileNotFoundError:
		return []
	return passwords

def save_passwords(passwords):
	f = open('passwords.json' , 'w')
	json.dump(passwords, f, indent = 4)
	f.close()


passwords = load_passwords()




def show_menu():
    print("""
    PASSWORD MANAGER
    1. Add Password
    2. View Passwords
    3. Search Password
    4. Update Password
    5. Delete Password
    6. Exit
    """)
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
        update_password()
    elif choice == '5':
        delete_passwords()
    elif choice == '6':
        print('Goodbye!')
        break
    else:
        print('Invalis Choice')

