from django.urls import path
from HealthCare import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.home, name='dashboard'),
    path('', views.index, name='homepage'),
    path('files', views.files, name='files'),
    path('book', views.book, name='book'),
    path('profile', views.profile, name='profile'),
    path('about', views.about, name='about'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)