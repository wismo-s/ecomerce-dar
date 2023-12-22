from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
USER_MODEL = get_user_model()

class CustomUser(models.Model):
    user = models.OneToOneField(USER_MODEL, on_delete=models.CASCADE)
    distric = models.CharField(max_length=125, blank=True, null=False)
    department = models.CharField(max_length=80, blank=True, null=False)
    reference = models.CharField(max_length=150, blank=True, null=False)
    direction = models.CharField(max_length=300, blank=True, null=False)
    phone = models.CharField(max_length=20, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=False)
    