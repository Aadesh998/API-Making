from django.contrib import admin
from django.urls import path
from base import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('',views.endpoints),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('advocate/',views.advocate_list),
    path('advocate/<str:username>/',views.Advocatedetails.as_view()),
    
]