from django.db import models

# Create your models here.


class Questions(models.Model):
    question_id = models.IntegerField(unique=True, primary_key=True)
    question = models.CharField(max_length=140, unique=True)
    type_response_id = models.IntegerField()

    class Meta:
        unique_together = (('question_id', 'question'),)


class CategoryMaster(models.Model):
    type_response = models.CharField(max_length=15, unique=True)
    response_id = models.IntegerField(primary_key=True, unique=True)

    class Meta:
        unique_together = (('type_response', 'response_id'),)


class Companies(models.Model):
    company_id = models.CharField(max_length=30, primary_key=True, unique=True)
    company_name = models.CharField(max_length=20, unique=True)
    type_company = models.CharField(max_length=8)

    class Meta:
        unique_together = (('company_id', 'company_name'),)


class Formularios(models.Model):
    employee_id = models.IntegerField()
    question_id = models.ForeignKey(Questions, to_field='question_id', on_delete=models.CASCADE)
    answer_id = models.IntegerField(null=True)
    company_id = models.ForeignKey(Companies, to_field='company_id', on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('employee_id', 'question_id', 'company_id', 'datetime'),)


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=30, unique=True)

    class Meta:
        unique_together = (('category_id', 'category_name'),)


class TypeResponses(models.Model):
    type_response = models.ForeignKey(CategoryMaster, to_field='type_response', on_delete=models.CASCADE)
    answer_id = models.IntegerField()
    answer_string = models.CharField(max_length=25)
    score = models.FloatField(null=True)

    class Meta:
        unique_together = (('type_response', 'answer_id', 'score'),)


class Results(models.Model):
    question_id = models.ForeignKey(Questions, to_field='question_id', on_delete=models.CASCADE)
    question = models.CharField(max_length=140)
    type_company = models.CharField(max_length=8)
    result = models.FloatField()
    active = models.CharField(max_length=6)
    type_response = models.ForeignKey(CategoryMaster, to_field='type_response', on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, to_field='category_id', on_delete=models.CASCADE)

