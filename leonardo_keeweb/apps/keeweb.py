from django.conf.urls import url
from leonardo_keeweb.views import KeewebView

urlpatterns = [
    url(r'^keeweb/$',  KeewebView.as_view())
]
