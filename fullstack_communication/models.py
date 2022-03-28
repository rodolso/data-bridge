from django.db import models

# Create your models here.


class Companies(models.Model):
    company_id = models.IntegerField()
    company_name = models.CharField(max_length=20, primary_key=True)
    type_company = models.CharField(max_length=8)

    class Meta:
        unique_together = (('company_id', 'company_name'),)


class Formularios(models.Model):
    employee_id = models.IntegerField()
    question_id = models.IntegerField()
    answer_id = models.IntegerField(null=True)
    company_id = models.ForeignKey(Companies, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('employee_id', 'question_id'),)


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=30)


class TypeResponses(models.Model):
    type_response = models.CharField(max_length=15)
    answer_id = models.IntegerField()
    answer_string = models.CharField(max_length=25)
    score = models.FloatField(null=True)

    class Meta:
        unique_together = (('type_response', 'answer_id'),)


class Results(models.Model):
    question_id = models.ForeignKey(Formularios, on_delete=models.CASCADE)
    question = models.CharField(max_length=140)
    type_company = models.CharField(max_length=3)
    result = models.FloatField()
    active = models.CharField(max_length=6)
    type_response = models.ForeignKey(TypeResponses, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('type_company', 'question_id'),)








