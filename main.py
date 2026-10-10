
# ==========================================================
# REDEMPTION ACADEMY
# STUDENT LEARNING AND RESULTS MANAGEMENT SYSTEM
# Object-Oriented Programming Assignment 
# JOHN MOHAMED ALIE KOROMA BSEM1101 905006289
# ==========================================================


class Student:
    """Represents one student and their academic results."""

    total_students = 0

    def __init__(self, student_id, name, class_name):
        self.student_id = student_id
        self.name = name
        self.class_name = class_name
        self.marks = {}

        Student.total_students += 1

    def add_or_update_mark(self, subject, mark):
        """Record or update a student's mark."""

        if not isinstance(mark, (int, float)) or isinstance(mark, bool):
            print("Error: Marks must be a number.")
            return

        if not 0 <= mark <= 100:
            print("Error: Marks must be between 0 and 100.")
            return

        self.marks[subject] = mark
        print(f"Mark recorded successfully for {self.name}.")

    def calculate_average(self):
        """Calculate the student's average mark."""

        if not self.marks:
            return 0

        return sum(self.marks.values()) / len(self.marks)

    @staticmethod
    def calculate_grade(average):
        """Return a grade based on the average mark."""

        if average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    def display_info(self):
        """Display a student's details and results."""

        print("\n" + "=" * 40)
        print("       STUDENT ACADEMIC REPORT")
        print("=" * 40)
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Class      : {self.class_name}")

        if self.marks:
            print("\nSubject Results:")

            for subject, mark in self.marks.items():
                print(f"{subject}: {mark}/100")
        else:
            print("\nNo marks have been recorded.")

        average = self.calculate_average()
        grade = self.calculate_grade(average)

        print(f"\nAverage    : {average:.2f}")
        print(f"Grade      : {grade}")
        print("=" * 40)

    @classmethod
    def get_total_students(cls):
        """Return the number of Student objects created."""

        return cls.total_students


class StudentManagementSystem:
    """Manages student records for Redemption Academy."""

    def __init__(self):
        self.students = []

    def add_student(self, student):
        """Add a Student object to the system."""

        if self.find_student(student.student_id):
            print("Error: This student ID already exists.")
            return

        self.students.append(student)
        print(f"{student.name} has been registered successfully.")

    def find_student(self, student_id):
        """Find a student using their unique ID."""

        for student in self.students:
            if student.student_id.lower() == student_id.lower():
                return student

        return None

    def display_all_students(self):
        """Display every student stored in the list."""

        if not self.students:
            print("No students have been registered yet.")
            return

        for student in self.students:
            student.display_info()

    def record_mark(self, student_id, subject, mark):
        """Find a student and record their subject mark."""

        student = self.find_student(student_id)

        if student is None:
            print("Student not found.")
            return

        student.add_or_update_mark(subject, mark)

    def show_summary(self):
        """Display a summary of the school records."""

        print("\n===== SCHOOL RECORD SUMMARY =====")
        print(f"Students in this system: {len(self.students)}")
        print(
            "Student objects created: "
            f"{Student.get_total_students()}"
        )
        print("=================================")


def main():
    """Run the main menu of the application."""

    system = StudentManagementSystem()

    # Sample records for demonstration only.
    # These are fictional records, not actual student data.
    sample_students = [
        Student("RA001", "Student One", "JSS 1"),
        Student("RA002", "Student Two", "JSS 2"),
    ]

    for student in sample_students:
        system.add_student(student)

    system.record_mark("RA001", "Mathematics", 85)
    system.record_mark("RA001", "English", 76)
    system.record_mark("RA002", "Mathematics", 68)

    while True:
        print("\n")
        print("=" * 45)
        print(" REDEMPTION ACADEMY STUDENT MANAGEMENT")
        print("=" * 45)
        print("1. Register a student")
        print("2. Display all students")
        print("3. Search for a student")
        print("4. Record or update a mark")
        print("5. Show school record summary")
        print("6. Exit")
        print("=" * 45)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            student_id = input("Enter student ID: ").strip()
            name = input("Enter student name: ").strip()
            class_name = input("Enter class: ").strip()

            if not student_id or not name or not class_name:
                print("Error: All fields are required.")
                continue

            student = Student(student_id, name, class_name)
            system.add_student(student)

        elif choice == "2":
            system.display_all_students()

        elif choice == "3":
            student_id = input("Enter student ID to search: ").strip()
            student = system.find_student(student_id)

            if student:
                student.display_info()
            else:
                print("Student not found.")

        elif choice == "4":
            student_id = input("Enter student ID: ").strip()
            subject = input("Enter subject: ").strip()

            if not subject:
                print("Error: Subject cannot be empty.")
                continue

            try:
                mark = float(input("Enter mark (0-100): "))
                system.record_mark(student_id, subject, mark)
            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == "5":
            system.show_summary()

        elif choice == "6":
            print("Thank you for using the school management system.")
            break

        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
