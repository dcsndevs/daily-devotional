from django.apps import AppConfig


class EventsConfig(AppConfig):
    """
    Provides primary key type for events app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'events'
