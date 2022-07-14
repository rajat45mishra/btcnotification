from notificarion import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"notification", views.TestClass, basename="test")
urlpatterns = router.urls
