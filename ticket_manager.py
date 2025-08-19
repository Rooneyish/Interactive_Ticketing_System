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
            if i < len(row):
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