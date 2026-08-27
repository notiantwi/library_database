booklist = []
def addbook ():
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    status = "Available"
    booklist.append({"title":title, "author":author, "status":status})
    print (f"{title} added successfully!")

