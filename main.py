from ticket_manager import display, collection, dashboard,history_list,display_history, add_tickets, undo_last_action, update_ticket, delete_ticket, process_next_ticket

def menu():
    while True:
        print("\n===== Help Desk Ticket System =====")
        print("1. Display Tickets")
        print("2. Display Dashboard")
        print("3. Add new Ticket")
        print("4. Update Ticket")
        print("5. Delete Ticket")
        print("6. Process Next Ticket")
        print("7. Undo Last Action")
        print("8. History")
        print("0. Exit")

        choice = input("Enter your choice: ")
        data = collection()
        
        if choice == "1":
            display(data)
        elif choice == "2":
            dashboard(data)
        elif choice == "3":
            add_tickets()
        elif choice == "4":  
            while True:
                ticket_id = input("Enter the Ticket ID to Update: ").strip()
                if ticket_id == "":
                    print("Ticket ID cannot be empty. Try again.")
                elif not ticket_id.isdigit():
                    print("Ticket ID must be a number. Try again.")
                else:
                    update_ticket(int(ticket_id))
                    break
        elif choice == "5":  
            while True:
                ticket_id = input("Enter the Ticket ID to Delete: ").strip()
                if ticket_id == "":
                    print("Ticket ID cannot be empty. Try again.")
                elif not ticket_id.isdigit():
                    print("Ticket ID must be a number. Try again.")
                else:
                    delete_ticket(int(ticket_id))
                    break
        elif choice =="6":
            process_next_ticket()
        elif choice == "7":
            undo_last_action()
        elif choice == "8":
            display_history(history_list)
        elif choice == "0":
            print("Exiting Help Desk Ticket System. \n")
            print("System Logged Out. Thank You!!")
            return
        else:
            print("Invalid Choice. Please Try Again!")

if __name__ == "__main__":
    menu()