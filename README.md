# Student Management System

A full-stack **Student Management System** built using **Python
(Flask)** and **MySQL**.\
This project demonstrates backend API development, authentication,
database design, and frontend integration with real-world features like
pagination and sorting.

------------------------------------------------------------------------

## 📘 Project Overview

The Student Management System is designed to manage student records
securely and efficiently.\
It supports authentication, CRUD operations, sorting, pagination, and
audit fields, following a clean and modular Flask architecture.

------------------------------------------------------------------------

## 🚀 Features

-   Session-based authentication (login & logout)
-   Secure management of student records
-   Full CRUD operations (Create, Read, Update, Delete)
-   Server-side sorting (name, created date, updated date)
-   Pagination for large datasets
-   Audit fields using `created_at` and `updated_at`
-   RESTful APIs using Flask
-   Dynamic frontend using JavaScript and CSS

------------------------------------------------------------------------

## 🛠️ Tech Stack

**Backend** - Python - Flask - Flask-CORS

**Database** - MySQL

**Frontend** - HTML - JavaScript - CSS

**Tools & Concepts** - REST APIs - Session-based authentication -
Environment variables - Modular Flask architecture - Git & GitHub

------------------------------------------------------------------------

## 📂 Project Structure

    backend/
      app/
        routes/        -> API routes
        services/      -> Business logic
        config.py      -> Application configuration
        extensions.py -> Flask extensions
      run.py           -> Application entry point

    frontend/
      templates/       -> HTML templates
      static/          -> CSS and JavaScript files

    database/
      schema.sql       -> Database schema
      db_config.py     -> Database connection

    requirements.txt
    README.md

------------------------------------------------------------------------

## 📸 Screenshots

- **Login Page**  
![Login](frontend/static/images/screenshots/login_ss.png)

- **Register Page**  
![Register](frontend/static/images/screenshots/register_ss.png)

- **Forgot Password Page**  
![Forgot Password](frontend/static/images/screenshots/forgot_password_ss.png)

- **Dashboard / Add Student**  
![Dashboard](frontend/static/images/screenshots/dashboard_ss.png)

- **Student List with Pagination**  
![Student List](frontend/static/images/screenshots/student_list_ss.png)

------------------------------------------------------------------------

## 🗄️ Database Schema (Summary)

### Students Table

-   id
-   sname
-   age
-   course
-   created_at
-   updated_at

### Users Table

-   id
-   username
-   password
-   created_at

------------------------------------------------------------------------

## ▶️ How to Run Locally

### 1️⃣ Clone the Repository

``` bash
git clone https://github.com/SubhanduG/student-management-system-python.git
cd student-management-system-python
```

### 2️⃣ Create Virtual Environment

``` bash
python -m venv venv
```

### 3️⃣ Activate Virtual Environment

**Windows**

``` bash
venv\Scripts\activate
```

**Linux / macOS**

``` bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

### 5️⃣ Configure Environment Variables

Create a `.env` file in the project root:

``` env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=student_db
SECRET_KEY=dev-secret-key
```

### 6️⃣ Setup Database

Run SQL commands from `database/schema.sql`.

### 7️⃣ Run Application

``` bash
python backend/run.py
```

Open browser:

    http://127.0.0.1:5000

------------------------------------------------------------------------

## 🔐 Security Notes

-   Database credentials are stored using environment variables
-   `.env` files and virtual environments are excluded from version
    control
-   Passwords are securely hashed
-   Protected APIs require authentication

------------------------------------------------------------------------

## 🎓 Learning Outcomes

-   Designed REST APIs using Flask
-   Implemented authentication and access control
-   Worked with relational databases and SQL queries
-   Built pagination and sorting mechanisms
-   Integrated frontend UI with backend APIs
-   Applied clean project structuring and configuration management

------------------------------------------------------------------------

## 🔮 Future Improvements

-   Role-based access control
-   Admin dashboard
-   Export student data
-   Improved UI and UX
-   Cloud deployment

------------------------------------------------------------------------

## 👤 Author

**Subhandu Ghosh**\
MSc Computer Science\
Python Backend & Full-Stack Developer\
