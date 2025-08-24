def display(table):
    columns = list(zip(*table))
    col_widths =[]
    for col in columns:
        max_len = max(len(item) for item in col)
        col_widths.append(max_len)

    for row in table:
        line = "| "
        for i, item in enumerate(row):
            line += "{:<{width}}".format(item, width = col_widths[i])
            if i < len(row)-1:
                line += " | "
        print(line)

def collection():
    file = open("tickets.txt", "r")
    dataList = []
    for eachLine in file:
        eachLine = eachLine.strip().split(",")
        dataList.append(eachLine)
    file.close()
    return dataList

def dashboard(data):
    status_counts = {"open": 0, "closed": 0}
    priority_counts = {"low": 0, "medium":  0, "high": 0}

    for row in data[1:]:
        status = row[2].lower()
        priority = row[3].lower()

        if status in status_counts:
            status_counts[status] += 1
        if priority in priority_counts:
            priority_counts[priority] += 1
        
    print("\n Ticket Analytics Dashboard")
    print("="*40)
    print("Ticket Status:")
    for status, count in status_counts.items():
        print(f"  {status.capitalize():<7}: {count}")

    print("\nPriority Levels:")
    for priority, count in priority_counts.items():
        print(f"  {priority.capitalize():<7}: {count}")
    print("="*40)

def add_tickets():
    table = collection()

    exiting_ids = [int(row[0]) for row in table[1:]]

    new_id = max(exiting_ids) + 1 if exiting_ids else 1

    while True:
        title = input("Enter Title: ")
        if title == "":
            print("Title cannot be empty.")
        else: 
            break
    
    while True:
        status = input("Enter Status ('o' for  open/'c' for closed): ").lower()
        if status not in ["o", "c"]:
            print("Invalid status. Enter 'o' or 'c'")
        else:
            status = "open" if status == "o" else "closed"
            break
    
    while True:
        priority = input("Enter Priority ('l' for low/ 'm' for medium/'h' for high): ").lower()
        if priority not in ["l", "m", "h"]:
            print("Invalid priority. Enter 'l', 'm' or 'h'")
        else: 
            priority = "low" if priority == "l" else "medium" if priority == 'm' else 'high'
            break
    
    file = open("tickets.txt", 'a')
    file.write(f"\n{new_id},{title},{status},{priority}")
    file.close()

    print("Ticket added successfully!")

def delete_ticket(ticket_id):
    ticket_id = str(ticket_id).strip()

    table = collection()
    if not table:
        print("No data found.")
        return False
    
    header = table[0]
    found = False
    kept_rows = [header]

    for row in table[1:]:
        if len(row) == 0:
            continue
        
        if row[0].strip() == ticket_id:
            found = True
            continue
        
        kept_rows.append(row)
    
    if not found:
        print(f'Ticket {ticket_id} not found.')
        return False
    
    file = open('tickets.txt', 'w')
    for row in kept_rows:
        file.write(",".join(row)+"\n")

    print(f'Ticket {ticket_id} deleted successfully.')
    return True

def update_ticket(ticket_id):
    ticket_id = str(ticket_id).strip()

    table = collection()
    updated = False

    for row in table:
        if len(row) > 0 and row[0] == ticket_id:
            print("Current Ticket Details: \n")
            print(row)

            while True:
                new_description = input(f"Enter new description (current: {row[1]}): \n").lower().strip()
                if new_description == "":
                    new_description = row[1]
                    break
                else:
                    break
            
            while True:
                new_priority = input(f"Enter new priority (current: {row[3]}) [l/m/h]: \n").lower().strip()
                if new_priority == "":
                    new_priority = row[3]
                    break
                elif new_priority not in ["l", "m", "h"]:
                    print("Invalid priority. Enter 'l', 'm' or 'h'")
                else:
                    new_priority = "low" if new_priority == "l" else "medium" if new_priority == "m" else "high"
                    break

            while True:
                new_status = input(f"Enter new status (current: {row[2]}) [o/c]: ").lower().strip()
                if new_status == "":
                    new_status = row[2]
                    break
                elif new_status not in ["o", "c"]:
                    print("Invalid status. Enter 'o' or 'c'")
                else:
                    new_status = "open" if new_status == "o" else "closed"
                    break

            if new_description.strip():
                row[1]= new_description
            if new_priority.strip():
                row[3]= new_priority
            if new_status.strip():
                row[2]= new_status
            
            updated = True
            break

    if updated:
        file = open('tickets.txt', 'w')
        for row in table:
            file.write(",".join(row)+"\n")
        print("Ticket Updated Successfully.")
    else:
        print("Ticket not found.")
    
    return updated

update_ticket(4)