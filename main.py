from ticket_manager import display

def menu():
    while True:
        print("\n===== Help Desk Ticket System =====")
        print("1. Display Tickets")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display()
        if choice == "0":
            return
menu()