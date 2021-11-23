from django.urls import path
# from .views import StudentView, student_list, student_detail, StudentAPIVIew, StudentDetailAPIView,
# StudentListMixinView, StudentDetailMixinView, StudentListCreateView, StudentDetailView
from .views import StudentViewSet2
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"students", StudentViewSet2, basename="students")

urlpatterns = router.urls