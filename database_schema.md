Database Schema and Design Decisions


Overview:
The database for the Employee Management System is designed to efficiently manage employee records and their attendance. It uses SQLite as the database management system, which is lightweight and easy to use, making it suitable for this project. The schema consists of two primary tables: Employee and Attendance.

Tables in the Database:

1. Employee Table
Table Name: employee

id:
Data Type: Integer
Constraints: Primary Key, Auto Increment
Description: Unique identifier for each employee.

name:
Data Type: String
Constraints: Not Null
Description: The full name of the employee.

designation:
Data Type: String
Constraints: Not Null
Description: The job title of the employee.

department:
Data Type: String
Constraints: Not Null
Description: The department in which the employee works.

date_of_joining:
Data Type: Date
Constraints: Not Null
Description: The date when the employee joined the company.

2. Attendance Table
Table Name: attendance

id:
Data Type: Integer
Constraints: Primary Key, Auto Increment
Description: Unique identifier for each attendance record.

date:
Data Type: Date
Constraints: Not Null
Description: The date of attendance.

status:
Data Type: String
Constraints: Not Null
Description: Attendance status (Present or Absent).

employee_id:
Data Type: Integer
Constraints: Foreign Key (employee.id)
Description: References the employee associated with this attendance record.

Relationships:

One-to-Many Relationship: There is a one-to-many relationship between Employee and Attendance. Each employee can have multiple attendance records, but each attendance record belongs to only one employee.

Design Decisions:

1. Choice of Database

- SQLite was chosen for its simplicity and ease of setup. It is suitable for small to medium applications, and its file-based nature allows for easy distribution and deployment.

2. Table Structure

- The Employee table captures essential information about employees that can be easily extended in the future (e.g., adding fields like email or phone number if required).

- The Attendance table is designed to log attendance efficiently. It captures the date and status, allowing for straightforward querying of attendance records for each employee.

3. Data Integrity

- Constraints such as Not Null ensure that essential fields must be filled, maintaining the integrity of the data. For instance, every employee must have a name, designation, department, and date of joining.

4. Use of Foreign Keys

- Foreign keys are used to enforce referential integrity between the Employee and Attendance tables. This ensures that every attendance record corresponds to a valid employee.

5. Scalability

- The schema is designed to be scalable. New attributes can be added to the Employee table without significant restructuring. Additionally, attendance tracking can be extended to include more features (e.g., half-days, late arrivals) if needed.

Conclusion:

The database schema for the Employee Management System is structured to provide a solid foundation for managing employee records and attendance tracking. The design decisions made prioritize data integrity, simplicity, and scalability, making it well-suited for the application’s requirements.