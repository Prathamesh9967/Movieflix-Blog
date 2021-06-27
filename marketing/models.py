from django.db import models

# Create your models here.
class Signup(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class contact(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    profile = models.ImageField(upload_to='contact')

    def __str__(self):
        return self.username