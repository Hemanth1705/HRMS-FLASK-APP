# Human Resource Management System

This is an Employee Management System built with Flask, SQLAlchemy, and SQLite. It allows users to manage employee records, including adding new employees, marking attendance, and generating reports.

## Project Structure

Hrms/
├── instance/                  # SQLite database folder
├── migrations/                # Directory for database migrations
├── templates/                 # Contains HTML templates
│   ├── employee_details.html   # Page for viewing details and attendance 								of a specific employee
│   ├── index.html             # Home page for displaying employees and 								attendance form
│   └── report_table.html      # Page for displaying reports of employees 								by department
├── app.py                     # Main application file
└── database_schema.md         # Document explaining the database schema 								and design decisions
├── README.md                  # Project documentation

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd employee_management
```

### Step 2: Create a Virtual Environment (Recommended)
Creating a virtual environment helps manage dependencies:

```bash
python -m venv venv        # Create a virtual environment named 'venv'
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Required Packages
Install the necessary packages listed in requirements.txt:

```bash
pip install -r requirements.txt
```

## Running the Application Locally

### Step 1: Set Up the Database
Before running the app, initialize the database:

```bash
flask db init        # Initialize the migration environment
flask db migrate     # Create migration scripts
flask db upgrade     # Apply the migrations to the database
```

### Step 2: Start the Application
Run the application using:

```bash
python app.py
```

### Step 3: Access the Application
Open your web browser and go to:

```arduino
http://127.0.0.1:5000/
```

## Features
- Add Employee: Users can add new employee records.
- Mark Attendance: Users can mark attendance for employees directly from the home page.
- View Employee Details: Click on an employee to see their details and attendance history.
- Generate Reports: View the count of employees in each department.

## Additional Information
- API Endpoints: The app provides various API endpoints to manage employees and attendance.
- Database: The application uses SQLite for data storage.
- Migrations: Flask-Migrate is used to manage database schema changes.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request.