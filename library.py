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

def searchcbook(query):
    found = False
    for p in booklist:
        if query == p["title"]:
            print (p)
        if query.lower() in p["title"].lower():
            print(f"Found: {p["title"]} -- {p["author"]} -- {p["status"]}")
            found = True
            
    if not found:
        print("No contacts matched your search.")
def main ():
    ui = """
    Library Database
    1. Add Book
    2. View All Books
    3. Search For A Book
    0. Exit
    """

    print (ui)
    print()
    choice = input("Choose a number to navigate or type in 'exit' to quit: ").strip()
    if choice == "1":
        print()
        addbook()

    elif choice == "2":
        print()
        allbooks()

    elif choice == "3":
        print()
        searchcbook()

    elif choice == "0":
        print()
        print("Goodbye!")
        
    else:
        print("Invalid Choice!")
main() 
