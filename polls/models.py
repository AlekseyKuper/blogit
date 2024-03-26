from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название')

    def __str__(self):
        return self.name

class Tests(models.Model):
    test_name = models.CharField(verbose_name='Название')

    category = models.ForeignKey('Categories', on_delete=models.CASCADE, verbose_name='Название')

    def __str__(self):
        return self.test_name

class Questions(models.Model):
    question_name = models.CharField(verbose_name='Название')

    test = models.ForeignKey('Tests', on_delete=models.CASCADE, verbose_name='Название')

    def __str__(self):
        return self.question_name

class Answers(models.Model):
    answers_name = models.CharField(verbose_name='Название')
    exist = models.BooleanField(default=True, verbose_name='Правильный вариант ответа')

    question = models.ForeignKey('Questions', on_delete=models.CASCADE, verbose_name='Название')

    def __str__(self):
        return self.answers_name