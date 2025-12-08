# 2.student.mark.oop.py

class Student:
    def __init__(self,sid,name,dob):
        self.sid=sid
        self.name=name
        self.dob=dob
    def list(self):
        print(self.sid,self.name,self.dob)

class Course:
    def __init__(self,cid,name):
        self.cid=cid
        self.name=name
        self.marks={}
    def list(self):
        print(self.cid,self.name)
    def input_marks(self,students):
        for s in students:
            self.marks[s.sid]=float(input())
    def show_marks(self,students):
        for s in students:
            print(s.sid,self.marks[s.sid])

class Manager:
    def __init__(self):
        self.students=[]
        self.courses=[]
    def input_students(self):
        n=int(input())
        for _ in range(n):
            sid=input()
            name=input()
            dob=input()
            self.students.append(Student(sid,name,dob))
    def input_courses(self):
        n=int(input())
        for _ in range(n):
            cid=input()
            name=input()
            self.courses.append(Course(cid,name))
    def select_course_input_marks(self):
        cid=input()
        for c in self.courses:
            if c.cid==cid:
                c.input_marks(self.students)
                return
    def list_courses(self):
        for c in self.courses:
            c.list()
    def list_students(self):
        for s in self.students:
            s.list()
    def show_marks(self):
        cid=input()
        for c in self.courses:
            if c.cid==cid:
                c.show_marks(self.students)
                return

m=Manager()
m.input_students()
m.input_courses()
m.select_course_input_marks()
m.list_courses()
m.list_students()
m.show_marks()
