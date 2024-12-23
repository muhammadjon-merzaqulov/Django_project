from django.db import models


# Create your models here.
class Company(models.Model):
    title = models.CharField(max_length=100)
    about = models.TextField()

    def __str__(self):
        return self.title


class Worker(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

    def get_image(self):
        return self.image.url

