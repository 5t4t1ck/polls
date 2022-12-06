from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Estás en la página principal de Encuestas")


def detail(request, question_id):
    return HttpResponse(f"Estás viendo la pregunta número {question_id}")


def results(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta {question_id}")


def vote(request, question_id):
    return HttpResponse(f"Estás viendo a la pregunta número {question_id}")

