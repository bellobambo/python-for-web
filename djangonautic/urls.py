from django.contrib import admin
from django.conf.urls import  include
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from articles import views as article_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/' , include('accounts.urls')),
    path('articles/', include('articles.urls')),
    path('about/', views.about),
    path('', article_views.article_list , name="home"),
]


urlpatterns += staticfiles_urlpatterns()