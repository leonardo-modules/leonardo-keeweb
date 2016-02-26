from django.views.generic.base import TemplateView
from constance import config


class KeewebView(TemplateView):

    template_name = 'keeweb.html'

    def get_context_data(self, *args, **kwargs):
        return {
            'DROPBOX_APP_FOLDER': config.LEONARDO_KEEWEB_DROPBOX_APP_FOLDER
        }
