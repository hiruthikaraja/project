import json

class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def _init_(self, id, name, age, grade, marks):
        super()._init_(name, age)
        self.id = id
        self.grade = grade
        self.marks = marks

    def get_average(self):
        return sum(self.marks.values()) / len(self.marks)


# ---- JSON Functions ----
def load_students(filename="students.json"):
    with open(filename, "r") as f:
        return json.load(f)


def save_students(students, filename="students.json"):
    with open(filename, "w") as f:
        json.dump(students, f, indent=4)


def print_students(students):
    for s in students:
        avg = sum(s["marks"].values()) / len(s["marks"])
        print(f"ID: {s['id']} | Name: {s['name']} | Grade: {s['grade']} | Avg Marks: {avg:.2f}")


def find_topper(students):
    topper = max(students, key=lambda s: sum(s["marks"].values())/len(s["marks"]))
    avg = sum(topper["marks"].values()) / len(topper["marks"])
    print(f"\nTopper: {topper['name']} with Average {avg:.2f}")
    return topper


def add_student(students, new_student):
    students.append(new_student)
    save_students(students)
    print(f"\n Added {new_student['name']} successfully!")
