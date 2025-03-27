from django.shortcuts import render
from django.http import HttpResponse

def cars_view(request):
    html = '''
        <html>
            <head>
                <title>Meus Carros</title>
            </head>
            <body>
                <h1>Carros da Chagas Revendas</h1>
                <h3>Só carro top!</h3>
            </body>
        </html>
    '''

    return HttpResponse(html)
