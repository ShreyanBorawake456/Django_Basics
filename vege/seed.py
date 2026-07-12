from faker import Faker
faker = Faker()
from . models import *
import random

def create_subject_marks(n):
    try:
        students_objs = Student.objects.all()
        for student in students_objs:
            subjects = Subject.objects.all()
            for subject in subjects:
                SubjectMarks.objects.create(
                    student=student,
                    subject=subject,
                    marks=random.randint(0, 100)
                )
    except Exception as e:
        print(f"Error occurred while creating subject marks: {e}")

def seed_db(n=10) -> None:
    try:
        for i in range(0,n):
            departments_objs = Department.objects.all()
            random_index = random.randint(0, len(departments_objs) - 1)  #random.randint  returns a random integer between the two numbers provided, including both endpoints.
            department = departments_objs[random_index] # department_obj[2] means get the department object at index 2 from the list of department objects, this will return a single department object

            student_id = f'STU-0{random.randint(100 , 999)}'
            student_name = faker.name()
            student_email = faker.email()
            student_age = faker.random_int(min=18, max=100)
            student_address = faker.address()

            student_id_obj = StudentID.objects.create(student_id=student_id)  #this means create a new row in the StudentID table with the student_id value and return the object of that row

            Student.objects.create(
                department=department,
                student_id=student_id_obj,
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address 
        ) # this means store the generated data in the Student table, this will create a new row in the Student table
    except Exception as e:
        print(f"Error occurred while seeding the database: {e}")
