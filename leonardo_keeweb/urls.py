from constance import config
from django.conf.urls import url

from leonardo_keeweb.views import KeewebView

urlpatterns = [
    url(r'^%s$' % config.LEONARDO_KEEWEB_PATH,
        KeewebView.as_view())
]

if not config.LEONARDO_KEEWEB_PUBLIC:
    from leonardo.decorators import _decorate_urlconf
    _decorate_urlconf(urlpatterns)
