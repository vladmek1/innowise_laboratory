students = []


def add_student():
    """
    Adds a new student to the system
    Checks that name is not empty and not duplicate
    """
    name = input("Enter student name: ")

    if not name.strip():
        print("Name cannot be empty!")
        return

    for student in students:
        if student["name"] == name:
            print("A student with this name already exists.")
            return

    new_student = {"name": name, "grades": []}
    students.append(new_student)
    print(f"Student {name} added!")


def add_grades():
    """
    Adds grades for a student
    Can enter grades until 'done' is typed
    Checks that grade is between 0 and 100
    """
    name = input("Enter student name: ")

    for student in students:
        if student["name"] == name:
            while True:
                grade = input("Enter a grade (or 'done' to finish): ")
                if grade.lower() == "done":
                    return

                try:
                    grade_num = int(grade)
                    if 0 <= grade_num <= 100:
                        student["grades"].append(grade_num)
                    else:
                        print("Grade must be from 0 to 100")
                except ValueError:
                    print("Invalid input, please enter a number.")
            return

    print("Student not found.")


def show_report():
    """
    Shows report for all students
    Average grades, max/min and overall average
    If no students or no grades - shows message
    """
    print("--- Student Report ---")
    if not students:
        print("No students in the system")
        return

    all_grades = []
    for student in students:
        all_grades.extend(student["grades"])

    if not all_grades:
        print("No grades available for any student")
        return

    else:
        average_grades = []
        print()
        for student in students:
            try:
                avg_grade = round(sum(student["grades"]) / len(student["grades"]), 2)
                print(f"{student['name']}'s average grade is {avg_grade}")
                average_grades.append(avg_grade)
            except ZeroDivisionError:
                print(f"{student['name']}'s average grade is N/A")
        if average_grades:
            print(f"""{'-' * 25}
Max Average: {max(average_grades)}
Min Average: {min(average_grades)}
Overall Average: {round(sum(average_grades) / len(average_grades), 2)}""")
        else:
            return


def find_top_student():
    """
    Finds student with highest average grade
    Uses lambda function with max() to find
    """
    if students:
        has_grades = False
        for student in students:
            if student["grades"]:
                has_grades = True
                break

        if has_grades:
            best_student = max(students, key=lambda s: sum(s["grades"]) / len(s["grades"]) if s["grades"] else -1)
            best_avg = round(sum(best_student["grades"]) / len(best_student["grades"]), 2)
            print(f"The student with the highest average is {best_student['name']} with a grade of {best_avg}")
        else:
            print("No grades available for any student")
    else:
        print("No students in the system")


while True:
    try:
        print("""
===The Student Grade Analyzer===
1.Add a new student
2.Add a grades for a student
3.Show report(all students)
4.Find top performer
5.Exit
        """)
        choice = int(input("Please, choose the option:"))

        if choice == 1:
            add_student()
        elif choice == 2:
            add_grades()
        elif choice == 3:
            show_report()
        elif choice == 4:
            find_top_student()
        elif choice == 5:
            break
        else:
            print("Please, enter a number between 1-5")

    except ValueError:
        print("Invalid input. Please enter a number.")