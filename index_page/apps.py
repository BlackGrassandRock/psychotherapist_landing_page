from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class IndexPageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'index_page'
    verbose_name = _('Index Page')
