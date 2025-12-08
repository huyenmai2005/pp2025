students=[]
courses=[]
marks={}

def input_number_students():
    return int(input())

def input_student_info(n):
    for _ in range(n):
        sid=input()
        name=input()
        dob=input()
        students.append((sid,name,dob))

def input_number_courses():
    return int(input())

def input_course_info(n):
    for _ in range(n):
        cid=input()
        name=input()
        courses.append((cid,name))

def select_course_input_marks():
    cid=input()
    marks[cid]={}
    for s in students:
        m=float(input())
        marks[cid][s[0]]=m

def list_courses():
    for c in courses:
        print(c[0],c[1])

def list_students():
    for s in students:
        print(s[0],s[1],s[2])

def show_student_marks():
    cid=input()
    if cid in marks:
        for s in students:
            print(s[0],marks[cid][s[0]])

n=input_number_students()
input_student_info(n)
m=input_number_courses()
input_course_info(m)
select_course_input_marks()
list_courses()
list_students()
show_student_marks()
