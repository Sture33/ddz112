from django.db import models

# Create your models here.
class Student(models.Model):

    instruments = [
        ('Фортепиано', 'Фортепиано'),
        ('Гитара', 'Гитара'),
        ('Скрипка', 'Скрипка')
    ]

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    course = models.CharField(max_length=255)
    music_instrument = models.CharField(max_length=255, choices=instruments)
    grade = models.CharField(max_length=255,default=1, choices=[(str(i),str(i)) for i in range(1,13)])
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} {self.surname}'
