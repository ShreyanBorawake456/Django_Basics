from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) # user ke sath recipe ko link kar diya 
    # taki pata chale ki kaunse user ne kaunse recipe banayi hai
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to="recipe")
    

    recipe_view_count = models.IntegerField(default=1) # recipe_view_count me recipe ke kitne views hai ye store hoga


class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering = ['department'] # department ko alphabetical order me show karne ke liye
    

class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.subject_name

class Student(models.Model):
    department = models.ForeignKey(Department, related_name='depart', on_delete=models.CASCADE) # department ke sath student ko link kar diya taki pata chale ki kaunse student kaunse department me hai
    student_id = models.OneToOneField(StudentID , related_name='studentid',on_delete=models.CASCADE) # student_id ke sath student ko link kar diya taki pata chale ki kaunse student kaunse student_id ke sath hai
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=10)
    student_address = models.TextField()

    def __str__(self) -> str:
        return self.student_name
    

    class Meta:
        ordering = ['student_name'] # student_name ko alphabetical order me show karne ke liye
        verbose_name = 'Student' # admin panel me Student ke jagah Student show hoga


class SubjectMarks(models.Model):
    student = models.ForeignKey(Student, related_name='studentmarks', on_delete=models.CASCADE) # student ke sath subject_marks ko link kar diya taki pata chale ki kaunse student kaunse subject_marks ke sath hai
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.student.student_name} - {self.subject.subject_name} - {self.marks}" #this will return the student name, subject name and marks in the format "student name - subject name - marks"    


    class Meta:
        unique_together = ('student', 'subject') # student aur subject ke combination ko unique banane ke liye taki ek student ke liye ek hi subject ke marks ho
