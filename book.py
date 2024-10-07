book = [
    {"ID": 1, "Title" : "The Great Gatsby", "Author" : "F. Scott Fitzgerald", "Genre" : "Fiction", "Published Year" : "1925", "ISBN" : "978-0743273565", "Stock" : "20", "Price" : "15.99"},
    {"ID": 2, "Title" : "To Kill a Mockingbird", "Author": "Harper Lee ", "Genre": "Fiction", "Published Year": "1960","ISBN": "978-0060935467", "Stock": "35", "Price": "10.99"},
    {"ID": 3, "Title" : "1984", "Author": "George Orwell", "Genre": "Dystopian", "Published Year": "1949", "ISBN": "978-0451524935", "Stock": "40", "Price": "9.99"},
    {"ID": 4, "Title" : "The catcher in the rye" , "Author": "J.D. Salinger", "Genre": "Fiction", "Published Year": "1951", "ISBN": "978-0316769488", "Stock": "25", "Price": "8.99"},
    {"ID": 5, "Title" : "A Brief History of Time", "Author": "Stephen Hawking ", "Genre" : "Non-Fiction", "Published Year": "1988", "ISBN": "978-0553380163", "Stock": "10", "Price": "18.99"}
]
for books in book:
  print(f"ID: {books['ID']}, Title: {books['Title']}, Author: {books['Author']}, Genre: {books['Genre']}, Published Year: {books['Published Year']}, ISBN: {books['ISBN']} ,Stock: {books['Stock']} Price: {books['Price']}")