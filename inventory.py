def view_books(inventory):
    if not inventory:
        print("Inventory Empty")
    else:
        print(inventory)

def add_book(inventory,detail):
    product = input("Enter the name of the product: ")
    quantity = input('Enter the quantity: ')
    price = int(input('Enter the price: '))
    detail[0] = quantity
    detail[1] = price
    inventory[product] = detail


def borrow_book(inventory):
    bbook = input("Enter the book to borrow: ")
    inventory[bbook]['Copies']+=1


def return_book(inventory):
    rproduct = input("Enter the product to remove: ")
    inventory.pop(rproduct)


def remove_book(inventory):
    rb = input('Enter the book to return: ')
    inventory.pop(rb)



def inv():
    inventory = {}
    detail = []

    print('''** Options **
    1: View Inventory
    2: Add Product
    3: Remove Product
    4: Update Product
    5: Calculate Total Value
    6: Exit''')

    while True:
        option = int(input("Enter the option: "))
        if option == 1:
            view_books(inventory)

        elif option == 2:
            add_book(inventory,detail)

        elif option == 3:
            borrow_book(inventory)

        elif option == 4:
            return_book(inventory)

        elif option == 5:
            remove_book(inventory)

        elif option == 6:
            print("Exiting the Library Management System...")
            break

        else:
            print("Invalid Choice")
            continue
inv()

