from django.apps import AppConfig


class PersonaConfig(AppConfig):
    """
    Provides primary key type for devotional app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'persona'
