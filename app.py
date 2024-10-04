from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import date

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
db = SQLAlchemy(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Employee model
class Employee(db.Model):
    """Model representing an employee."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    designation = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    date_of_joining = db.Column(db.Date, nullable=False)

# Attendance model
class Attendance(db.Model):
    """Model representing an employee's attendance record."""
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(10), nullable=False)  # Present/Absent
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))

# Home route to display employees
@app.route('/')
def home():
    employees = Employee.query.all()  # Fetch all employees
    return render_template('index.html', employees=employees)

# Route to add an employee
@app.route('/add_employee', methods=['POST'])  # Ensure methods=['POST'] is included
def add_employee():
    """Route to add a new employee. Expects name, designation, department, and date of joining."""
    name = request.form['name']  # Direct access to form data
    designation = request.form['designation']
    department = request.form['department']
    date_of_joining = request.form['date_of_joining']

    # Create a new employee record
    new_employee = Employee(
        name=name,
        designation=designation,
        department=department,
        date_of_joining=date.fromisoformat(date_of_joining)
    )
    db.session.add(new_employee)
    db.session.commit()  # Commit the session

    return redirect(url_for('home'))  # Redirect back to home page

# API to retrieve all employees
@app.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()  # Query all employees from the database
    employee_list = [{'id': e.id, 'name': e.name, 'designation': e.designation, 'department': e.department, 'date_of_joining': str(e.date_of_joining)} for e in employees]
    return jsonify({'employees': employee_list})

@app.route('/employee/<int:employee_id>')
def employee_details(employee_id):
    """Route to view details of a specific employee by ID, including attendance records."""
    employee = Employee.query.get_or_404(employee_id)
    attendance_records = Attendance.query.filter_by(employee_id=employee_id).all()
    return render_template('employee_details.html', employee=employee, attendance_records=attendance_records)

# API to mark attendance
@app.route('/mark_attendance/<int:employee_id>', methods=['POST'])
def mark_attendance(employee_id):
    """API route to mark attendance for a specific employee. Expects date and status."""
    employee = Employee.query.get_or_404(employee_id)
    date_of_attendance = request.form['date']
    status = request.form['status']
    employee = Employee.query.get_or_404(employee_id)
    date_of_attendance = request.form['date']
    status = request.form['status']

    new_attendance = Attendance(
        employee_id=employee_id,
        date=date.fromisoformat(date_of_attendance),
        status=status
    )
    db.session.add(new_attendance)
    db.session.commit()
    return redirect(url_for('employee_details', employee_id=employee_id))

# API to get employee attendance
@app.route('/attendance/<int:employee_id>', methods=['GET'])
def get_attendance(employee_id):
    """API route to get attendance records for a specific employee by ID."""
    attendance_records = Attendance.query.filter_by(employee_id=employee_id).all()
    attendance_list = [{'date': str(a.date), 'status': a.status} for a in attendance_records]
    return jsonify({'attendance': attendance_list})

# Report: Count employees by department
@app.route('/report')
def report():
    # Query to get the count of employees by department
    report_data = db.session.query(Employee.department, db.func.count(Employee.id)).group_by(Employee.department).all()
    # Render the report in an HTML table
    return render_template('report_table.html', report_data=report_data)

@app.route('/test', methods=['GET'])
def test_route():
    """Test route to confirm that the API is working."""
    return jsonify({'message': 'Test route is working!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
