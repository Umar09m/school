from django.urls import path
from .views import SchoolView

urlpatterns = [
    path("", SchoolView.as_view())
]