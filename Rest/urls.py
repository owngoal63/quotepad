from django.urls import path, include
from . import views
from rest_framework import routers 
from Rest.views import ProfileList, ProfileDetail

router = routers.DefaultRouter()
router.register('User', views.UserView)
router.register('Profile', views.ProfileView)
router.register('ProductPrice', views.ProductPriceView)
router.register('Document', views.DocumentView)
#router.register('ProfileList', views.DocumentView)

urlpatterns = [
    path('restapi/', include(router.urls)),
    path('pl/',ProfileList.as_view()),
    path('pd/<int:pk>/',ProfileDetail.as_view())
]