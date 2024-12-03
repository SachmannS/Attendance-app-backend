from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Organisation(models.Model):
    name = models.CharField(max_length = 200, null = False, blank = True)

    def __str__(self):
        return self.name

class Profile(AbstractUser):
    org = models.ForeignKey(Organisation, on_delete = models.CASCADE, null = True)
    employee_id = models.CharField(max_length = 10, blank = True, null = True)
    is_company_admin = models.BooleanField(default = False, blank = False)
    phone_number = models.CharField(max_length = 15, blank = True, null = True)

