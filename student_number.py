from random import randint

def generate_student_number():
    student_member_list = []
    for i in range(1000):
        student_number = str(randint(2230, 2330)) + ''.join([str(randint(0, 9)) for j in range(4)])
        if student_number not in student_member_list:
            student_member_list.append(student_number)
    return student_member_list
print(generate_student_number())