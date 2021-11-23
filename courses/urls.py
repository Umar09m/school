from django.urls import path
from .views import CourseView, courses_list, course_detail, CourseListView, CourseDetailView

urlpatterns = [
    path("courses/", CourseListView.as_view(), name="courses-list"),
    path("courses/<int:pk>/", CourseDetailView.as_view(), name="course-detail"),
]