from django.contrib import admin
from .models import Single_Picture, Picture_Gallery, Gallery_Picture
# Register your models here.

class PictureAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Single_Picture, PictureAdmin)
admin.site.register(Picture_Gallery, PictureAdmin)
admin.site.register(Gallery_Picture)
