from django.db import models
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

# Create your models here.


class JiraProject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default=None)

    def __str__(self) -> str:
        return self.name
    

    def clean_name(self):
        if self.name.isinstance('str'):
            return self.name
        raise ValidationError(f"{self.name} is not valid string")
    
    def clean_description(self):
        if self.description.isinstance('str'):
            return self.description
        raise ValidationError(f"{self.description} is not valid string")
    
