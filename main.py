
# ==========================================================
# REDEMPTION ACADEMY
# STUDENT LEARNING AND RESULTS MANAGEMENT SYSTEM
# Object-Oriented Programming Assignment 
# JOHN MOHAMED ALIE KOROMA BSEM1101 905006289
# ==========================================================

class Student:
    """Represents a student and their academic results."""

    total_registered = 0

    def __init__(self, student_id, name, class_name):
        self.student_id = student_id.strip()
        self.name = name.strip()
        self.class_name = class_name.strip()
        self.marks = {}

    def add_or_update_mark(self, subject, mark):
        """Add or update a subject mark."""

        if not isinstance(mark, (int, float)) or isinstance(mark, bool):
            print("Error: The mark must be a number.")
            return False

        if not 0 <= mark <= 100:
            print("Error: Marks must be between 0 and 100.")
            return False

        subject = subject.strip()

        if not subject:
            print("Error: Subject cannot be empty.")
            return False

        self.marks[subject] = mark
        print(f"Mark saved successfully for {self.name}.")
        return True

    def calculate_average(self):
        """Calculate the average of recorded marks."""

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
        """Display student details and academic results."""

        print("\n" + "=" * 42)
        print("          STUDENT ACADEMIC REPORT")
        print("=" * 42)
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Class      : {self.class_name}")

        if self.marks:
            print("\nSubject Results:")

            for subject, mark in self.marks.items():
                print(f"  {subject}: {mark:g}/100")
        else:
            print("\nNo marks have been recorded.")

        average = self.calculate_average()
        print(f"\nAverage    : {average:.2f}")
        print(f"Grade      : {self.calculate_grade(average)}")
        print("=" * 42)

    @classmethod
    def get_total_registered(cls):
        """Return the number of registered students."""

        return cls.total_registered

    @classmethod
    def update_registration_count(cls, amount):
        """Update the registered-student count."""

        cls.total_registered += amount


class StudentManagementSystem:
    """Stores and manages student records."""

    def __init__(self):
        self.students = []

    def find_student(self, student_id):
        """Find a student by ID, ignoring letter case."""

        student_id = student_id.strip().lower()

        for student in self.students:
            if student.student_id.lower() == student_id:
                return student

        return None

    def add_student(self, student):
        """Register a student if the ID is unique."""

        if self.find_student(student.student_id):
            print("Error: This student ID is already registered.")
            return False

        self.students.append(student)
        Student.update_registration_count(1)

        print(f"{student.name} registered successfully.")
        return True

    def display_all_students(self):
        """Display all registered students."""

        if not self.students:
            print("No students have been registered.")
            return

        for student in self.students:
            student.display_info()

    def record_mark(self, student_id, subject, mark):
        """Find a student and record a subject mark."""

        student = self.find_student(student_id)

        if student is None:
            print("Error: Student not found.")
            return

        student.add_or_update_mark(subject, mark)

    def show_summary(self):
        """Display the school record summary."""

        print("\n" + "=" * 42)
        print("          SCHOOL RECORD SUMMARY")
        print("=" * 42)
        print(f"Students in this system: {len(self.students)}")
        print(
            "Total registered students: "
            f"{Student.get_total_registered()}"
        )
        print("=" * 42)


def load_sample_data(system):
    """Load fictional records for demonstration."""

    student_one = Student("RA001", "Student One", "JSS 1")
    student_two = Student("RA002", "Student Two", "JSS 2")

    system.add_student(student_one)
    system.add_student(student_two)

    system.record_mark("RA001", "Mathematics", 85)
    system.record_mark("RA001", "English", 76)
    system.record_mark("RA002", "Mathematics", 68)


def main():
    """Display the menu and run the application."""

    system = StudentManagementSystem()
    load_sample_data(system)

    while True:
        print("\n")
        print("=" * 46)
        print(" REDEMPTION ACADEMY STUDENT MANAGEMENT")
        print("=" * 46)
        print("1. Register a student")
        print("2. Display all students")
        print("3. Search for a student")
        print("4. Record or update a mark")
        print("5. Show school record summary")
        print("6. Exit")
        print("=" * 46)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            student_id = input("Enter student ID: ").strip()
            name = input("Enter student name: ").strip()
            class_name = input("Enter class: ").strip()

            if not student_id or not name or not class_name:
                print("Error: All fields are required.")
                continue

            # Check the ID before creating the Student object.
            if system.find_student(student_id):
                print("Error: This student ID is already registered.")
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
                print("Error: Enter a valid number for the mark.")

        elif choice == "5":
            system.show_summary()

        elif choice == "6":
            print("Thank you for using Redemption Academy Student Management.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
