from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from fullstack_communication import models
from fullstack_communication import utils
import sys

# Create your views here.
# As shown in the examples.
#
#
# def newapp_hello(request):
#     # return HttpResponse('Hello from Python!')
#     return render(request, 'newapp_hello.html')
#
#
# def capture_params(request):
#     return HttpResponse(
#         json.dumps(request.GET),
#         content_type='application/javascript; charset=utf8'
#     )


def index(request):
    return render(request, "base_ds.html")


@csrf_exempt
def post_company(request):
    q = dict(request.POST.items())

    insert = models.Companies(**q)
    insert.save()

    return HttpResponse("Success!!")



@csrf_exempt
def post_user(request):
    # return HttpResponse('POST User is online')
    return JsonResponse(request.POST)  # it only fetches parameters from the BODY


@csrf_exempt
def post_answers(request):

    def insert_item(item):

        item['employee_id'] = int(item['employee_id'])
        item['question_id'] = int(item['question_id'])
        item['question_id'] = models.Questions.objects.filter(
            question_id=item['question_id']).first()
        item['answer_id'] = int(item['answer_id'])
        item['company_id'] = models.Companies.objects.filter(
            company_id=item['company_id']).first()
        insert = models.Formularios(**item)
        insert.save()

    if request.headers['Content-Type'] == 'application/json':
        json_loads = json.loads(request.body.decode('ascii'))
        for item_i in json_loads:
            insert_item(item_i)
    else:
        item_i = dict(request.POST.items())
        insert_item(item_i)


    return HttpResponse("Success!!")


def get_form(request):

    form_dict = utils.form()
    return JsonResponse(form_dict, safe=False)


def get_ranking(request):
    ranking_dict = utils.ranking()
    return JsonResponse(ranking_dict, safe=False)


def get_stats(request):
    company_id = request.GET.get("company_id")
    stats_dict = utils.cers_vs_company_categories(company_id)
    return JsonResponse(stats_dict, safe=False)

