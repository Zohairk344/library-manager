# Personal Library Manager

## Overview
The Personal Library Manager is a command-line application that allows users to manage their book collection. Users can add, remove, search for books, and view statistics about their library. The application supports multiple genres for each book and tracks reading progress.

## Features
- **Add a Book**: Enter details for a new book, including title, author, publication year, genres, and reading status.
- **Remove a Book**: Remove a book from the library by title.
- **Search for a Book**: Search for books by title or author.
- **Display All Books**: View all books in the library with their details.
- **Display Statistics**: View total books, read/unread counts, and percentage of books read.
- **Filter by Genre**: Filter and display books based on selected genres.
- **Sort Library**: Sort books by title, author, publication year, or reading progress.
- **Reading Progress Tracking**: Track the start date, current page, total pages, and progress percentage for each book.

## Requirements
- Python 3.x
- `json` module (included in standard Python library)
- `datetime` module (included in standard Python library)

## Installation
1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Run the application using the command:
   ```bash
   python library_manager.py
   ```

## Usage
1. Upon starting the application, you will see a menu with options.
2. Follow the prompts to add, remove, search, or display books.
3. Enter the required information as prompted.
4. The library data is saved in a JSON file (`library_data.json`) for persistence.


## Predefined Books
The application starts with a set of predefined books:
- The Great Gatsby by F. Scott Fitzgerald (1925) - Genres: Fiction, Classic, Romance - Read
- 1984 by George Orwell (1949) - Genres: Dystopian, Science Fiction, Political Fiction - Unread
- To Kill a Mockingbird by Harper Lee (1960) - Genres: Fiction, Classic, Historical Fiction - Read
- The Hobbit by J.R.R. Tolkien (1937) - Genres: Fantasy, Adventure, Classic - Read
- Pride and Prejudice by Jane Austen (1813) - Genres: Romance, Classic, Historical Fiction - Unread

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
