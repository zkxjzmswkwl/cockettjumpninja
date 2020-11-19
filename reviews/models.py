from django.db import models


class Mouse(models.Model):
    company = models.CharField(max_length=64, null=True, blank=True)
    model_name = models.CharField(max_length=32)
    weight = models.CharField(max_length=6)
    dimensions = models.CharField(max_length=8)
    button_count = models.IntegerField()

    def __str__(self):
        return f'{self.company} {self.model_name}'


class Keyboard(models.Model):
    company = models.CharField(max_length=64, null=True, blank=True)
    model_name = models.CharField(max_length=32)
    weight = models.CharField(max_length=10)
    dimensions = models.CharField(max_length=16)
    key_count = models.IntegerField()
    is_backlit = models.BooleanField()

    def __str__(self):
        return f'{company} {model_name}'