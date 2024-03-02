from django.apps import AppConfig


class NewuserConfig(AppConfig):
    """
    Provides primary key type for devotional app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newuser'
