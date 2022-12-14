"""dogAdventure URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from http.client import ImproperConnectionState
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from VolunteerMatching import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # my api
    path('', views.TestAPI.as_view()),
    path('detail/', views.DogDetailAPI.as_view()),
    path('list/', views.DogListFilteringAPI.as_view()),
    path('reserve', views.ReserveAPI.as_view()),
    path('isSuccess/', views.isSuccessAPI.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
