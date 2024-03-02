from django.apps import AppConfig


class DevotionalConfig(AppConfig):
    """
    Provides primary key type for devotional app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'devotional'
