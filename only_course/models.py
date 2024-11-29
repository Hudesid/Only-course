from django.core.exceptions import ValidationError
from django.db import models

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    specialty = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_at = models.DateField()
    end_at = models.DateField()
    teacher = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='course')

    def clean(self):
        if self.start_at > self.end_at:
            raise ValidationError({'non_field_errors': "Kursning boshlanish sanasi tugash sanasidan oldin bo'lishi kerak"})

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lesson')
    order = models.IntegerField()

    def clean(self):
        if self.order < 0:
            raise ValidationError({'order': "Tartib raqami musbat butun son bo'lishi kerak."})