import csv

class Teacher:
    def _init_(self, id, name, subject, salary):
        self.id = id
        self.name = name
        self.subject = subject
        self.salary = salary

    def get_details(self):
        return f"Teacher: {self.name}, Subject: {self.subject}, Salary: {self.salary}"


# ---- CSV Functions ----
def load_teachers(filename="teachers.csv"):
    teachers = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            teachers.append(row)
    return teachers


def save_teachers(teachers, filename="teachers.csv"):
    fieldnames = ["id", "name", "subject", "salary"]
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(teachers)


def print_teachers(teachers):
    for t in teachers:
        print(f"ID: {t['id']} | Name: {t['name']} | Subject: {t['subject']} | Salary: {t['salary']}")


def average_salary(teachers):
    total = sum(int(t["salary"]) for t in teachers)
    return total / len(teachers)


def highest_paid_teacher(teachers):
    top = max(teachers, key=lambda t: int(t["salary"]))
    print(f"\nHighest Paid Teacher: {top['name']} with Salary {top['salary']}")
    return top


def add_teacher(teachers, new_teacher):
    teachers.append(new_teacher)
    save_teachers(teachers)
    print(f"\n Added {new_teacher['name']} successfully!")
