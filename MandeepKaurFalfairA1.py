""" IT@JCU CP1404 Assignment 1 from SP2 2016
    Shopping List
    Mandeep Kaur Falfair
    09/09/2016
"""


MENU = "Menu:\nR - List required items\nC - List completed items\nA - Add new item\nM - Mark an item as completed\nQ - Quit"
REQUIRED = 'r'
COMPLETED = 'c'


def main():
    # define shoping list with required item, add new items, completed items and mark items
    print("Shopping List 1.0 - by Mandeep Kaur Falfair")
    items = readList()
    print(MENU)
    choice = input(">>>").upper()
    while choice != 'Q':
        if choice == 'R':
            count = 0
            for item in items:
                if item[3] == REQUIRED:
                    count = count + 1
            if count == 0:
                print("No required items")
            else:
                print("Required items")
                list_items(items, REQUIRED)
        elif choice == 'C':
            count = 0
            for item in items:
                if item[3] == COMPLETED:
                    count = count + 1
            if count == 0:
                print("No completed items")
            else:
                print("Completed items")
                list_items(items, COMPLETED)
        elif choice == 'A':
            items = add_new_item(items)
        elif choice == 'M':
            mark_item_list(items)
        else:
            print("Invalid menu choice")

        print(MENU)
        choice = input('>>>').upper()
    output_file = open("items.csv", "w")
    for item in items:
        print("{},{},{},{}".format(item[0], item[1], item[2], item[3]), file=output_file)

    output_file.close()
    print("{} items saved to items.csv".format(len(items)))
    print("Have a nice day :)")


"""
function readlist()
    create items as an empty list
    open file for reading
    for each line in file
        read name,price, and priority from file
        append name, price and priority to items with status 'r'
    close file
    print number of items read to screen
    return list of items
"""
def readList():
    #load items in file for find completed items and required items
    items = []
    inFile = open('items.csv', 'r')
    for line in inFile:
        name, price, priority, status = line.strip().split(',')
        items.append([name, float(price), int(priority), status])

    inFile.close()
    print("{} items read from items.csv".format(len(items)))
    return items


def list_items(item_list, status):
    from operator import itemgetter

    item_list.sort(key=itemgetter(2, 0))

    count = 0
    total = 0

    for item in item_list:
        if item[3] == status:
            print("{}. {:20} ${:.2f} ({})".format(count, item[0], item[1], item[2]))
            total += item[1]
            count = count + 1

    print("Total expected price for {} items: ${:.2f}".format(count, total))
    return count


def add_new_item(items_list):
    """get add new items by using exceptions to control error handling"""
    item_name = input("Enter new item name:")
    while item_name == "" or item_name.isspace():
        print("Name cannot be blank")
        item_name = input("Enter new item name:")

    valid_price = False
    while not valid_price:
        try:
            item_price = float(input("Enter new item price"))
            if item_price <= 0:
                print("Price must be >= $0")
            else:
                valid_price = True
        except ValueError:
            print("Invalid input; enter a valid number")

    valid_priority = False
    while not valid_priority:
        try:
            item_priority = int(input("Enter item priority"))
            if item_priority not in [1, 2, 3]:
                print("Priority must be 1, 2 or 3")
            else:
                valid_priority = True
        except ValueError:
            print("Invalid input; enter a valid numnber")

    items_list.append([item_name, item_price, item_priority, 'r'])
    return items_list


"""
function mark_item_list()
    num_required = list item
    valid_item = False
    while is not valid_item
        get completed item
        if completed_item less than 0 or completed_item is gratter than num_required
            display invalid item number
        else
            valid item = True
        except value error
            display invalid input; enter a number
"""
def mark_item_list(items):
    """get completed list of items and try error handling using exceptional for mark list"""
    num_required = list_items(items, REQUIRED)

    valid_item = False
    while not valid_item:
        try:
            completed_item = int(input("Enter mark completed items"))
            if completed_item < 0 or completed_item >= num_required:
                print("Invalid item number")
            else:
                valid_item = True
        except ValueError:
            print("Invalid input; enter a number")

    current_required_item = 0
    for item in items:
        if item[3] == 'r':
            if current_required_item == completed_item:
                item[3] = 'c'
            current_required_item = current_required_item + 1


main()
