import pandas as pd
from django.db.models.base import ModelBase
from fullstack_communication.models import *

def insert(row: dict, model_class: ModelBase):
    """
    Insert a row in a table
    
    param row: A dictionary with all the necesary columns to insert
    param model_class: The class corresponding to the table model
    """
    insert = model_class(**row)
    insert.save()


[q.delete() for q in Companies.objects.all()]
[q.delete() for q in Formularios.objects.all()]
[q.delete() for q in Questions.objects.all()]
[q.delete() for q in CategoryMaster.objects.all()]
[q.delete() for q in Category.objects.all()]
[q.delete() for q in TypeResponses.objects.all()]
[q.delete() for q in Results.objects.all()]
    
companies = pd.read_excel('bbdd_project.xlsx', sheet_name='companies')
companies_dict = companies.to_dict(orient='records')

for row in companies_dict:
    insert(row, Companies)


category = pd.read_excel('bbdd_project.xlsx', sheet_name='category')
category_dict = category.to_dict(orient='records')

for row in category_dict:
    insert(row, Category)


category_master = pd.read_excel('bbdd_project.xlsx', sheet_name='category_master')
category_master_dict = category_master.to_dict(orient='records')

for row in category_master_dict:
    insert(row, CategoryMaster)


questions = pd.read_excel('bbdd_project.xlsx', sheet_name='questions')
questions_dict = questions.to_dict(orient='records')

for row in questions_dict:
    insert(row, Questions)

formularios = pd.read_excel('bbdd_project.xlsx', sheet_name='formularios')
formularios['datetime'] = formularios['datetime'].astype(str)
formularios_dict = formularios.to_dict(orient='records')

for row in formularios_dict:
    row['company_id'] = Companies.objects.filter(company_id=row['company_id']).first()
    row['question_id'] = Questions.objects.filter(question_id=row['question_id']).first()
    insert(row, Formularios)
    

type_responses = pd.read_excel('bbdd_project.xlsx', sheet_name='type_responses')
type_responses_dict = type_responses.to_dict(orient='records')

for row in type_responses_dict:
    row['type_response'] = CategoryMaster.objects.filter(type_response=row['type_response']).first()
    insert(row, TypeResponses)
    
    
results = pd.read_excel('bbdd_project.xlsx', sheet_name='results')
results_dict = results.to_dict(orient='records')

for row in results_dict:
    row['question_id'] = Questions.objects.filter(question_id=row['question_id']).first()
    row['type_response'] = CategoryMaster.objects.filter(type_response=row['type_response']).first()
    row['category_id'] = Category.objects.filter(category_id=row['category_id']).first()
    insert(row, Results)

