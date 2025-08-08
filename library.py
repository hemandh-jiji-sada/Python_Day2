def view_books(libman):
    if not libman:
        print("No books are added")
    else:
        print(libman)

def add_book(libman,detail):
    book = input("Enter the name of the book: ")
    author = input('Enter the name of author: ')
    copy = int(input('Enter the no. of copies: '))
    detail['Author'] = author
    detail['Copies'] = copy
    libman[book] = detail


def borrow_book(libman):
    bbook = input("Enter the book to borrow: ")
    libman[bbook]['Copies']+=1


def return_book(libman):
    rbook = input("Enter the book to return: ")
    libman[rbook]['Copies'] -= 1

def remove_book(libman):
    rb = input('Enter the book to return: ')
    libman.pop(rb)



def lib():
    libman = {}
    detail = {'Author':'','Copies':''}

    print('''** Options **
    1: View All Books
    2: Add New Book
    3: Borrow Book
    4: Return Book
    5: Remove Book
    6: Exit''')

    while True:
        option = int(input("Enter the option: "))
        if option == 1:
            view_books(libman)

        elif option == 2:
            add_book(libman,detail)

        elif option == 3:
            borrow_book(libman)

        elif option == 4:
            return_book(libman)

        elif option == 5:
            remove_book(libman)

        elif option == 6:
            print("Exiting the Library Management System...")
            break

        else:
            print("Invalid Choice")
            continue
lib()

