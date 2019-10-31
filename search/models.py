from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    # src  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # title = models.CharField(max_length=200)
    # text = models.TextField()
    # created_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)
    src = models.CharField(max_length = 10)
    des = models.CharField(max_length = 10)
    doj = models.DateTimeField(default = timezone.now)
    hashTravel = models.CharField(max_length = 100)
    sampleData = models.CharField(max_length = 100)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    # def __str__(self):
    #     return self.title

