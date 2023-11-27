from django.db import models


class Post(models.Model):
    title = models.TextField(null=True, blank=True, default=None)
