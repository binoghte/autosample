from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager


class TemplateText(models.Model):
    title = models.CharField(max_length=45)
    text = models.CharField(max_length=2500)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=45)

    def __str__(self):
        return self.title