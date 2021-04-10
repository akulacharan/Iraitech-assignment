from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('',views.home,name='home'),
    path('logout/',views.logout,name='logout'),
    path('<str:username>/calculate/',views.calculate,name='calculate')
]