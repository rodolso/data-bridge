# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# import json


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
    return HttpResponse('Data Science API is online')
    # return render(request, "index.html")


@csrf_exempt
def post_company(request):
    # return HttpResponse('POST Company is online')
    return JsonResponse(request.POST)  # it only fetches parameters from the BODY


@csrf_exempt
def post_user(request):
    # return HttpResponse('POST User is online')
    return JsonResponse(request.POST)  # it only fetches parameters from the BODY


@csrf_exempt
def post_answers(request):
    # return HttpResponse('POST Answers is online')
    return JsonResponse(request.POST)  # it only fetches parameters from the BODY


def get_form(request):
    form_dict = [
        {
            "question_id": 1,
            "question": "¿Ha establecido su empresa un diálogo con los grupos o partes interesadas en materia de sostenibilidad?",
            "answer_id": [0, 1, 2, 3],
            "answer": ["Nada", "Poco", "Medio", "Alto"]
        },
        {
            "question_id": 2,
            "question": "Por favor, describa en qué medida su empresa alinea sus acciones de sostenibilidad con los ODS:",
            "answer_id": [0, 1, 2, 3, 4],
            "answer": ["Nada", "Poco", "Medio", "Alto", "Muy alto"]
        },
        {
            "question_id": 3,
            "question": "¿Su empresa forma parte de alguna alianza, organización o asociación de promoción de la sostenibilidad?",
            "answer_id": [1, 0],
            "answer": ["Sí", "No"]
        }
    ]
    return JsonResponse(form_dict, safe=False)


def get_ranking(request):
    ranking_dict = [
        {
            "company_name": "Lady Rogers S.A.",
            "score": 9.2
        },
        {
            "company_name": "Gerahara S.A.",
            "score": 9.1
        },
        {
            "company_name": "Hasbulla Magomedov S.L.",
            "score": 9.0
        },
        {
            "company_name": "Puntuación media",
            "score": 6.4
        }
    ]
    return JsonResponse(ranking_dict, safe=False)


def get_stats(request):
    stats_dict = [
        {
            "category_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "category_name": ["Compromiso",
                              "Política y RSC",
                              "Derechos Humanos",
                              "Sostenibilidad Estructural",
                              "Presupuesto Sostenibilidad",
                              "Innovación",
                              "Proveedores",
                              "Medio Ambiente",
                              "Personas",
                              "Acción Social"
                              ]
        },
        {
            "company_name": "Puntuación media",
            "mean_score": {1: 6.0,
                           2: 5.5,
                           3: 6.0,
                           4: 5.5,
                           5: 6.0,
                           6: 5.5,
                           7: 6.0,
                           8: 5.5,
                           9: 6.0,
                           10: 5.5}
        },
        {
            "company_name": "Hasbulla Magomedov S.L.",
            "mean_score": {1: 9.0,
                           2: 9.0,
                           3: 9.0,
                           4: 9.0,
                           5: 9.5,
                           6: 8.5,
                           7: 9.5,
                           8: 8.5,
                           9: 9.5,
                           10: 8.5}
        }

    ]
    return JsonResponse(stats_dict, safe=False)
