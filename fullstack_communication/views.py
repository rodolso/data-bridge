from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


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


@csrf_exempt
def post_company(request):
    # return HttpResponse('POST Company is online')
    # return HttpResponse(json.dumps(request.GET))
    return JsonResponse(request.GET)


@csrf_exempt
def post_user(request):
    return HttpResponse('POST User is online')


@csrf_exempt
def post_answers(request):
    return HttpResponse('POST Answers is online')


def get_form(request):
    return HttpResponse('GET Form is online')


def get_ranking(request):
    return HttpResponse('GET Ranking is online')


def get_stats(request):
    return HttpResponse('GET Stats is online')
