from django.db import models

# Create your models here.
class Timetabels(models.Model):
    course_id = models.IntegerField(verbose_name='ID Курса')
    day_week = models.IntegerField(verbose_name='День недели')
    timetable = models.CharField(max_length=200,verbose_name="Расписание")
    is_odd = models.BooleanField(verbose_name='Четность недели')

    class Meta:
        verbose_name="Расписание"
        verbose_name_plural="Расписание"
    def __str__(self):
        return self.timetable



class Person(models.Model):
    user_id = models.IntegerField(unique=True, verbose_name='ID Пользователя')
    course_id = models.IntegerField(verbose_name='ID Курса')
    build_id = models.ForeignKey('Build', on_delete=models.DO_NOTHING, verbose_name='Корпус')
    notify = models.BooleanField(verbose_name='Уведомления')

    class Meta:
        verbose_name="Пользователь"
        verbose_name_plural="Пользователи"

    def __str__(self):
        return self.user_id

class Build(models.Model):
    mill = models.CharField(max_length=20)
    def __str__(self):
        return self.mill

