from django.urls import path,re_path
from . import views
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register("banner",views.BannerAPIView)
urlpatterns = [

]

urlpatterns+= router.urls