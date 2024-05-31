from random import *

def generate_student_number():
    student_number = "22"
    for i in range(6):
        student_number += str(randint(0, 9))
    return student_number
print(generate_student_number())