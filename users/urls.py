from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import Login, Register, EmployeeProfileRetrieveUpdateDestroy

app_name = "users"


urlpatterns = [
    path("login/", Login.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("register/", Register.as_view()),
    path("update_profile/<str:username>/", EmployeeProfileRetrieveUpdateDestroy.as_view()),
]
