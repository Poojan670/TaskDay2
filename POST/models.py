from django.db import models
import uuid
from userservice.models import User


# Create your models here.

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_no = models.BigIntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    # def __str__(self):
    #    return id
