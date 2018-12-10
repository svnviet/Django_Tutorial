from django.conf.urls import url
from . import views
from django.urls import path
app_name = 'articles'

urlpatterns = [
    path('/', views.List.as_view(), name="list"),
    path('/create', views.article_create, name="create"),
    path('/<slug>', views.Detail.as_view(), name="detail"),
]
