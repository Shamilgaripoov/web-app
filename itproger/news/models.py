from django.db import models


class Articles(models.Model):
    title = models.CharField('Фамилия Имя Отчество', max_length=50)
    date = models.DateTimeField('Дата заезда')
    departure = models.DateTimeField('Дата выезда')
    full_text = models.TextField('Дополнительные пожелания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'
