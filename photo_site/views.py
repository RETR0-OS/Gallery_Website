from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from photo_manager.models import *

@login_required
def home(request):
    latest_gallery1 = Picture_Gallery.objects.all().latest("id")
    latest_gallery = Gallery_Picture.objects.filter(gallery=latest_gallery1)
    latest_imgs = Single_Picture.objects.all().order_by("-id")[:3]
    data ={
        "latest_gallery": latest_gallery,
        "latest_imgs": latest_imgs
    }
    return render(request, "home.html", data)
