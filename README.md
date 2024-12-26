
# Library Management System  

## Description  
This is a Python-based **Library Management System** project that allows users to perform basic operations such as:  
- Adding new books to the library.  
- Borrowing books from the library.  
- Returning borrowed books to the library.  
- Viewing the list of available books.  

This project was implemented following **Test-Driven Development (TDD)** principles to ensure clean, maintainable, and well-tested code.  

---

## Features  
1. **Add Books**:  
   - Add new books with a unique identifier (ISBN), title, author, and publication year.  

2. **Borrow Books**:  
   - Borrow books only if they are available.  
   - Error handling for cases where books are unavailable.  

3. **Return Books**:  
   - Return borrowed books and update availability.  

4. **View Available Books**:  
   - See a list of all available books in the library.  

---

## Prerequisites  
- Python 3.7 or higher  
- `pip` for managing Python packages  

---

## Setup Instructions  

### Step 1: Clone the Repository  
1. Clone the repository to your local machine using:  
   ```bash  
   git clone https://github.com/iammadhukar177/Library-Management-System.git  
   ```  
2. Navigate to the project directory:  
   ```bash  
   cd Library-Management-System  
   ```  

### Step 2: Create a Virtual Environment (Optional but Recommended)  
1. Create a virtual environment:  
   ```bash  
   python -m venv venv  
   ```  
2. Activate the virtual environment:  
   - On Linux/macOS:  
     ```bash  
     source venv/bin/activate  
     ```  
   - On Windows:  
     ```bash  
     venv\Scripts\activate  
     ```  

### Step 3: Install Dependencies  
Install the required packages listed in `requirements.txt`:  
```bash  
pip install -r requirements.txt  
```  

---

## Project Structure  

```
Library-Management-System/  
├── library.py             # Main implementation of the library system  
├── tests/                 # Contains all the test cases  
│   └── test_library.py    # Test cases for all library functionalities  
├── README.md              # Project documentation  
├── requirements.txt       # Dependencies list  
```  

---

## Usage  

### Step 1: Running the Tests  
To verify the implementation, run the test cases using:  
```bash  
pytest tests/  
```  
Successful execution will show results similar to:  
```
======================== test session starts ========================  
collected 4 items  

tests/test_library.py ....                                       [100%]  

========================= 4 passed in 0.03s =========================  
```  

### Step 2: Example Code Usage  
You can also interact with the `Library` class directly. Below is a Python snippet for using the library system:  

```python  
from library import Library  

# Initialize the library system  
library = Library()  

# Add books  
library.add_book({"isbn": "123456789", "title": "Book One", "author": "Author A", "year": 2020})  
library.add_book({"isbn": "987654321", "title": "Book Two", "author": "Author B", "year": 2021})  

# Borrow a book  
borrowed = library.borrow_book("123456789")  
print("Borrowed:", borrowed)  

# View available books  
available_books = library.get_available_books()  
print("Available books:", available_books)  

# Return the book  
library.return_book("123456789")  

# View available books again  
available_books = library.get_available_books()  
print("Available books after return:", available_books)  
```  

---

## Implementation Details  

### Step 1: Add Books  
- **Test Case**: Verifies that books can be added to the library and appear in the available books list.  
- **Implementation**: The `add_book` method stores book details and sets availability to `True`.  

### Step 2: Borrow Books  
- **Test Case**: Ensures users can only borrow available books and raises an error for unavailable books.  
- **Implementation**: The `borrow_book` method checks availability, updates the status, and returns the book details.  

### Step 3: Return Books  
- **Test Case**: Ensures borrowed books can be returned, updating their availability.  
- **Implementation**: The `return_book` method updates the book’s availability back to `True`.  

### Step 4: View Available Books  
- **Test Case**: Ensures users can view all books currently available.  
- **Implementation**: The `get_available_books` method filters and returns only available books.  

---

## Development Workflow  

### Step 1: Initialize Git Repository  
```bash  
git init  
echo "# Library Management System" > README.md  
git add README.md  
git commit -m "Initial commit with README"  
```  

### Step 2: Add and Commit Changes  
After implementing and testing each feature, use the following commands:  
```bash  
git add .  
git commit -m "Implement <feature> functionality and test cases"  
```  

### Step 3: Push to Remote Repository  
```bash  
git remote add origin https://github.com/iammadhukar177/Library-Management-System.git  
git push -u origin master  
```  

---

## License  
This project is licensed under the MIT License.  

--- 

