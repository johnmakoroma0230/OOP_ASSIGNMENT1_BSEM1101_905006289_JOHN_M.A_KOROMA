# OOP_ASSIGNMENT1_BSEM1101_905006289_JOHN_M.A_KOROMA
A Python-based Student Learning and Results Management System for Redemption Academy School, developed using Object-Oriented Programming (OOP)

## 1. Project Description

The Redemption Academy Student Learning and Results Management System is a simple Python application developed to demonstrate the practical use of Object-Oriented Programming (OOP).

We developed this project using a school environment as our real-world example. The system helps organize student records and academic results through a menu-driven interface. It allows users to register students, search for existing records, record subject marks, calculate average marks, and display academic reports.

The main purpose of this project is to demonstrate how Python classes, objects, attributes, methods, and data structures can be used to solve a practical problem.

The project also introduces Digital Public Goods (DPG) principles, including open-source development, accessibility, privacy, modularity, and reusability.

## 2. Problem Statement

Schools need an organized way to manage student information and academic results. When information is managed manually, searching for records, updating marks, and calculating averages can take time.

For this assignment, we developed a basic application to demonstrate how these activities can be managed through a computer program.

The current version is an educational prototype. It demonstrates the main operations but does not replace a complete school information system.

## 3. Project Objectives

The objectives of the project are:

1. To demonstrate the use of classes and objects in Python.
2. To create and manage student records.
3. To use a Python list to store multiple student objects.
4. To use a dictionary to associate subjects with marks.
5. To demonstrate instance methods, class methods, and static methods.
6. To calculate students' average marks and grades.
7. To validate input and prevent duplicate student IDs.
8. To demonstrate selected Digital Public Goods principles.
9. To develop a program that is easy to understand, test, and extend.

## 4. Main Features

The system provides the following features:

- Student registration.
- Unique student ID checking.
- Displaying all registered students.
- Searching for a student by ID.
- Recording subject marks.
- Updating previously recorded marks.
- Calculating average marks.
- Assigning grades based on an illustrative grading scale.
- Displaying student academic reports.
- Displaying the number of registered students.
- A simple menu-driven interface.

## 5. Technologies Used

The project uses:

- **Python:** The main programming language.
- **Visual Studio Code:** The development environment.
- **Git:** Version control.
- **GitHub:** Online source code hosting and collaboration.

The current version uses Python's built-in data structures and does not require an external database or third-party Python packages.

## 6. Project Structure

The project folder contains the following main files:

    OOP_ASSIGNMENT1_BSEM1101/
    |
    |-- main.py
    |-- README.md
    |-- LICENSE
    |-- .gitignore
    |
    |-- screenshots/
        |-- main_menu.png
        |-- student_records.png
        |-- school_summary.png

The `main.py` file contains the program code.

The `README.md` file explains the project and how to run it.

The `LICENSE` file specifies the terms under which others may use, modify, and distribute the source code.

The `.gitignore` file specifies files that Git should not track.

The `screenshots` folder can contain screenshots showing the program running.

## 7. How to Install and Run the Program

### Requirements

Before running the program, make sure Python is installed on your computer and Git is available if you intend to work with the GitHub repository.

### Step 1: Open the project

Open the project folder in Visual Studio Code.

### Step 2: Open the terminal

Select Terminal, then New Terminal.

### Step 3: Run the program

Enter the following command:

    py main.py

If the `py` command is unavailable, try:

    python main.py

### Step 4: Use the menu

When the program starts, a menu appears with six options. Enter the number corresponding to the operation you want to perform.

## 8. How to Use the System

### Option 1: Register a student

The user enters the student's ID, name, and class. The program checks that the fields are not empty and that the student ID has not already been registered.

### Option 2: Display all students

The program displays the details and academic reports of all students currently registered in the system.

### Option 3: Search for a student

The user enters a student ID. The program searches the list and displays the student's details if a matching record is found.

### Option 4: Record or update a mark

The user enters the student's ID, subject, and mark. The program checks that the student exists and that the mark is between 0 and 100.

If the subject already exists for that student, the new mark replaces the previous mark.

### Option 5: Show school record summary

The program displays the number of students registered in the current session.

### Option 6: Exit

The program terminates.

## 9. Sample Demonstration

The application loads two fictional demonstration records when it starts.

| Student ID | Name | Class | Subject | Mark |
|---|---|---|---|---:|
| RA001 | Student One | JSS 1 | Mathematics | 85 |
| RA001 | Student One | JSS 1 | English | 76 |
| RA002 | Student Two | JSS 2 | Mathematics | 68 |

These names and records are for demonstration only.

For Student One, the average is calculated as follows:

    Average = (85 + 76) / 2
    Average = 80.5

Using the illustrative grading scale in the program, an average of 80.5 receives grade A.

The grading boundaries are examples for this assignment and should be adjusted if the school has an official grading policy.

## 10. Object-Oriented Programming Concepts

### 10.1 Classes

The program contains two main classes: `Student` and `StudentManagementSystem`.

The `Student` class represents an individual student and stores their details and marks.

The `StudentManagementSystem` class manages the collection of student records.

### 10.2 Objects

Objects are created from the `Student` class. Each object represents a different student and stores its own information.

For example:

    student_one = Student("RA001", "Student One", "JSS 1")

This creates a student object with an ID, name, and class.

### 10.3 Attributes

Attributes are variables associated with an object or class.

The student attributes include:

- `student_id`
- `name`
- `class_name`
- `marks`

The class attribute `total_registered` tracks successful registrations within the running program.

### 10.4 Instance Methods

Instance methods operate on an individual object.

Examples include:

- `add_or_update_mark()`
- `calculate_average()`
- `display_info()`

These methods work with the information belonging to a particular student.

### 10.5 Class Methods

The `get_total_registered()` method uses the `@classmethod` decorator to return the class-level registration count.

The `update_registration_count()` class method updates that count when a student is successfully registered.

This demonstrates how class methods can manage information shared across instances.

### 10.6 Static Methods

The `calculate_grade()` method uses the `@staticmethod` decorator. It receives an average mark and returns the corresponding grade without needing direct access to an individual student's attributes.

### 10.7 Encapsulation

The program groups student information and related operations inside the `Student` class. This keeps the data and methods that operate on it together.

The attributes are accessible in this beginner-level implementation; strict access control has not been implemented.

### 10.8 Interaction Between Objects

The `StudentManagementSystem` stores `Student` objects in a list. When a user searches for a student or records a mark, the management system finds the appropriate object and calls its methods.

This demonstrates interaction between objects from different classes.

## 11. Python Data Structures

### 11.1 List

The program uses a list to store multiple student objects.

    self.students = []

When a student is registered, the object is added using:

    self.students.append(student)

The program loops through this list to display records and search for students.

### 11.2 Dictionary

Each student has a dictionary called `marks`.

For example:

    {
        "Mathematics": 85,
        "English": 76
    }

The subject is used as the key, and the mark is stored as the value.

This makes it possible to retrieve and update a mark using its subject name.

## 12. Input Validation and Error Handling

The program includes basic validation to improve reliability.

It checks that:

- Required registration fields are not empty.
- Student IDs are unique, without distinguishing between uppercase and lowercase letters.
- Marks are numeric and fall between 0 and 100.
- A student exists before the program records a mark.
- A valid menu option is selected.
- A valid number is entered when recording marks.

These checks help prevent common input errors.

## 13. Digital Public Goods Principles

### 13.1 Open-Source Development

The source code is maintained in a GitHub repository so that it can be reviewed and shared according to the chosen open-source licence.

### 13.2 Accessibility and Inclusion

The application uses a simple text-based menu and clear messages. It does not require an expensive graphical interface or additional Python packages.

This makes the prototype relatively easy to run in a basic Python environment.

### 13.3 Privacy

The demonstration uses fictional student records rather than real student information.

A production version would need stronger privacy controls, appropriate access permissions, and secure handling of personal and academic records.

### 13.4 Modularity

The main operations are divided between two classes. This organization makes the program easier to understand and provides a foundation for adding features in the future.

### 13.5 Reusability

The `Student` class could be reused in other educational applications, while the management class could be extended to support additional student operations.

### 13.6 Limitations

This project demonstrates selected DPG principles but is not, by itself, a formally recognized Digital Public Good.

The current version does not provide permanent storage, user authentication, multiple-user access, backups, or a graphical interface.

## 14. Testing

The following tests should be performed before submission.

| Test | Expected result |
|---|---|
| Display all students | Both sample students appear |
| Search for RA001 | Student One's report appears |
| Search for an unknown ID | A student-not-found message appears |
| Register a unique ID | The student is registered |
| Register a duplicate ID | Registration is rejected |
| Enter a mark of 85 | The mark is saved |
| Enter a mark above 100 | The mark is rejected |
| Enter invalid text for a mark | An error message appears |
| Select an invalid menu option | The program requests a valid choice |
| Select Exit | The program terminates |

Screenshots should be captured from actual program execution to demonstrate the results.

## 15. Limitations and Future Improvements

The current application stores data in memory. This means student records and marks entered during a session are lost when the program closes.

Future improvements could include:

- Saving records to SQLite or MySQL.
- Adding login and user roles.
- Editing student information.
- Generating printable academic reports.
- Adding a graphical user interface.
- Exporting records to CSV.
- Introducing automated unit tests.
- Implementing secure backups and stronger privacy controls.

These features are not included in the current version.

## 16. Conclusion

This project demonstrates how we can apply Object-Oriented Programming in Python to a practical educational problem. By developing the Redemption Academy Student Learning and Results Management System, we have demonstrated classes, objects, attributes, instance methods, class methods, static methods, and interaction between objects.

We have also used a list to store student records and a dictionary to manage subject marks. Input validation helps the application handle common mistakes, while the project documentation explains its relationship to Digital Public Goods principles.

Although this is a basic prototype and does not permanently save records, it provides a foundation for further development and demonstrates the main programming concepts required for this assignment.

## 17. References

1. Object-Oriented Programming lecture notes and teaching materials provided for the BSEM1101 module.
2. Python Software Foundation. *Python 3 Documentation*. https://docs.python.org/3/
3. GitHub Docs. *About repositories*. https://docs.github.com/en/repositories
4. Digital Public Goods Alliance. *Digital Public Goods Standard*. https://digitalpublicgoods.net/standard/

The lecture materials should be cited using the actual lecturer's name, lecture title, institution, and year if those details are available.
