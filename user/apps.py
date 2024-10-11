from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
<<<<<<< HEAD
=======
    def ready(self):
        import user.signals
>>>>>>> 35b2c6c (upload project file)
