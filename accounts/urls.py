from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('logout/',LogoutView.as_view(template_name='index.html'),name="users_logout"),
    path('',views.index,name="index"),
    path('login',views.users_login,name='users_login'),
    path('register',views.users_register,name='users_register'),
]
