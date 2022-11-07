from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

def validate_stroke(stroke):
    if stroke not in ['front crawl', 'butterfly', 'breast', 'back','freestyle']:
        raise ValidationError(f"{stroke} is not a valid stroke")

class SwimRecord(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    team_name = models.CharField(max_length=255)
    relay = models.BooleanField()
    stroke = models.CharField(max_length=255, validators=[validate_stroke])
    distance = models.IntegerField(validators=[MinValueValidator(50)])
    record_date = models.DateTimeField(validators=[MaxValueValidator(timezone.now(), "Can't set record in the future.")])
    record_broken_date = models.DateTimeField()