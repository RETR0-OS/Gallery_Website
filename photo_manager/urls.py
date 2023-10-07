from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('picture/', views.show_single_picture, name="show_single_picture"),
    path('galleries', views.show_galleries, name="show_galleries"),
    path('gallery/<int:id>', views.show_gallery, name="show_gallery"),
    path('add_picture/', views.add_single_picture, name="add_single_picture"),
    path('add_gallery/', views.add_gallery, name="add_gallery"),
]
