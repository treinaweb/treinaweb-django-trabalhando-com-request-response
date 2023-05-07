from django.shortcuts import render
from django.template import loader
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request: HttpRequest) -> HttpResponse:
    # body = loader.render_to_string("app/home.html", context=None, request=request)
    template = loader.get_template("app/home.html")
    body = template.render(context=None, request=request)
    print(f"Path: {request.path}")
    print(f"Path info: {request.path_info}")
    print(f"Method: {request.method}")
    print(f"Content type: {request.content_type}")
    print(f"Header: {request.headers}")
    # print(f"META: {request.META}")
    print(f"Session: {request.session.items()}")
    print(f"User: {request.user}")
    print(f"Host: {request.get_host()}")
    print(f"Port: {request.get_port()}")
    print(f"Full path: {request.get_full_path()}")
    print(f"Full path info: {request.get_full_path_info()}")
    print(f"Is secure: {request.is_secure()}")
    print(f"Accepts: {request.accepts('application/json')}")
    return HttpResponse(body)