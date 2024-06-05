from datetime import datetime
def borrow(self):
    
    #Allows a user to borrow a book from the library.
    #Prompts the user to enter the ID of the book they wish to borrow.
    #If the book is available, the user's name and the current date and time are recorded, and the book's status is updated to 'Already issued'.
    #If the book is not available, the user is informed who currently has the book and is prompted to try again.
    
    book_id = input("Enter the ID of the book: ")
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if book_id in self.books_dict.keys():
        #checks if the book is available in the library
        if self.books_dict[book_id]["status"] != "Available":
            print(f"This book has already been issued to {self.books_dict[book_id]['lender_name']} on {self.books_dict[book_id]['issue_date']}")
            return self.borrow()
        else:
            your_name = input("Enter Your Name: ")
            self.books_dict[book_id]["lender_name"] = your_name
            self.books_dict[book_id]["issue_date"] = current_date
            self.books_dict[book_id]["status"] = "Already issued"
            print(f"Book '{self.books_dict[book_id]['title']}' has been issued to {your_name} on {current_date}")
    else:
        print("Sorry! Book not found in the library.")
        return self.borrow()

def return_book(self):
    
    #Allows a user to return a borrowed book to the library.
    #Prompts the user to enter the ID of the book they wish to return.
    #If the book is found and is currently issued, the book's status is updated to 'Available', and the lender's information is cleared.
    #If the book is not currently issued, the user is informed.
    
    book_id=input("Enter Book Id: ")
    if book_id in self.books_dict.keys():
        if self.books_dict[book_id]["status"]=="Available":
            print("This book is already available in the library.Please check your Book ID carefully")
            return return_book()
        elif not self.books_dict[book_id]["status"]=="Available":
            self.books_dict[book_id]["lender_name"]=""
            self.books_dict[book_id]["issue_date"]=""
            self.books_dict[book_id]["status"]="Available"
            print("Book successfully returned.")
    else:
        print("Book Id is not found in the library")
    

    