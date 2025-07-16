from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    photo = models.ImageField(upload_to="imgs")
    designation = models.CharField(max_length=128)
    email_address = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)  # Optional field

    # Creating timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)