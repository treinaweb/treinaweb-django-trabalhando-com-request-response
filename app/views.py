import json
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request: HttpRequest) -> HttpResponse:
    # body = json.dumps({"nome": "Cleyson", "sobrenome": "Lima"})
    # return HttpResponse(content=body, content_type="application/json", charset="utf-8")
    body = [
        {"nome": "Cleyson", "sobrenome": "Lima"},
        {"nome": "Ana", "sobrenome": "Beatriz"},
        {"nome": "Elton", "sobrenome": "Fonseca"}
    ]
    return JsonResponse(body, safe=False)


def outra_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(content="<h1>Outra rota</h1>")