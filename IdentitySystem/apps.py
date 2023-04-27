from django.apps import AppConfig


class IdentitysystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'IdentitySystem'

    def ready(self):
        from .models import Region
        if Region.objects.count() == 0:
            Region.objects.create(
                name='CENTRE'
            )
            Region.objects.create(
                name='SUD'
            )
            Region.objects.create(
                name='LITTORAL'
            )
            Region.objects.create(
                name='EST'
            )
            Region.objects.create(
                name='OUEST'
            )
            Region.objects.create(
                name='NORD'
            )
            Region.objects.create(
                name='EXTREME-NORD'
            )
            Region.objects.create(
                name='ADAMAOUA'
            )
            Region.objects.create(
                name='NORD-OUEST'
            )
            Region.objects.create(
                name='SUD-OUEST'
            )
