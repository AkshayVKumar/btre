from django.urls import path
from . import views

app_name="accounts"
urlpatterns = [
    path('login/',views.user_login,name="login"),
    path('register/',views.register,name="register"),
    path('logout/',views.user_logout,name="logout"),
    path('dashboard/',views.dashboard,name='dashboard'),
]