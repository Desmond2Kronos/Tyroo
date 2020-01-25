from django.urls import path, include
from camp import views

app_name = 'camp'

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('user_login/', views.user_login, name = 'user_login'),
]
