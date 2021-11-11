from django.urls import path
from .views import StudentView, StudentCourseView

urlpatterns = [
    path("", StudentView.as_view()),
    path("course/", StudentCourseView.as_view())
]