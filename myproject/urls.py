"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]

from django.urls import path
from myapp.views import display_text_file

urlpatterns = [
    path('', display_text_file, name='display_text_file'),
]

from django.urls import path
from myapp.views import display_text_file, poll_file_content

urlpatterns = [
    path('', display_text_file, name='display_text_file'),
    path('poll_file/', poll_file_content, name='poll_file_content'),
]

from django.contrib import admin
from django.urls import path
from myapp.views import display_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', display_image, name='display_image'),
]