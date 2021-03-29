from django.db import models

# Create your models here.
class Timetabels(models.Model):
    course_id = models.IntegerField(verbose_name='ID Курса')
    day_week = models.IntegerField(verbose_name='День недели')
    timetable = models.TextField(verbose_name="Расписание")
    is_odd = models.BooleanField(verbose_name='Четность недели')

    class Meta:
        verbose_name="Расписание"
        verbose_name_plural="Расписание"
    def __str__(self):
        return self.timetable



class Person(models.Model):
    user_id = models.IntegerField(unique=True, verbose_name='ID Пользователя')
    course_id = models.IntegerField(verbose_name='ID Курса')
    notify = models.BooleanField(verbose_name='Уведомления')

    class Meta:
        verbose_name="Пользователь"
        verbose_name_plural="Пользователи"

    def __str__(self):
        return str(self.user_id)

class Build(models.Model):
    mill = models.CharField(max_length=20)
    def __str__(self):
        return self.mill

