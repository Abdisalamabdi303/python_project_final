from datetime import datetime
def borrow(self):
    book_id = input("Enter the ID of the book: ")
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if book_id in self.books_dict:
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
        print("Book not found.")
        return self.borrow()