from django.shortcuts import render
from django.views import generic
from .models import Course
from .forms import CourseForm


class CourseView(generic.CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course.html'
    success_url = 'home'

    # def post(self, request, *args, **kwargs):
    #     form = self.get_form_class(request.data)
    #     if form
