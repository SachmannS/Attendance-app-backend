from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'organisation', OrganisationViewSet, basename = 'org')
router.register(r'profile', ProfileViewSet, basename = 'profile')
urlpatterns = [
    path('', include(router.urls)),
    path('login', LoginView.as_view())
]