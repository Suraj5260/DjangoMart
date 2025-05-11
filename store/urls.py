from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('aboutme/', views.aboutme, name='aboutme' ),
    path('login/', views.login_user, name='login' ),
    path('logout/', views.logout_user, name='logout' ),
]