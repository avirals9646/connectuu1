from django.db import models

# Create your models here.
from django.db import models

class Alumni(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    graduation_year = models.PositiveIntegerField()
    degree_program = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    occupation = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    linkedin_profile = models.URLField(blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.graduation_year}"
