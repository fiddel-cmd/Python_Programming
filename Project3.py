def student_details():
    name  =  input('Enter your name:')
    age  =  input('Enter your age:')
    adm  =  input('Enter your your student admission:')
    output = print(f'Student name {name},addmision Number{adm}.student age {age}')
    return name, age,adm,output

student_details()

