from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/', views.login_user, name="login_user"),
    path('logout/', views.logout_user, name="logout_user"),

]
