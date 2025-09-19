from student_module import load_students
from teacher_module import load_teachers


# Report: Students per grade
def students_per_grade(students):
    grade_count = {}
    for s in students:
        grade_count[s["grade"]] = grade_count.get(s["grade"], 0) + 1
    return grade_count


# Report: Average marks in each subject
def average_subject_marks(students):
    totals = {}
    counts = {}
    for s in students:
        for subject, mark in s["marks"].items():
            totals[subject] = totals.get(subject, 0) + mark
            counts[subject] = counts.get(subject, 0) + 1

    averages = {sub: totals[sub]/counts[sub] for sub in totals}
    return averages


# Report: Total salary spent on teachers
def total_teacher_salary(teachers):
    return sum(int(t["salary"]) for t in teachers)


# Report: Class teacher mapping (student → teacher of best subject)
def class_teacher_mapping(students, teachers):
    mapping = []
    for s in students:
        # Find best subject
        best_subject = max(s["marks"], key=s["marks"].get)
        # Match teacher
        teacher = next((t for t in teachers if t["subject"] == best_subject), None)
        if teacher:
            mapping.append((s["name"], best_subject, teacher["name"]))
    return mapping


# Combined Report
def generate_report():
    students = load_students()
    teachers = load_teachers()

    print("\n===== School Report =====")

    # Students per grade
    grade_summary = students_per_grade(students)
    print("\nStudents per Grade:")
    for grade, count in grade_summary.items():
        print(f" Grade {grade}: {count} students")

    # Average subject marks
    subject_avgs = average_subject_marks(students)
    print("\nAverage Marks per Subject:")
    for subject, avg in subject_avgs.items():
        print(f" {subject}: {avg:.2f}")

    # Teacher salary
    total_salary = total_teacher_salary(teachers)
    print(f"\nTotal Salary Spent on Teachers: {total_salary}")

    # Class teacher mapping
    print("\nClass Teacher Assignments:")
    for student, subject, teacher in class_teacher_mapping(students, teachers):
        print(f" {student} → Best in {subject} → Class Teacher: {teacher}")
