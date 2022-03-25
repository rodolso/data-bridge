from django.db import models
from django import forms

# Create your models here.

class Companies(models.Model):
    company_id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=20)
    type_company = models.CharField(max_length=8)


class Formularios(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    question_id = models.IntegerField()
    score = models.FloatField()
    company_name = models.ForeignKey(Companies, on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    # class Meta:
    #     unique_together = (('employee_id', 'question_id', 'datetime',),)


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=30)


class Typeresponses(models.Model):
    type_response = models.CharField(max_length=15, primary_key=True)
    answer_id = models.IntegerField()
    answer_string = models.CharField(max_length=25)
    score = models.FloatField()

    class Meta:
        unique_together = (('type_response', 'answer_id'),)


class Results(models.Model):
    question_id = models.ForeignKey(Formularios, on_delete=models.CASCADE)
    question = models.CharField(max_length=140)
    type_company = models.CharField(max_length=3, primary_key=True)
    result = models.FloatField()
    active = models.CharField(max_length=6)
    type_response = models.ForeignKey(Typeresponses, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('type_company', 'question_id'),)








