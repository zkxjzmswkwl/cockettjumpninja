from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


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
        return f'{self.company} {self.model_name}'


class MouseReview(models.Model):
    mouse = models.ForeignKey(Mouse, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    author = models.CharField(max_length=32, blank=False, null=False)
    body = models.TextField(max_length=15000, blank=False, null=False)

    def __str__(self):
        return f'{self.author} - {self.mouse.model_name}'


class KeyboardReview(models.Model):
    keyboard = models.ForeignKey(Keyboard, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    author = models.CharField(max_length=32, blank=False, null=False)
    body = models.TextField(max_length=15000, blank=False, null=False)

    def __str__(self):
        return f'{self.author} - {self.keyboard.model_name}'
