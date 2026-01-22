# Student Information
student_name = "Adegoke David"
matric_number = "24/14173"

users = {}

def display_student_info():
    print("===================================")
    print("Login Authentication System")
    print(f"Name: {student_name}")
    print(f"Matric Number: {matric_number}")
    print("===================================\n")

def register_user():
    print("\n=== Register User ===")
    username = input("Enter username: ")

    if username in users:
        print("Username already exists.")
        return

    password = input("Enter password: ")
    users[username] = password
    print("Registration successful.")

def login_user():
    print("\n=== Login User ===")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login successful. Access granted.")
    else:
        print("Invalid username or password.")

def main_menu():
    display_student_info()

    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("System exiting...")
            break
        else:
            print("Invalid choice.\n")

main_menu()
