from random import randint

def generate_student_number():
    student_member_list = []
    
    student_number = randint(22300000,23300000)
    if student_number not in student_member_list:
        student_member_list.append(student_number)
    else : 
        generate_student_number()
    return student_member_list
print(generate_student_number())