from django.urls import path
from .views import CourseView, courses_list, course_detail

urlpatterns = [
    path("courses/", courses_list, name="courses-list"),
    path("courses/<int:pk>/", course_detail, name="course-detail"),
]