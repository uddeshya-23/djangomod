from django.db import models
from django.core.validators import (
    EmailValidator,
    MaxValueValidator,
    MinValueValidator,
    URLValidator,
    validate_slug
    )

from main.validators import(
    validate_even_number
    )


# Create your models here.
# evry table in db is represented as a class
# every row in db is represented by an object of this class

class Student(models.Model):
    GENDERS = (
        ('F', 'FEMALE'),
        ('M', 'MALE'),
        ('UN', 'NOT PREFER TO SAY')
        )
    name = models.CharField(max_length = 100)
    roll_number = models.IntegerField(unique = True)
    #integer
    #can be null in db
    #can be null in ORM
    

    dob = models.CharField(max_length = 100)
    age = models.IntegerField(null = True, validators = [MaxValueValidator(100), MinValueValidator(10), validate_even_number])
    department = models.CharField(max_length = 100)
    address = models.TextField(null = True, blank = True)
    contact_number = models.CharField(max_length = 15, null = True)
    email = models.EmailField(null = True, validators = [EmailValidator("Email address is not valid")])
    gender = models.CharField(max_length = 2, choices= GENDERS, null = True)

    slug = models.CharField(max_length = 100, validators = [validate_slug], null = True)
    def __str__(self):
        return self.name
    