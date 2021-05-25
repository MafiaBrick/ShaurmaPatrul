from django.urls import path,include
from . import views
urlpatterns = [
    path('signup/',views.signupuser, name = 'signup'),
    path('',views.loginuser, name = 'login'),
    path('logout/',views.logoutuser, name = 'logout'),
]
