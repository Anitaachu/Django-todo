from django.urls import path
from .views import RegisterView
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user', views.AuthUserAPIView.as_view(), name="user")

]