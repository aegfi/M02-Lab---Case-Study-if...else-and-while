"""
Author: Amarius Trotter
name: M02 case study
desc: test if a student is on Deans list & Honer Roll
"""
student=str(input("enter students last name: "))
while student != "ZZZ":
    Fname=str(input("enter students first name: "))
    gpa=float(input("enter GPA: "))
    if gpa>=3.5:
        print(Fname+" is on Deans list and Honer Roll")
    elif gpa>=3.25:
        print(Fname+" is on Honer Roll")
    else:
        print("not on Deans list or Honer Roll")
    print()
    student=str(input("enter students last name: "))