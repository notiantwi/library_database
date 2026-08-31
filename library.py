booklist = []

def addbook ():
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    status = "Available"
    booklist.append({"title":title, "author":author, "status":status})
    print (f"{title} added successfully!")

def allbooks ():
    if not booklist:
        print("The booklist is empty.")
        return
    for index, c in enumerate(booklist, start=1):  
        print (f"{index}. {c['title']}--{c['author']}--{c['status']}")
       

def searchbook():
    if not booklist:
        print("The booklist is empty. Nothing to search.")
        return
        
    query = input("Enter the title to search for: ").strip()
    found = False
    for p in booklist:
        if query.lower() in p["title"].lower():
            print(f"Found: {p['title']} -- {p['author']} -- {p['status']}")
            found = True
            
    if not found:
        print("No books matched your search.")

def borrowbook():
    if not booklist:
        print(" The booklist is empty. No books to borrow.")
        return

    title_to_borrow = input("Enter the exact title of the book you want to borrow: ").strip().lower()
    
    for book in booklist:
        if book["title"].lower() == title_to_borrow:
            
            if book["status"] == "Available":
                book["status"] = "Borrowed"
                print(f" You have successfully borrowed '{book['title']}'!")
                return
            else:
                print(f" '{book['title']}' is already borrowed.")
                return
                
    print(" That book is not in the booklist.")

def returnbook():
    if not booklist:
        print(" The booklist is empty. No books to return.")
        return

    title_to_return = input("Enter the exact title of the book you want to return: ").strip().lower()
    
    for book in booklist:
        if book["title"].lower() == title_to_return:
            
            if book["status"] == "Borrowed":
                book["status"] = "Available"
                print(f" You have successfully returned '{book['title']}'!")
                return
            else:
                print(f" '{book['title']}' is already available.")
                return
   
            
def main ():
    ui = """
    Library Database
    1. Add Book
    2. View All Books
    3. Search For A Book
    4. Borrow Book
    5. Return Book
    0. Exit
    """
    while True:
        print (ui)
        print()
        choice = input("Choose a number to navigate or type in 'exit' to quit: ").strip().lower()
        if choice == "1":
            print()
            addbook()

        elif choice == "2":
            print()
            allbooks()

        elif choice == "3":
            print()
            searchbook() 
            
        elif choice == "4":
            print()
            borrowbook()

        elif choice == "5":
            print()
            returnbook()

        elif choice in ["0", "exit"]:
            print()
            print("Goodbye!")
            break

        else:
            print()
            print("Invalid Choice!")
    
main() 
