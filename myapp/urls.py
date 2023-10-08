from os import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', display_text_file, name='display_text_file'),
    path('poll_image/', views.poll_image, name='poll_image'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)