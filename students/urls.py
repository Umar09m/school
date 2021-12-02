

from .views import StudentViewSet2
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"students", StudentViewSet2, basename="students")

urlpatterns = router.urls