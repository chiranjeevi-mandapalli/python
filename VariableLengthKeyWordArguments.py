# if in case we need to pass data in a specific way then we can use ** to convert it into variablelengthKeyword argument
def collect_student_data(**data):
    print(data);
    print(type(data))

# if in case we nedd to pass one more parameter after variable lengthKeywordargument then we should pass like key value pairs
def collect_student_data1(profession,**data):
    print(profession)
    print(data);
    print(type(data))
#
# def collect_student_data2(**data,profession): #need to check this
#     print(profession)
#     print(data);
#     print(type(data))

collect_student_data(Name='Rohith', Age=28, Avg=60.5, Gender='M');
collect_student_data1('student',Name='Rohith', Age=28, Avg=60.5, Gender='M');
# collect_student_data2('student',Name='Rohith', Age=28, Avg=60.5, Gender='M',profession="Student");


