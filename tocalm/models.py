from django.conf import settings
from django.db import models


class Item(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    task = models.CharField(max_length=500)
    impact = models.IntegerField(default=1)
    done = models.BooleanField(default=False)
