import json
from datetime import datetime

book_details = {
    "Title": "",
    "Author": "",
    "Publication_Year": 0,
    "Genres": [],
    "Read_Status": False,
    "Reading_Progress": {
        "Start_Date": "",
        "Current_Page": 0,
        "Total_Pages": 0,
        "Progress_Percentage": 0
    }
}

# Initialize an empty list to store books
library = []

def validate_year(year):
    """Validate the publication year"""
    try:
        year = int(year)
        current_year = datetime.now().year
        if year < 1800 or year > current_year + 1:
            raise ValueError(f"Year must be between 1800 and {current_year + 1}")
        return year
    except ValueError as e:
        raise ValueError("Please enter a valid year (e.g., 1925)")

def validate_input(prompt, validator=None):
    """Get and validate user input"""
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                print("This field cannot be empty. Please try again.")
                continue
            if validator:
                value = validator(value)
            return value
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

def get_genres():
    """Get multiple genres for a book"""
    genres = []
    while True:
        genre = input("Enter a genre (or press Enter to finish): ").strip()
        if not genre:
            if not genres:
                print("Please enter at least one genre.")
                continue
            break
        genres.append(genre)
    return genres

def get_reading_progress():
    """Get reading progress details"""
    start_date = input("When did you start reading? (YYYY-MM-DD): ")
    while True:
        try:
            current_page = int(input("Current page number: "))
            total_pages = int(input("Total pages: "))
            if current_page < 0 or total_pages < 0:
                print("Page numbers cannot be negative.")
                continue
            if current_page > total_pages:
                print("Current page cannot be greater than total pages.")
                continue
            progress = (current_page / total_pages) * 100
            return {
                "Start_Date": start_date,
                "Current_Page": current_page,
                "Total_Pages": total_pages,
                "Progress_Percentage": round(progress, 1)
            }
        except ValueError:
            print("Please enter valid numbers.")

def add_book():
    """Add a new book to the library with validation"""
    print("\nAdding a new book:")
    print("-" * 30)
    
    # Get book details with validation
    title = validate_input("Enter book title: ")
    
    # Check for duplicate titles
    if any(book["Title"].lower() == title.lower() for book in library):
        print(f"Warning: A book with the title '{title}' already exists.")
        if input("Do you want to continue? (yes/no): ").lower() != "yes":
            return
    
    author = validate_input("Enter book author: ")
    year = validate_input("Enter publication year: ", validate_year)
    
    print("\nEnter genres (press Enter when done):")
    genres = get_genres()
    
    while True:
        status = input("Have you read this book? (yes/no): ").lower()
        if status in ['yes', 'no']:
            break
        print("Please enter 'yes' or 'no'")
    
    # Get reading progress if the book is being read
    reading_progress = None
    if status == "no":
        print("\nEnter reading progress:")
        reading_progress = get_reading_progress()
    
    # Create the book dictionary
    book = {
        "Title": title,
        "Author": author,
        "Publication_Year": year,
        "Genres": genres,
        "Read_Status": status == "yes",
        "Reading_Progress": reading_progress
    }
    
    # Add book to library and save
    library.append(book)
    save_library()
    
    print("\nBook added successfully!")
    print("Book details:")
    print(format_book_display(book))

def save_library():
    """Save the library data to a JSON file"""
    try:
        with open('library_data.json', 'w') as file:
            json.dump(library, file, indent=4)
        print("Library data saved successfully!")
    except Exception as e:
        print(f"Error saving library: {e}")

def load_library():
    """Load the library data from JSON file"""
    global library
    try:
        with open('library_data.json', 'r') as file:
            library = json.load(file)
        print("Library data loaded successfully!")
    except FileNotFoundError:
        library = []  # If file doesn't exist, start with empty library
        print("No existing library found. Starting with empty library.")
    except Exception as e:
        print(f"Error loading library: {e}")
        library = []

def format_book_display(book, index=None):
    """Format a book for display"""
    read_status = "Read" if book["Read_Status"] else "Unread"
    genres_str = ", ".join(book["Genres"])
    progress_str = ""
    
    if not book["Read_Status"] and book["Reading_Progress"]:
        progress = book["Reading_Progress"]
        progress_str = f" - Progress: {progress['Progress_Percentage']}% ({progress['Current_Page']}/{progress['Total_Pages']} pages)"
    
    book_str = f"{book['Title']} by {book['Author']} ({book['Publication_Year']}) - {genres_str} - {read_status}{progress_str}"
    if index is not None:
        return f"{index + 1}. {book_str}"
    return book_str

def filter_by_genre(genre):
    """Filter books by genre"""
    return [book for book in library if genre.lower() in [g.lower() for g in book["Genres"]]]

def sort_library(sort_by="title"):
    """Sort the library by specified criteria"""
    if sort_by == "title":
        library.sort(key=lambda x: x["Title"].lower())
    elif sort_by == "author":
        library.sort(key=lambda x: x["Author"].lower())
    elif sort_by == "year":
        library.sort(key=lambda x: x["Publication_Year"])
    elif sort_by == "progress":
        library.sort(key=lambda x: x["Reading_Progress"]["Progress_Percentage"] if x["Reading_Progress"] else 0, reverse=True)

def MenuSystem():
    Choice = input("""Welcome to your Personal Library Manager!
1. Add a book
2. Remove a book
3. Search for a book
4. Display all books
5. Display statistics
6. Filter by genre
7. Sort library
8. Exit
Enter your choice: """)
    
    if Choice == "1":
        add_book()
    
    elif Choice == "2":
        Find_Book = input("Enter the title of the book to remove: ")
        # Find and remove the book
        for book in library[:]:
            if Find_Book.lower() in book["Title"].lower():
                library.remove(book)
                save_library()  # Save after removing a book
                print(f"Book '{Find_Book}' has been removed successfully!")
                break
        else:
            print(f"Book '{Find_Book}' not found in your library.")
    
    elif Choice == "3":
        print("\nSearch by:")
        print("1. Title")
        print("2. Author")
        search_choice = input("Enter your choice: ")
        
        if search_choice == "1":
            Search_Book = input("Enter the title: ")
            found = False
            print("\nMatching Books:")
            for book in library:
                if Search_Book.lower() in book["Title"].lower():
                    print(format_book_display(book))
                    found = True
        elif search_choice == "2":
            Search_Author = input("Enter the author: ")
            found = False
            print("\nMatching Books:")
            for book in library:
                if Search_Author.lower() in book["Author"].lower():
                    print(format_book_display(book))
                    found = True
        else:
            print("Invalid choice!")
            found = True  # To skip the "not found" message
            
        if not found:
            print(f"No books found matching your search.")
    
    elif Choice == "4":
        if not library:
            print("Your library is empty.")
        else:
            print("\nYour Library:")
            for index, book in enumerate(library):
                print(format_book_display(book, index))
    
    elif Choice == "5":
        if not library:
            print("Your library is empty.")
        else:
            total_books = len(library)
            read_books = sum(1 for book in library if book["Read_Status"])
            unread_books = total_books - read_books
            read_percentage = (read_books / total_books) * 100 if total_books > 0 else 0
            
            print("\nLibrary Statistics:")
            print(f"Total books: {total_books}")
            print(f"Books Read: {read_books}")
            print(f"Books Unread: {unread_books}")
            print(f"Percentage read: {read_percentage:.1f}%")
            
            # Genre statistics
            genres = {}
            for book in library:
                for genre in book["Genres"]:
                    genres[genre] = genres.get(genre, 0) + 1
            
            print("\nBooks by Genre:")
            for genre, count in sorted(genres.items()):
                print(f"{genre}: {count}")
            
            # Reading progress statistics
            in_progress = [book for book in library if not book["Read_Status"] and book["Reading_Progress"]]
            if in_progress:
                print("\nCurrently Reading:")
                for book in in_progress:
                    progress = book["Reading_Progress"]
                    print(f"{book['Title']}: {progress['Progress_Percentage']}% complete")
    
    elif Choice == "6":
        if not library:
            print("Your library is empty.")
        else:
            print("\nAvailable genres:")
            genres = set()
            for book in library:
                genres.update(book["Genres"])
            for genre in sorted(genres):
                print(f"- {genre}")
            
            genre = input("\nEnter genre to filter by: ").strip()
            filtered_books = filter_by_genre(genre)
            
            if filtered_books:
                print(f"\nBooks in genre '{genre}':")
                for index, book in enumerate(filtered_books):
                    print(format_book_display(book, index))
            else:
                print(f"No books found in genre '{genre}'")
    
    elif Choice == "7":
        if not library:
            print("Your library is empty.")
        else:
            print("\nSort by:")
            print("1. Title")
            print("2. Author")
            print("3. Publication Year")
            print("4. Reading Progress")
            sort_choice = input("Enter your choice: ")
            
            if sort_choice == "1":
                sort_library("title")
            elif sort_choice == "2":
                sort_library("author")
            elif sort_choice == "3":
                sort_library("year")
            elif sort_choice == "4":
                sort_library("progress")
            else:
                print("Invalid choice!")
                return
            
            print("\nSorted Library:")
            for index, book in enumerate(library):
                print(format_book_display(book, index))
    
    elif Choice == "8":
        save_library()  # Save before exiting
        print("Library saved to file. Goodbye!")
        return
    
    else:
        print("Invalid choice. Please enter a number between 1 and 8.")
    
    MenuSystem()

# Load existing library data when starting the program
load_library()
MenuSystem()