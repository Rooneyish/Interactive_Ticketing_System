def display():
    file = open("tickets.txt", "r")
    table = [line.strip().split(",") for line in file]
    file.close()

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

