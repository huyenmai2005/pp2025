import math
import numpy as np
import curses

class Student:
    def __init__(self,sid,name,dob):
        self.sid=sid
        self.name=name
        self.dob=dob
        self.gpa=0
    def list(self,win):
        win.addstr(f"{self.sid} {self.name} {self.dob} {self.gpa:.2f}\n")

class Course:
    def __init__(self,cid,name,credit):
        self.cid=cid
        self.name=name
        self.credit=credit
        self.marks={}
    def list(self,win):
        win.addstr(f"{self.cid} {self.name} {self.credit}\n")
    def input_marks(self,students):
        for s in students:
            m=float(input())
            m=math.floor(m*10)/10
            self.marks[s.sid]=m
    def get_mark(self,s):
        return self.marks[s.sid]

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
            credit=float(input())
            self.courses.append(Course(cid,name,credit))
    def input_marks(self):
        cid=input()
        for c in self.courses:
            if c.cid==cid:
                c.input_marks(self.students)
                return
    def calc_gpa(self):
        for s in self.students:
            arr=[]
            w=[]
            for c in self.courses:
                if s.sid in c.marks:
                    arr.append(c.get_mark(s))
                    w.append(c.credit)
            if len(arr)>0:
                arr=np.array(arr)
                w=np.array(w)
                s.gpa=(arr*w).sum()/w.sum()
            else:
                s.gpa=0
    def sort_by_gpa(self):
        self.students.sort(key=lambda x:x.gpa,reverse=True)
    def ui(self,win):
        win.clear()
        win.addstr("Courses:\n")
        for c in self.courses:
            c.list(win)
        win.addstr("Students:\n")
        for s in self.students:
            s.list(win)
        win.refresh()
        win.getch()

m=Manager()
m.input_students()
m.input_courses()
m.input_marks()
m.calc_gpa()
m.sort_by_gpa()
curses.wrapper(m.ui)
