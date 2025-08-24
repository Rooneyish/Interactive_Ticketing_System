from ticket_manager import display, collection, dashboard, add_tickets, update_ticket, delete_ticket

def menu():
    while True:
        print("\n===== Help Desk Ticket System =====")
        print("1. Display Tickets")
        print("2. Display Dashboard")
        print("3. Add new Ticket")
        print("4. Update Ticket")
        print("5. Delete Ticket")
        print("0. Exit")

        choice = input("Enter your choice: ")
        data = collection()
        
        if choice == "1":
            display(data)
        if choice == "2":
            dashboard(data)
        if choice == "3":
            add_tickets()
        if choice == "4":  
            while True:
                ticket_id = input("Enter the Ticket ID to Update: ").strip()
                if ticket_id == "":
                    print("Ticket ID cannot be empty. Try again.")
                elif not ticket_id.isdigit():
                    print("Ticket ID must be a number. Try again.")
                else:
                    update_ticket(ticket_id)
                    break
        if choice == "5":  
            while True:
                ticket_id = input("Enter the Ticket ID to Delete: ").strip()
                if ticket_id == "":
                    print("Ticket ID cannot be empty. Try again.")
                elif not ticket_id.isdigit():
                    print("Ticket ID must be a number. Try again.")
                else:
                    delete_ticket(ticket_id)
                    break


        if choice == "0":
            return
menu()