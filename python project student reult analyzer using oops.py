class Student:
    def __init__(self,name,marks):
        if marks < 0 or marks > 100:
            return ValueError ("marks must be between 0 and 100")
        self.name = name 
        self.marks = marks
    def is_passed(self):
        return self.marks>=40
    def __str__(self):
        status = "Pass" if self.is_passed() else "Fail"
        return f"{self.name} : {self.marks} ({status})"
    
class ResultAnalyzer:
    def __init__(self):
        self.students = []
    def add_students(self,name,marks):
        self.students.append(Student(name,marks))
    def average_marks(self):
        assert len(self.students)>0,"No students added"
        total = sum(s.marks for s in self.students)
        return total / len(self.students)
ra = ResultAnalyzer()
ra.add_students("A",50)
ra.add_students("B",33)
ra.add_students("C",99)
for s in ra.students:
    print(s)
print("Average",ra.average_marks())