from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=16, unique=True)
    description = models.TextField(max_length=200)
    def __str__(self):
        return self.name

class Homebrew(models.Model):
    title = models.CharField(max_length=26)
    summary = models.TextField(max_length=200)
    jobs = models.ForeignKey(Job, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def sum(self):
        return self.summary[:64]+"..."

    def pub_date(self):
        return self.date.strftime('%e %B, %Y')