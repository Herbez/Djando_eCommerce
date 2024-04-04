from . import views
from django.urls import path
from django.conf.urls.static import static, settings

urlpatterns = [
    path('',views.index),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)