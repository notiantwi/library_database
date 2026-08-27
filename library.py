booklist = []
def addbook ():
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    status = "Available"
    booklist.append({"title":title, "author":author, "status":status})
    print (f"{title} added successfully!")

def allbooks ():
    for index, c in enumerate(booklist, start=1):  
       print (f"{index}. {c["title"]}--{c["author"]}--{c["status"]}")

def main ():
    ui = """
    Library Database
    1. Add Book
    2. View All Books
    """

    print (ui)
    print()
    choice = input("Choose a number to navigate or type in 'exit' to quit: ").lower().strip()
    if choice == "1":
        print()
        addbook()
    elif choice == "2":
        print()
        allbooks()
    elif choice == "exit":
        print()
        print("Goodbye!")
    else:
        print("Invalid Choice!")
main() 
