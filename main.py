from ticket_manager import display, collection, dashboard

def menu():
    while True:
        print("\n===== Help Desk Ticket System =====")
        print("1. Display Tickets")
        print("2. Display Dashboard")
        print("0. Exit")

        choice = input("Enter your choice: ")
        data = collection()
        
        if choice == "1":
            display(data)
        if choice == "2":
            dashboard(data)
        if choice == "0":
            return
menu()