from django.db import models

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = "Задачи"


class intoxicated_drink(models.Model):
    rating = models.IntegerField(max_length=100, help_text="Рейтинг")
    name = models.CharField(max_length=50, help_text="Название")
    alcohol_percent = models.IntegerField(max_length=100, help_text="Содержание алкоголя")
