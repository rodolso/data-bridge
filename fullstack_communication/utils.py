import pandas as pd
import numpy as np
import operator
import json
from fullstack_communication import models

def load_results():
    results_df = pd.DataFrame(list(models.Results.objects.all().values()))
    results_df = results_df.rename(columns={'category_id_id':'category_id',
                                            'question_id_id':'question_id',
                                            'type_response_id': 'type_response'})
    return results_df


def load_formularios():
    formularios_df = pd.DataFrame(list(models.Formularios.objects.all().values()))
    formularios_df = formularios_df.rename(columns={'company_id_id':'company_id'})
    return formularios_df


def load_type_responses():
    type_responses_df = pd.DataFrame(list(models.TypeResponses.objects.all().values()))
    return type_responses_df


def load_category():
    category_df = pd.DataFrame(list(models.Category.objects.all().values()))
    return category_df


def load_companies():
    companies_df = pd.DataFrame(list(models.Companies.objects.all().values()))
    return companies_df


def global_value_cers():
    df_results = pd.read_excel('/Users/auxi/Documents/bbdd_project.xlsx', sheet_name='results')
    global_value_cers = df_results.loc[df_results.type_company == 'TOTAL', 'result'].mean()
    dict_global_value_cers = {'CERS:':global_value_cers}
    return dict_global_value_cers

def category_value_cers():
    df_results = pd.read_excel('/Users/auxi/Documents/bbdd_project.xlsx', sheet_name='results')
    df_category = pd.read_excel('/Users/auxi/Documents/bbdd_project.xlsx', sheet_name='category')
    df_cat = pd.merge(df_results, df_category, how='left', on='category_id')
    df_cers_categories = pd.DataFrame((df_cat.groupby([df_cat.type_company, df_cat.category_id, df_cat.category_name])['result'].mean()).loc['TOTAL',:])
    df_cers_categories = df_cers_categories.reset_index()
    df_cers_categories = df_cers_categories[['category_id','category_name', 'result']]
    dict_cers_category = df_cers_categories.to_dict(orient='records')
    return df_cers_categories

def company_mean_total(company_id:int):
    df_results = pd.read_excel('/Users/auxi/Documents/bbdd_project.xlsx', sheet_name='results')
    df_type_responses = pd.read_excel('/Users/auxi/Documents/bbdd_project.xlsx', sheet_name='type_responses')
    df_formularios = pd.read_excel('/Users/auxi/Documents/bbdd_project.xlsx', sheet_name='formularios')
    df_form =df_formularios[['question_id', 'answer_id', 'company_id']]
    df_resu = df_results[['question_id', 'type_response']]
    df_type= df_type_responses[['type_response', 'answer_id', 'score']]
    df_merge_1= pd.merge(df_form,df_resu, how='left', on='question_id')
    df_merge_total = pd.merge(df_merge_1,df_type, how='left', on=['answer_id','type_response'])
    company_value = df_merge_total.groupby('company_id').mean()['score'][company_id]
    dict_value = {company_id: company_value}
    return dict_value


def ranking():
    df_companies = pd.read_excel('/Users/auxi/Documents/bbdd_project.xlsx', sheet_name='companies')

    ranking_list = []
    for c_id in df_companies.company_id:
        cmt = company_mean_total(c_id)
        f_name_company = df_companies.company_id == c_id
        company_name = df_companies.loc[f_name_company, 'company_name'].values[0]
        dict_company = {'company_name': company_name, 'value': cmt[c_id]}
        ranking_list.append(dict_company)

    df_ranking = pd.DataFrame(ranking_list)
    df_ranking = df_ranking.sort_values(by=['value'], ascending=False)
    dict_ranking = df_ranking.to_dict(orient='records')

    return dict_ranking

def company_mean_category(company_id:int):
    df_results = pd.read_excel('/Users/auxi/Documents/bbdd_project.xlsx', sheet_name='results')
    df_type_responses = pd.read_excel('/Users/auxi/Documents/bbdd_project.xlsx', sheet_name='type_responses')
    df_formularios = pd.read_excel('/Users/auxi/Documents/bbdd_project.xlsx', sheet_name='formularios')
    df_form =df_formularios[['question_id', 'answer_id', 'company_id']]
    df_resu = df_results[['question_id', 'type_response','category_id']]
    df_type= df_type_responses[['type_response', 'answer_id', 'score']]
    df_merge_1= pd.merge(df_form,df_resu, how='left', on='question_id')
    df_merge_total = pd.merge(df_merge_1,df_type, how='left', on=['answer_id','type_response'])
    company_value = pd.DataFrame(df_merge_total.groupby(['company_id','category_id']).mean()['score'].loc[company_id])
    company_value = company_value.reset_index()
    dict_category_values_company = company_value.to_dict(orient='records')
    return company_value


def cers_vs_company_categories(company_id: int):
    df_cers_categories = category_value_cers()

    df_score_result = pd.merge(df_cers_categories, company_mean_category(company_id), how='left', on='category_id')

    category_value_list = []

    for index, row in df_score_result.iterrows():
        form_dict_categories = {'category_id': row['category_id'], 'category_name': row['category_name'],
                                'score': [row['result'], row['score']]}
        category_value_list.append(form_dict_categories)
    return category_value_list


def load_form():
    df_results = pd.read_excel('/Users/auxi/Documents/bbdd_project.xlsx', sheet_name='results')
    df_type_responses = pd.read_excel('/Users/auxi/Documents/bbdd_project.xlsx', sheet_name='type_responses')
    df_left_resp = df_results.loc[df_results.type_company=='TOTAL',['question_id','question','type_response']]
    df_right_resp = df_type_responses.loc[:,['type_response','answer_id', 'answer_string']]
    df_merge_resp = pd.merge(df_left_resp, df_right_resp, how='left', on='type_response')
    df_all = df_merge_resp.loc[:,['question_id','question','answer_string','answer_id']]
    df_ok = pd.DataFrame(df_all.groupby(['question_id','question'])['answer_id'].apply(list))
    df_ok = df_ok.reset_index()
    df_oky = pd.DataFrame(df_all.groupby(['question_id','question'])['answer_string'].apply(list))
    df_oky = df_oky.reset_index()
    df_form = pd.merge(df_ok,df_oky, how='left', on=['question_id','question'])
    return df_form


def form():
    df_form = load_form()

    form_list = []
    for index, row in df_form.iterrows():

        row_answer_id = row['answer_id']
        row_answer_string = row['answer_string']
        list_dict = []
        for id_, string in zip(row_answer_id, row_answer_string):
            list_dict.append({'id': id_, 'content': string})

        form_dict = {'question': {'id': row['question_id'], 'content': row['question']}, 'answer': list_dict}
        form_list.append(form_dict)
    return form_list
