from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('ajax/send_email/', views.send_email, name='send_email')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

