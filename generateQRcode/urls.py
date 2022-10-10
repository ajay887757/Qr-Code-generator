from django.contrib import admin
from django.urls import path
from .views import GenerateQrCode
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('GenerateQrCode/', GenerateQrCode.as_view(),name="GenerateQrCode"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
