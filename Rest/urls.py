from django.urls import path, include
from . import views
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('User', views.UserView)
router.register('Profile', views.ProfileView)
router.register('ProductPrice', views.ProductPriceView)
router.register('Document', views.DocumentView)

urlpatterns = [
    path('restapi/', include(router.urls))
]