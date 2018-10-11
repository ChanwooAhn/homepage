from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    article = MarkdownxField()
    created_date = models.DateTimeField(default=timezone.now())
    pub_date = models.DateTimeField(default=timezone.now(), null=True)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
