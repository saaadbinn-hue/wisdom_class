from django.db import models

# Create your models here.

class Enquiry(models.Model):
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    city = models.CharField(max_length=100)

    current_class = models.CharField(max_length=50)
    school = models.CharField(max_length=200, blank=True, null=True)

    course = models.CharField(max_length=100)
    batch = models.CharField(max_length=50)
    mode = models.CharField(max_length=50)

    message = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
