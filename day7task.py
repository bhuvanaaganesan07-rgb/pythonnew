students={}
for _ in range(3):
    name=input("Name: ")
    marks=int(input("Marks: "))
    students[name]=marks
print("Results:")
for name,marks in students.items():
    if marks>=90:
        g="A"
    elif marks>=75:
        g="B"
    else:
        g="F"
print(f"{name}:{marks}-Grade{g}")
avg=sum(students.values())/len(students)
print(f"Average: {avg:.1f}")