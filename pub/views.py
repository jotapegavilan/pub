from django.http import HttpResponse
import datetime
def saludo(request):
    return HttpResponse("Hola alumnos esta es nuestra primera pagina con django")

def despedida(request):
    return HttpResponse("<h1>Hasta pronto alumnos de django</h1>");

def getFecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """
    <html>
        <body>
            <h2>Fecha y hora actuales %s</h2>
        </body>
    </html>

    """ % fecha_actual
    return HttpResponse(documento)

def calcular_edad(request,edad,agno):
    edadActual = edad
    periodo = agno - 2020
    edad_futura = edadActual + periodo
    documento = """
    <html>
        <body>
            <h2>En el año %s tendras %s años</h2>
        </body>
    </html>

    """ % (agno,edad_futura)
    return HttpResponse(documento)