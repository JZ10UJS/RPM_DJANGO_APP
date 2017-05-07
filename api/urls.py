from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('^info/$', views.InfoView.as_view()),
    url('^info/([\w\d-]+)$', views.InfoDetailView.as_view()),
]
