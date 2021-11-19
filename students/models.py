from django.db import models
from schools_app.models import School
from courses.models import Course


class Student(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=False)
    is_graduated = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.student}/{self.course}"
