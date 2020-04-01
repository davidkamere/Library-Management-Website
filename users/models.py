from django.db import models
from django.contrib.auth.models import User


# Create your models here
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.IntegerField()
    phone_number = models.IntegerField()

    def __str__(self):
        return "%s" % self.user.username
