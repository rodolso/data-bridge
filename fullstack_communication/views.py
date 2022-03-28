from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from fullstack_communication import models
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

    print(q, sys.stdout)
    q['employee_id'] = int(q['employee_id'])
    q['question_id'] = int(q['question_id'])
    q['answer_id'] = int(q['answer_id'])
    q['company_id'] = models.Companies.objects.filter(company_id=q['company_id']).first()

    insert = models.Formularios(**q)
    insert.save()

    return HttpResponse("Success!!")


def get_form(request):
    form_dict = [
        {
            "question": {
                "id": 1,
                "content": "¿Ha establecido su empresa un diálogo con los grupos o partes interesadas en materia de sostenibilidad?"
            },
            "answer": [
                {
                    "id": 1,
                    "content": "Nada"
                },
                {
                    "id": 2,
                    "content": "Poco"
                },
                {
                    "id": 3,
                    "content": "Medio"
                },
                {
                    "id": 4,
                    "content": "Alto"
                }
            ]
        },
        {
            "question": {
                "id": 2,
                "content": "Por favor, describa en qué medida su empresa alinea sus acciones de sostenibilidad con los ODS:"
            },
            "answer": [
                {
                    "id": 1,
                    "content": "Nada"
                },
                {
                    "id": 2,
                    "content": "Poco"
                },
                {
                    "id": 3,
                    "content": "Medio"
                },
                {
                    "id": 4,
                    "content": "Alto"
                },
                {
                    "id": 5,
                    "content": "Muy alto"
                }
            ]
        },
        {
            "question": {
                "id": 3,
                "content": "¿Su empresa forma parte de alguna alianza, organización o asociación de promoción de la sostenibilidad?"
            },
            "answer": [
                {
                    "id": 1,
                    "content": "No"
                },
                {
                    "id": 2,
                    "content": "Sí"
                }
            ]
        }
    ]

    # form_dict = [
    #     {
    #         "question_id": 1,
    #         "question": "¿Ha establecido su empresa un diálogo con los grupos o partes interesadas en materia de sostenibilidad?",
    #         "answer_id": [0, 1, 2, 3],
    #         "answer": ["Nada", "Poco", "Medio", "Alto"]
    #     },
    #     {
    #         "question_id": 2,
    #         "question": "Por favor, describa en qué medida su empresa alinea sus acciones de sostenibilidad con los ODS:",
    #         "answer_id": [0, 1, 2, 3, 4],
    #         "answer": ["Nada", "Poco", "Medio", "Alto", "Muy alto"]
    #     },
    #     {
    #         "question_id": 3,
    #         "question": "¿Su empresa forma parte de alguna alianza, organización o asociación de promoción de la sostenibilidad?",
    #         "answer_id": [0, 1],
    #         "answer": ["No", "Sí"]
    #     }
    # ]
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
            "company_name": "Puntuación media CERS",
            "score": 6.4
        }
    ]
    return JsonResponse(ranking_dict, safe=False)


def get_stats(request):
    stats_dict = [
        {
            "category_id": 1,
            "category_name": "Compromiso",
            "score": [6.0, 9.0]
        },
        {
            "category_id": 2,
            "category_name": "Política y RSC",
            "score": [6.0, 9.0]
        },
        {
            "category_id": 3,
            "category_name": "Derechos Humanos",
            "score": [6.0, 9.0]
        },
        {
            "category_id": 4,
            "category_name": "Sostenibilidad Estructural",
            "score": [6.0, 9.0]
        },
        {
            "category_id": 5,
            "category_name": "Presupuesto Sostenibilidad",
            "score": [6.0, 9.0]
        },
        {
            "category_id": 6,
            "category_name": "Innovación",
            "score": [6.0, 9.0]
        },
        {
            "category_id": 7,
            "category_name": "Proveedores",
            "score": [6.0, 9.0]
        },
        {
            "category_id": 8,
            "category_name": "Medio Ambiente",
            "score": [6.0, 9.0]
        },
        {
            "category_id": 9,
            "category_name": "Personas",
            "score": [6.0, 9.0]
        },
        {
            "category_id": 10,
            "category_name": "Acción Social",
            "score": [6.0, 9.0]
        }
    ]
    return JsonResponse(stats_dict, safe=False)
