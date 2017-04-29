from django.conf.urls import url
from django.contrib import admin
from pig_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^translate/', views.piglatin, name='piglatin'),
    url(r'^about/', views.about, name='about'),
    url(r'^admin/', admin.site.urls),
]
