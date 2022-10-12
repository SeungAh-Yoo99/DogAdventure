from django.contrib import admin

from .models import AbandonedDog, Image

# Register your models here.

# Image 클래스를 inline으로 나타낸다.
class ImageInline(admin.TabularInline):
    model = Image

# AbandonedDog 클래스는 해당하는 Image 객체를 리스트로 관리하는 한다. 
class AbandonedDogAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]

admin.site.register(AbandonedDog, AbandonedDogAdmin)