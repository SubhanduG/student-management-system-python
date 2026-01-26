# Backend Data Management Application (Python + MySQL)

A **full-stack Student Management System** built with **Python (Flask), MySQL, and Bootstrap**, allowing users to **register, login, manage students**, and perform CRUD operations via both **web interface** and **CLI tool**.  

This project demonstrates **web development, REST API design, authentication, database integration, and frontend-backend interaction**, making it ideal for showcasing full-stack skills.

---

## 🔹 Features

### **User Authentication**
- Register new users.
- Login with **session-based authentication**.
- Reset forgotten passwords.
- Passwords securely **hashed using Werkzeug**.

### **Student Management**
- Add, Update, and Delete student records.
- View all students with **pagination**.
- Sort students by **name, creation date, and last updated date**.
- Dynamic **dashboard interface** built with **Bootstrap 5**.

### **CLI Interface**
- Command-line interface to manage students offline.
- Add, View, Update, Delete student records via terminal.
- Validates user input for age, name, and course.

### **Tech Stack**
- **Editor:** VS Code
- **Backend:** Python, Flask, Flask-CORS
- **Database:** MySQL
- **Frontend:** HTML, Bootstrap 5, JavaScript (Fetch API)
- **Security:** Password hashing, session management
- **Others:** dotenv for environment configuration

---

## 🔹 Project Structure

student-management-system-python/
│
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── pages.py
│   │   │   └── students.py
│   │   │
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── auth_service.py
│   │   │   └── students_service.py
│   │   │
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── extensions.py
│   │
│   ├── cli/
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   └── main.py
│   │
│   ├── __init__.py
│   └── run.py
│
├── database/
│   ├── db_config.py
│   └── schema.sql
│
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   ├── images/
│   │   └── js/
│   │
│   └── templates/
│       ├── login.html
│       ├── register.html
│       ├── forgot_password.html
│       └── index.html
│
├── venv/
├── .env
├── README.md
└── requirements.txt

---

## 🔹 Installation

### 1. Clone the repository
```bash
git clone https://github.com/SubhanduG/student-management-system-python.git
cd student-management-system-python
```

### 2. Setup Python environment
```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Database

🔹Create a MySQL database:
```sql
CREATE DATABASE student_db;
```

🔹Update .env with your MySQL credentials:
```ini
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=student_db
SECRET_KEY=super-secret-key
FLASK_ENV=development
```

🔹Run the SQL schema:
```bash
mysql -u root -p student_db < database/schema.sql
```

### 5. Run the Flask App
```bash
python -m backend.run
```
Access the app at: http://127.0.0.1:5000

### 6. Run the CLI Tool (Optional)
```bash
python -m backend.cli
```

---

## 🔹 Skills & Learnings Demonstrated

- Full-stack development with Python Flask and Bootstrap
- RESTful API design with CRUD operations
- Session-based authentication and password hashing
- Database integration with MySQL
- Frontend interactivity using JavaScript Fetch API
- CLI development for offline management
- Handling pagination, sorting, and validation
- Environment configuration using dotenv

---

## 🔹 Future Enhancements

- Add user roles (Admin/Student) and permissions.
- Improve UI/UX with a modern frontend framework (React/Vue).
- Add search functionality for students.
- Implement JWT authentication for API security.
- Deploy to Heroku or AWS for live demonstration.

---

## 🔹 Author

Subhandu Ghosh
MSc Computer Science
Backend & Full-Stack Developer (Fresher)

---

## 🔹 Purpose

This Student Management System is a full-stack web application built with Python Flask, MySQL, and Bootstrap that enables users to securely register, log in, and manage student records with features like add, update, delete, sorting, and pagination. It demonstrates practical CRUD operations, session management, and responsive UI development, making it an ideal portfolio project for freshers to showcase real-world web development skills.