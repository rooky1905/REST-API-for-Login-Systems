from django.urls import path, include
from profiles_api import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename = 'hello-viewset')
router.register('profile-viewset', views.UserProfileViewSet)

urlpatterns = [
    path('hello/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginView.as_view()),
    path('', include(router.urls)),
]