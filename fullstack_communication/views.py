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
      "content": "\\u00bfHa establecido su empresa un di\\u00e1logo con los grupos o partes interesadas en materia de sostenibilidad?"
    },
    "answer": [
      {
        "id": 0,
        "content": "nada"
      },
      {
        "id": 1,
        "content": "poco"
      },
      {
        "id": 2,
        "content": "medio"
      },
      {
        "id": 3,
        "content": "alto"
      }
    ]
  },
  {
    "question": {
      "id": 2,
      "content": "Por favor, describa en qu\\u00e9 medida la empresa alinea sus acciones de sostenibilidad con los ODS:"
    },
    "answer": [
      {
        "id": 0,
        "content": "nada"
      },
      {
        "id": 1,
        "content": "poco"
      },
      {
        "id": 2,
        "content": "medio"
      },
      {
        "id": 3,
        "content": "alto"
      },
      {
        "id": 4,
        "content": "muy alto"
      }
    ]
  },
  {
    "question": {
      "id": 3,
      "content": "\\u00bfForma parte de alguna alianza/organizaci\\u00f3n/asociaci\\u00f3n de promoci\\u00f3n de la sostenibilidad?\\u00a0 Puede seleccionar varias respuestas."
    },
    "answer": [
      {
        "id": 1,
        "content": "si"
      },
      {
        "id": 0,
        "content": "no"
      }
    ]
  },
  {
    "question": {
      "id": 4,
      "content": "\\u00bfCuenta su empresa con politica de sostenibilidad?"
    },
    "answer": [
      {
        "id": 1,
        "content": "si"
      },
      {
        "id": 0,
        "content": "no"
      }
    ]
  },
  {
    "question": {
      "id": 5,
      "content": "\\u00bfSu empresa tiene una estrategia de sostenibilidad y/o responsabilidad social corporativa?"
    },
    "answer": [
      {
        "id": 0,
        "content": "nada"
      },
      {
        "id": 1,
        "content": "poco"
      },
      {
        "id": 2,
        "content": "medio"
      },
      {
        "id": 3,
        "content": "alto"
      },
      {
        "id": 4,
        "content": "muy alto"
      }
    ]
  },
  {
    "question": {
      "id": 6,
      "content": "\\u00bfTiene su empresa una direccion de sostenibilidad especifica?"
    },
    "answer": [
      {
        "id": 1,
        "content": "si"
      },
      {
        "id": 0,
        "content": "no"
      }
    ]
  },
  {
    "question": {
      "id": 7,
      "content": "\\u00bfExiste una comision interdepartamental de sostenibilidad?"
    },
    "answer": [
      {
        "id": 1,
        "content": "si"
      },
      {
        "id": 0,
        "content": "no"
      }
    ]
  },
  {
    "question": {
      "id": 8,
      "content": "\\u00bfEn que medida cree que es adecuado el presuspuesto destinado a sostenibilidad?"
    },
    "answer": [
      {
        "id": 0,
        "content": "nada"
      },
      {
        "id": 1,
        "content": "poco"
      },
      {
        "id": 2,
        "content": "medio"
      },
      {
        "id": 3,
        "content": "alto"
      }
    ]
  },
  {
    "question": {
      "id": 9,
      "content": "\\u00bfTiene la empresa una pol\\u00edtica espec\\u00edfica de Derechos Humanos?"
    },
    "answer": [
      {
        "id": 1,
        "content": "si"
      },
      {
        "id": 0,
        "content": "no"
      }
    ]
  },
  {
    "question": {
      "id": 10,
      "content": "\\u00bfRealiza su empresa innovaci\\u00f3n con atributos de sostenibilidad?"
    },
    "answer": [
      {
        "id": 1,
        "content": "si"
      },
      {
        "id": 0,
        "content": "no"
      }
    ]
  },
  {
    "question": {
      "id": 11,
      "content": "\\u00bfHa adoptado pr\\u00e1cticas para evitar la competencia desleal?\\u00a0"
    },
    "answer": [
      {
        "id": 1,
        "content": "si"
      },
      {
        "id": 0,
        "content": "no"
      }
    ]
  },
  {
    "question": {
      "id": 12,
      "content": "\\u00bfDispone la empresa de una poli\\u0301tica medioambiental?"
    },
    "answer": [
      {
        "id": 1,
        "content": "si"
      },
      {
        "id": 0,
        "content": "no"
      }
    ]
  },
  {
    "question": {
      "id": 13,
      "content": "\\u00bfSe contempla la gestion de residuos en su pol\\u00edtica medioambiental?"
    },
    "answer": [
      {
        "id": 1,
        "content": "si"
      },
      {
        "id": 0,
        "content": "no"
      }
    ]
  },
  {
    "question": {
      "id": 14,
      "content": "\\u00bfSe contempla la eficiencia energetica en su pol\\u00edtica medioambiental?"
    },
    "answer": [
      {
        "id": 1,
        "content": "si"
      },
      {
        "id": 0,
        "content": "no"
      }
    ]
  },
  {
    "question": {
      "id": 15,
      "content": "\\u00bfTiene la empresa un plan de movilidad sostenible?"
    },
    "answer": [
      {
        "id": 0,
        "content": "nada"
      },
      {
        "id": 1,
        "content": "poco"
      },
      {
        "id": 2,
        "content": "medio"
      },
      {
        "id": 3,
        "content": "alto"
      }
    ]
  },
  {
    "question": {
      "id": 16,
      "content": "\\u00bfExisten acciones formativas espec\\u00edficas en sostenibilidad?"
    },
    "answer": [
      {
        "id": 0,
        "content": "no"
      },
      {
        "id": 1,
        "content": "en alguna ocasi\\u00f3n"
      },
      {
        "id": 2,
        "content": "si"
      }
    ]
  },
  {
    "question": {
      "id": 17,
      "content": "\\u00bfExiste en la empresa un plan de desarrollo profesional?"
    },
    "answer": [
      {
        "id": 0,
        "content": "nada"
      },
      {
        "id": 1,
        "content": "poco"
      },
      {
        "id": 2,
        "content": "medio"
      },
      {
        "id": 3,
        "content": "alto"
      }
    ]
  },
  {
    "question": {
      "id": 18,
      "content": "\\u00bfTiene la empresa un plan de igualdad?"
    },
    "answer": [
      {
        "id": 1,
        "content": "si"
      },
      {
        "id": 0,
        "content": "no"
      }
    ]
  },
  {
    "question": {
      "id": 19,
      "content": "\\u00bfHa adoptado la empresa medidas espec\\u00edficas sobre la brecha de g\\u00e9nero?"
    },
    "answer": [
      {
        "id": 0,
        "content": "no"
      },
      {
        "id": 1,
        "content": "en alguna ocasi\\u00f3n"
      },
      {
        "id": 2,
        "content": "si"
      }
    ]
  },
  {
    "question": {
      "id": 20,
      "content": "\\u00bfHa integrado la empresa los principios de accesibilidad universal?"
    },
    "answer": [
      {
        "id": 0,
        "content": "nada"
      },
      {
        "id": 1,
        "content": "poco"
      },
      {
        "id": 2,
        "content": "medio"
      },
      {
        "id": 3,
        "content": "alto"
      }
    ]
  },
  {
    "question": {
      "id": 21,
      "content": "\\u00bfSe realizan acciones de voluntariado corporativo?"
    },
    "answer": [
      {
        "id": 1,
        "content": "si"
      },
      {
        "id": 0,
        "content": "no"
      }
    ]
  },
  {
    "question": {
      "id": 22,
      "content": "\\u00bfTiene la empresa un plan de acci\\u00f3n social y cooperaci\\u00f3n al desarrollo?"
    },
    "answer": [
      {
        "id": 0,
        "content": "nada"
      },
      {
        "id": 1,
        "content": "poco"
      },
      {
        "id": 2,
        "content": "medio"
      },
      {
        "id": 3,
        "content": "alto"
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
