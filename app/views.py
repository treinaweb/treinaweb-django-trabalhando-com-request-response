from django.shortcuts import render
from django.template import loader
from django.http import HttpRequest, HttpResponse


def home(request: HttpRequest) -> HttpResponse:
    # body = loader.render_to_string("app/home.html", context=None, request=request)
    template = loader.get_template("app/home.html")
    body = template.render(context=None, request=request)
    return HttpResponse(body)