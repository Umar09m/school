from django.urls import path
from .views import StudentView, student_list, student_detail, StudentAPIVIew, StudentDetailAPIView

urlpatterns = [
    # path("", StudentView.as_view()),
    path("students/", StudentAPIVIew.as_view(), name="student_list"),
    path("students/<int:pk>/", StudentDetailAPIView.as_view(), name="student_detail")
]