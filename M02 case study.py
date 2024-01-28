"""
Author: Amarius Trotter
name: M02 case study
desc: test if a student is on Deans list & Honor roll
"""
student=str(input("enter students last name or ZZZ to exit: "))
while student != "ZZZ":
    Fname=str(input("enter students first name: "))
    gpa=float(input("enter GPA: "))
    if gpa>=3.5:
        print(Fname+" is on Deans list")
    elif gpa>=3.25:
        print(Fname+" is on Honer Roll")
    else:
        print("not on Deans list or Honor Roll")
    print()
    student=str(input("enter students last name or ZZZ to exit: "))
