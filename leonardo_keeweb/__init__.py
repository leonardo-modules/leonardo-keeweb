
from django.apps import AppConfig

default_app_config = 'leonardo_keeweb.Config'


LEONARDO_APPS = ['leonardo_keeweb']

LEONARDO_PUBLIC = True

LEONARDO_OPTGROUP = 'KeeWeb'

LEONARDO_CONFIG = {
    'LEONARDO_KEEWEB_PUBLIC': (True, 'Make keeweb accessible without login.'),
    'LEONARDO_KEEWEB_PATH': ('keeweb/', 'Set custom URL.'),
    'LEONARDO_KEEWEB_DROPBOX_APP_FOLDER': ('qp7ctun6qt5n9d6', 'Dropbox app folder.'),
}


class Config(AppConfig):
    name = 'leonardo_keeweb'
    verbose_name = "leonardo-keeweb"
