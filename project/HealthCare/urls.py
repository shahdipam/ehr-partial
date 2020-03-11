from django.urls import path
from HealthCare import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home', views.home, name='dashboard'),
    path('files', views.files, name='files'),
    path('book', views.book, name='book'),
    path('profile', views.profile, name='profile'),
    path('about', views.about, name='about'),
    path('doc', views.index_doc, name='doctor'),
    path('home_doc', views.home_doc, name='dashboard_doc'),
    path('files_doc', views.files_doc, name='files_doc'),
    path('book_doc', views.book_doc, name='book'),
    path('profile_doc', views.profile_doc, name='profile'),
    path('about_doc', views.about_doc, name='about'),
    path('login_pat', views.login_pat, name='login_pat'),
    path('login_doc', views.login_doc, name='login_doc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)