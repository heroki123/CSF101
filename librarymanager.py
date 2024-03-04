#initialize empty list, set and dictionary
books_list = []
author_set = set()
books_dict = {}

#add books
books_list.append("python programming")
author_set.add("John Smith")
books_dict["python programming"] = "Jhon Smith"

books_list.append("data structures and algorithms")
author_set.add("Jane Doe")
books_dict["data structures and algorithns"] = "Jane Doe"

books_list.append("machine learning basics")
author_set.add("Alice Johnson")
books_dict["machine learning basics"] = "Alice Johnson"

#search for a book
search_title = input("enter the title of the book to search: ")
if search_title in books_list:
    print(f"Book found! Author: {books_dict[search_title]}")

else:
    print("Book not found")

#display all book
print("list of books: ")
for book in books_list:
    print(book)

# Remove a book 
remove_title = input("enter the title of the book to remove or else enter to skip: ")
if remove_title in books_list:
    remove_author = books_dict[remove_title]
    books_list.remove(remove_title)
    author_set.remove(remove_author)
    del books_dict[remove_title]
    print("book removed successfully!")
    print("Books available: ",books_list)
else:
    print("book not found!")



    