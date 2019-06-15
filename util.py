import bs4

def parse_table(header, rows):
    header = parse_table_row(header)
    print("Fetch %d records."%len(rows))

    ret_rows = []
    for row in rows:
        row = parse_table_row(row)
        assert (len(row) == len(header))
        ret_rows.append(row)

    return header, ret_rows

def parse_table_row(row):
    children = row.children
    children = list(children)
    return [''.join(child.text.split()) for child in children if type(child) == bs4.element.Tag]

def output(header, rows, filename="pollutions.txt"):
    filename = "output/"+filename 
    with open(filename, "w", encoding="utf-8") as file:
        file.write(" ".join(header) + "\n")
        for row in rows:
            file.write(" ".join(row) + "\n")

        print("Save pollution data to %s"%filename)

