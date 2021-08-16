from django.db import models
from shortener_app.utils import get_random_alias

# Create your models here.

ALIAS_LENGTH = 8


class AliasedUrl(models.Model):
    alias = models.CharField(primary_key=True,
                             max_length=ALIAS_LENGTH,
                             default=get_random_alias)
    url = models.URLField(blank=False)

    def __str__(self):
        return f"{self.alias} -> {self.url}"
