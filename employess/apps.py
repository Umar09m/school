from django.apps import AppConfig


class EmployessConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'employess'

    def ready(self):
        import employess.signal