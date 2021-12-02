from django.contrib.auth.models import User
from django.db import models
from rest_framework.authtoken.models import Token

from courses.models import Course


class Department(models.Model):
	name = models.CharField(max_length=250)
	school = models.ForeignKey("schools_app.School", on_delete=models.PROTECT, related_name="departments")


class Position(models.Model):
	name = models.CharField(max_length=255)
	department = models.ForeignKey(Department, on_delete=models.PROTECT)

	def __str__(self):
		return self.name


class Employee(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee")
	date_of_birth = models.DateField()
	image = models.ImageField("/profile_image", null=True)
	position = models.ForeignKey(Position, on_delete=models.PROTECT)
	salary = models.DecimalField(max_digits=7,decimal_places=2)

	# def __str__(self):
		# return f"{self.user.first_name} {self.user.last_name}"


class Tutor(models.Model):
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="tutor")
	course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name="tutors")
	experience = models.PositiveSmallIntegerField()





