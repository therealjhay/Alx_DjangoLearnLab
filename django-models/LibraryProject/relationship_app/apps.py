# relationship_app/apps.py
from django.apps import AppConfig

class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'

    def ready(self):
        """
        Imports signals when the app is ready.
        """
        import relationship_app.signals # noqa: F401