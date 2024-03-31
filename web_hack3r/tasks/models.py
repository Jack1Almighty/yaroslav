from django.conf import settings
from django.db import models


class Tasks(models.Model):
    Difficulty = (
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
        ('Extreme', 'Extreme')
    )

    Category = (
        ('Osint', 'Osint'),
        ('Reverse', 'Reverse'),
        ('Web', 'Web'),
        ('Crypto', 'Crypto'),
        ('Other', 'Other'),
    )

    TaskName = models.CharField('Название', max_length=50, default='')
    TaskDescription = models.TextField('Описание', default='')
    Task_key = models.CharField('Флаг', max_length=50, default='web_hack3r{}')
    Task_category = models.CharField('Категория', choices=Category, max_length=10, default='')
    Task_difficulty = models.CharField('Сложность', choices=Difficulty, max_length=10, default='')
    Task_href = models.URLField("Ссылка", null=True, blank=True)
    Task_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, verbose_name='Aвтор')

    def __str__(self):
        return self.TaskName

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-id']

