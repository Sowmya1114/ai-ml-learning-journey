#store student details in a file
def add_student(name,marks):
    with open("students.txt", "a") as f:
        f.write(f"{name},{marks}\n")
def read_student():
    with open("students.txt", "r") as f:
        for line in f:
            name,marks=line.strip().split(",")
            print("Name: ", name, "| Marks: ", marks)
add_student("radisri",99)
add_student("sowra",98)
read_student()
