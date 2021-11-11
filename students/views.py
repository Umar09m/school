from django.shortcuts import render
from django.views import generic
from .models import Student, StudentCourse
from .forms import StudentForm, StudentCourseForm


class StudentView(generic.CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student.html'
    success_url = '/students/'

    def get_context_data(self, **kwargs):
        context = super(StudentView, self).get_context_data(**kwargs)
        context['students'] = Student.objects.all()
        return context


class StudentCourseView(generic.CreateView):
    model = StudentCourse
    form_class = StudentCourseForm
    template_name = 'student_course.html'
    success_url = '/students/'

    def get_context_data(self, **kwargs):
        context = super(StudentCourseView, self).get_context_data(**kwargs)
        context['student_courses'] = StudentCourse.objects.all()
        return context


# def students_list(request):
#     students = Student.objects.all()
#     return render(request, 'student.html', {'students': students})
