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

    q['company_id'] = int(q['company_id'])

    insert = models.Companies(**q)
    insert.save()

    return HttpResponse("Success!!")



@csrf_exempt
def post_user(request):
    # return HttpResponse('POST User is online')
    return JsonResponse(request.POST)  # it only fetches parameters from the BODY


@csrf_exempt
def post_answers(request):
    q = dict(request.POST.items())

    q['employee_id'] = int(q['employee_id'])
    q['question_id'] = int(q['question_id'])
    q['question_id'] = models.Questions.objects.filter(question_id=q['question_id']).first()
    q['answer_id'] = int(q['answer_id'])
    q['company_id'] = int(q['company_id'])
    q['company_id'] = models.Companies.objects.filter(company_id=q['company_id']).first()

    insert = models.Formularios(**q)
    insert.save()

    return HttpResponse("Success!!")


def get_form(request):

    form_dict = utils.form()
    return JsonResponse(form_dict, safe=False)


def get_ranking(request):
    ranking_dict = utils.ranking()
    return JsonResponse(ranking_dict, safe=False)


def get_stats(request):
    x = int(request.GET.get("company_id"))
    print(x, sys.stdout)
    stats_dict = utils.cers_vs_company_categories(x)
    return JsonResponse(stats_dict, safe=False)

