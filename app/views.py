from django.http import HttpRequest, HttpResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request: HttpRequest) -> HttpResponse:
    # with open('relatorio.pdf', 'rb') as file:
    #     return HttpResponse(
    #         content=file.read(), 
    #         content_type="application/pdf",
    #         headers={"Content-Disposition": "attachment; filename='relatorio.pdf'"}
    #     )
    return FileResponse(open('relatorio.pdf', 'rb'), as_attachment=True, filename='outro_nome.pdf')


def outra_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(content="<h1>Outra rota</h1>")