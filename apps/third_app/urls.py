from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^course$', views.course),
    url(r'^question$', views.question),
    url(r'^delete$', views.delete)
]