from django.template import loader
from django.http import HttpRequest, HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return HttpResponse("<h1>Tudo certo!</h1>")
    return HttpResponseNotAllowed(permitted_methods=["GET"])