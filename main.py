
# REDEMPTION ACADEMY SCHOOL

class Student:
    total_registered = 0

    def __init__(self, student_id, name, class_name):
        self.student_id = student_id.strip()
        self.name = name.strip()
        self.class_name = class_name.strip()
        self.marks = {}

    def add_or_update_mark(self, subject, mark):
        subject = subject.strip().title()

        if not subject:
            print("Error: Subject cannot be empty.")
            return False

        if not isinstance(mark, (int, float)) or isinstance(mark, bool):
            print("Error: Mark must be a number.")
            return False

        if not 0 <= mark <= 100:
            print("Error: Mark must be between 0 and 100.")
            return False

        self.marks[subject] = mark
        print(f"Mark for {subject} saved successfully.")
        return True

    def calculate_average(self):
        if len(self.marks) == 0:
            return None

        total_marks = sum(self.marks.values())
        number_of_subjects = len(self.marks)

        return total_marks / number_of_subjects

    @staticmethod
    def calculate_grade(average):
        if average is None:
            return "N/A"
        elif average >= 80:
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
        print("\n" + "=" * 45)
        print("          STUDENT ACADEMIC REPORT")
        print("=" * 45)
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Class      : {self.class_name}")

        if self.marks:
            print("\nSubject Results:")

            for subject, mark in self.marks.items():
                print(f"{subject}: {mark:g}/100")
        else:
            print("\nNo examination marks recorded.")

        average = self.calculate_average()
        grade = self.calculate_grade(average)

        if average is None:
            print("Average    : Not available")
        else:
            print(f"Average    : {average:.2f}")

        print(f"Grade      : {grade}")
        print("=" * 45)

    @classmethod
    def get_total_registered(cls):
        return cls.total_registered

    @classmethod
    def increase_registration_count(cls):
        cls.total_registered += 1


# ------------------------------------------------------------
# CLASS 2: STUDENT MANAGEMENT SYSTEM
# Manages student objects and school records.
# ------------------------------------------------------------

class StudentManagementSystem:

    def __init__(self):
        self.students = []

    def find_student(self, student_id):
        student_id = student_id.strip().lower()

        for student in self.students:
            if student.student_id.lower() == student_id:
                return student

        return None

    def register_student(self, student_id, name, class_name):
        if not student_id.strip() or not name.strip() or not class_name.strip():
            print("Error: All student details are required.")
            return False

        if self.find_student(student_id) is not None:
            print("Error: This student ID is already registered.")
            return False

        student = Student(student_id, name, class_name)
        self.students.append(student)

        Student.increase_registration_count()

        print(f"\nStudent {student.name} registered successfully.")
        return True

    def display_all_students(self):
        if not self.students:
            print("\nNo students have been registered.")
            return

        for student in self.students:
            student.display_info()

    def search_student(self, student_id):
        student = self.find_student(student_id)

        if student is None:
            print("\nStudent not found.")
        else:
            student.display_info()

    def record_student_mark(self, student_id, subject, mark):
        student = self.find_student(student_id)

        if student is None:
            print("\nError: Student not found.")
            return

        student.add_or_update_mark(subject, mark)

    def display_summary(self):
        print("\n" + "=" * 45)
        print("             SCHOOL SUMMARY")
        print("=" * 45)
        print(f"Students in current system : {len(self.students)}")
        print(
            "Registrations this session : "
            f"{Student.get_total_registered()}"
        )
        print("=" * 45)


# ------------------------------------------------------------
# CLASS 3: STUDENT MANAGEMENT APPLICATION
# Controls the menu and connects the user to system objects.
# ------------------------------------------------------------

class StudentManagementApp:

    def __init__(self):
        self.system = StudentManagementSystem()
        self.load_sample_data()

    def load_sample_data(self):
        self.system.register_student("RA001", "Student One", "JSS 1")
        self.system.register_student("RA002", "Student Two", "JSS 2")

        self.system.record_student_mark("RA001", "Mathematics", 85)
        self.system.record_student_mark("RA001", "English", 76)
        self.system.record_student_mark("RA002", "Mathematics", 68)

    def display_menu(self):
        print("\n")
        print("=" * 48)
        print(" REDEMPTION ACADEMY STUDENT MANAGEMENT SYSTEM")
        print("=" * 48)
        print("1. Register a student")
        print("2. Display all students")
        print("3. Search for a student")
        print("4. Record or update a mark")
        print("5. Show school summary")
        print("6. Exit")
        print("=" * 48)

    def register_student_menu(self):
        print("\n--- STUDENT REGISTRATION ---")

        student_id = input("Enter student ID: ").strip()
        name = input("Enter student name: ").strip()
        class_name = input("Enter student class: ").strip()

        self.system.register_student(student_id, name, class_name)

    def search_student_menu(self):
        print("\n--- SEARCH STUDENT ---")

        student_id = input("Enter student ID: ").strip()
        self.system.search_student(student_id)

    def record_mark_menu(self):
        print("\n--- RECORD OR UPDATE MARK ---")

        student_id = input("Enter student ID: ").strip()
        subject = input("Enter subject: ").strip()

        try:
            mark = float(input("Enter mark (0-100): ").strip())
        except ValueError:
            print("Error: Please enter a valid numeric mark.")
            return

        self.system.record_student_mark(student_id, subject, mark)

    def process_choice(self, choice):
        if choice == "1":
            self.register_student_menu()

        elif choice == "2":
            self.system.display_all_students()

        elif choice == "3":
            self.search_student_menu()

        elif choice == "4":
            self.record_mark_menu()

        elif choice == "5":
            self.system.display_summary()

        elif choice == "6":
            print("\nThank you for using the system.")
            return False

        else:
            print("\nInvalid option. Please select a number from 1 to 6.")

        return True

    def run(self):
        print("Welcome to Redemption Academy School.")

        running = True

        while running:
            self.display_menu()
            choice = input("Enter your choice (1-6): ").strip()
            running = self.process_choice(choice)


# ------------------------------------------------------------
# PROGRAM ENTRY POINT
# Creates an application object and asks it to run.
# ------------------------------------------------------------

if __name__ == "__main__":
    app = StudentManagementApp()
    app.run()
