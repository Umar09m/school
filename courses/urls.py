from django.urls import path
from .views import CourseView

urlpatterns = [
    path("create/", CourseView.as_view())
]