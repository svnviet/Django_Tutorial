
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views
from django.urls import path,include
app_name='homepage'
urlpatterns = [
    path('admin', admin.site.urls),
    path('/articles', include('articles.urls')),
    path('/accounts', include('accounts.urls')),
    path('/about', views.about,name='about'),
    path('', views.homepage, name="home"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
