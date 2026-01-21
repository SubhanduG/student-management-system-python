# Backend Data Management Application (Python + MySQL)

This project demonstrates my hands-on experience in backend development using Python and MySQL.
The focus of the project is on clean architecture, database interaction, input validation and real-world backend practices.


## Project Overview
This is a menu-driven backend application that performs full CRUD (Create, Read, Update, Delete) operations on structured data stored in a MySQL database. The application is designed with proper validation, error handling an clean control flow to ensure data integrity and stability.


## Features
- Add new records with validation
- View stored records
- Update existing records safely
- Delete records using unique identifiers
- Menu-driven command-line interface
- Proper handling of invalid input and database errors


## Technologies Used
- **Python**
- **MySQL**
- **mysql-connector-python**
- **Git & GitHub**
- **VS Code**


## Concepts Implemented
- Backend application design
- CRUD operations
- Python-MySQL connectivity
- Parameterized SQL queries
- Input validation for numeric and text fields
- Exception handling using try-except
- Clean execution flow using early returns
- Version control using Git


## Project Structure
student-management-system-python
|-----db_config.py
|-----main.py
|-----README.md
|-----requirements.txt


## How to Run the Application

### Prerequisites
- Python installed
- MySQL server running
- MySQL database configured

### Database Setup
- '''sql
    CREATE DATABASE IF NOT EXISTS student_db;
    USE student_db;
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        sname VARCHAR(50) NOT NULL,
        age INT NOT NULL,
        course VARCHAR(50) NOT NULL
    );

### Install Dependencies
- '''bash 
    pip install -r requirements.txt

### Run the Application
- '''bash
    python main.py


## Future Enhancements
- Convert application to REST APIs using Flask
- Add authentication and authorization
- Improve logging mechanism
- Deploy application on cloud infrastructure


## Author
Subhandu Ghosh
MSc Computer Science
Backend & Full-Stack Developer (Fresher)


# Purpose
This project was built to strengthen backend development fundamentals and demonstrate the ability to design, implement and manage a reliable data-driven application using Python and MySQL.