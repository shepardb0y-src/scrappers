from django.db import models

# Create your models here.


class Link(models.Model):

    def __str__(self):
        if self.address and self.name:  # Check if both fields are not None
            return f"{self.address} - {self.name}"
        elif self.address:  # Check if only field1 is not None
            return self.address
        elif self.name:  # Check if only field2 is not None
            return self.name
        else:
            return "Unnamed Object"

    address = models.CharField(max_length=1000, null=True, blank=True)
    name = models.CharField(max_length=1000, null=True, blank=True)
