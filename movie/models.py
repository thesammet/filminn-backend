from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length = 100)
    category = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200)
    year = models.CharField(max_length = 4)
    imdbRate = models.PositiveIntegerField(
        validators = [MinValueValidator(1), MaxValueValidator(10)],
    )
    imageUrl = models.CharField(max_length = 150)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default=True)

    def __str__(self) :
        return self.title
