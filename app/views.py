import json
from django.shortcuts import render
from django.template import loader
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request: HttpRequest) -> HttpResponse:
    # body = loader.render_to_string("app/home.html", context=None, request=request)
    template = loader.get_template("app/home.html")
    body = template.render(context=None, request=request)
    print(f"GET: {request.GET}")
    print(f"POST: {request.POST}")
    print(f"Body: {request.body}")
    body_dict = json.loads(request.body)
    print(body_dict)
    return HttpResponse(body)