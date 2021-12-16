import enum
from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings


# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_no = models.BigIntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    # Enum Assignment
    # SUPERADMIN = 1
    # ADMIN = 2
    # CUSTOMER = 3
    ROLES_CHOICES = (
        ('S', 'SuperAdmin'),
        ('A', 'Admin'),
        ('C', 'Customer'),
    )
    roles = models.CharField(max_length=100, choices=ROLES_CHOICES, blank=False)


class Roles(models.Model):
    STATUS_CHOICES = (
        ('S', 'SuperAdmin'),
        ('A', 'Admin'),
        ('C', 'Customer'),
    )
    your_role = models.CharField(max_length=100, choices=STATUS_CHOICES, default="Customer")
    user = models.ManyToManyField(User, related_name="user", blank=False)
