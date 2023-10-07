from django.shortcuts import render, redirect
from .models import Single_Picture, Picture_Gallery, Gallery_Picture
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

@login_required
def show_single_picture(request):
    pictures = Single_Picture.objects.all()
    data = {
        'pictures':pictures
    }
    if pictures is not None:
        return render(request, "show_single_picture.html", data)
    else:
        raise Http404('Picture does not exist!')

@login_required
def show_gallery(request, id):
    gallery = Picture_Gallery.objects.get(pk=id)
    pictures = Gallery_Picture.objects.filter(gallery=gallery)
    data ={
        'pictures':pictures
    }
    if pictures is not None:
        return render(request, "show_gallery.html", data)
    else:
        raise Http404('Gallery does not exist!')

@login_required
def show_galleries(request):
    galleries = Picture_Gallery.objects.all().order_by("-id")
    thumbnails = []
    for a in galleries:
        t = Gallery_Picture.objects.filter(gallery=a).order_by("-id")
        thumbnails.append(t)
    data = {
        "galleries":galleries,
        "thumbnails":thumbnails
    }
    return render(request, "show_galleries.html", data)

@login_required
def add_single_picture(request):
    if request.method == "POST":
        picture = request.FILES.get("image")
        caption = request.POST["caption"]
        if picture is not None:
            new_image = Single_Picture(picture=picture, caption=caption)
            new_image.save()
            return redirect("home")
    else:
        return render(request, "add_single_picture.html")

@login_required
def add_gallery(request):
    if request.method == "POST":
        pictures = request.FILES.getlist("images")
        gallery_name = request.POST["gallery_name"]
        gallery_message = request.POST["gallery_caption"]
        print(pictures)
        print(gallery_name)
        print(gallery_message)
        if pictures != []:
            print(pictures)
            new_gallery = Picture_Gallery(gallery_name=gallery_name, gallery_message=gallery_message)
            new_gallery.save()
            print(new_gallery)
            for pic in pictures:
                new_pic = Gallery_Picture(gallery=new_gallery, image=pic)
                new_pic.save()
            return redirect("home")
        else:
            print("error")
            return redirect("home")

    else:
        return render(request, "add_gallery.html")
