from django.apps import AppConfig

class WebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'web'

    def ready(self):
        # This method can be used to import signals or other necessary startup setup.
        pass

class BackendHospitalConfig(AppConfig):
    name = 'backend_hospital'
    verbose_name = 'Backend Hospital'

    def ready(self):
        # This method can also be used for specific startup activities related to this app.
        pass