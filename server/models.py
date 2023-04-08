from django.db import models


class Direction(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Target(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    third_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(primary_key=True, unique=True)
    phone = models.CharField(max_length=20)
    direction_list = [
        ('iOS разработчик', 'iOS разработчик'),
        ('системный аналитик', 'системный аналитик'),
        ('администратор баз данных', 'администратор баз данных'),
        ('разработчик баз данных', 'разработчик баз данных'),

    ]
    direction = models.CharField(max_length=100, choices=direction_list, verbose_name='Выберите направление')
    status_list = [
        ('студент ВУЗа', 'студент ВУЗа'),
        ('студент СПО', 'студент СПО'),

    ]
    status = models.CharField(max_length=100, choices=status_list, verbose_name='Выберите направление')

    target_list = [
        ('Практика', 'Практика'),
        ('Стажировка', 'Стажировка'),

    ]
    target = models.CharField(max_length=100, choices=target_list, verbose_name='Выберите направление')


def __str__(self):
    return self.name


class Questtion(models.Model):
    name = models.TextField()
    answer = models.TextField()
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserAnswer(models.Model):
    question_id = models.ForeignKey(Questtion,on_delete=models.CASCADE)
    answer = models.TextField()

    def __str__(self):
        return self.answer
