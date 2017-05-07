from django.conf.urls import url, include

from .views import IndexView
from api import urls as api_urls

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^api/', include(api_urls, namespace='api')),
]
