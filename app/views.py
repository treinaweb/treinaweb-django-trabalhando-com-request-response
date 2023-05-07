from django.shortcuts import redirect
from django.template import loader
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request: HttpRequest) -> HttpResponse:
    # return HttpResponseRedirect("http://localhost:8000/outra-rota")
    return redirect("outra_rota")


def outra_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(content="<h1>Outra rota</h1>")