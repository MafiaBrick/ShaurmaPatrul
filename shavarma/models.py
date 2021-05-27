from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class shavarmaModel(models.Model):
    title = models.CharField(max_length=200)
    memo = models.TextField(blank=True)
    image = models.ImageField(upload_to='shavarma/images')
    rating = models.FloatField(default = 1)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Точка"
        verbose_name_plural = "Точки"


class positionOfPoint(models.Model):
    id_point = models.ForeignKey('shavarmaModel', on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    rating = models.FloatField(default = 1)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Позиция"
        verbose_name_plural = "Позиции"

class comment(models.Model):
    point = models.ForeignKey('positionOfPoint', on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    com = models.TextField(blank=True)
    tasty = models.FloatField()
    struct = models.FloatField()
    orig = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"
