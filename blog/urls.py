from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.blogs_list, name='blogs_list'),
]