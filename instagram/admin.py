from django.contrib import admin
from .models import Image,Comment,Profile


class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('profile',)

admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Profile)
