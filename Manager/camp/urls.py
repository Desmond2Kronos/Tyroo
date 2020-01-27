from django.urls import path, include
from camp import views

app_name = 'camp'

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('user_login/', views.user_login, name = 'user_login'),
    path('add/', views.add_rule, name = 'add_rule'),
    path('edit/', views.edit_rule, name = 'edit_rule')
]
