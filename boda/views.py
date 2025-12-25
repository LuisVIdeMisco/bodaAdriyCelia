import re
from django.utils.timezone import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(
        request,
        "boda/home.html"
    )

def hola_buenas(request, name):
    """ now = datetime.now()
    formatted_time = now.strftime("%Y, %d %B, %Y a las %X")

    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "amego"
    
    content = "Hola buenas" + clean_name + "! Es el " + formatted_time
    return HttpResponse(content) """
    print(request.build_absolute_uri())
    return render(
        request,
        'boda/prueba.html',
        {
            'name': name,
            'date': datetime.now(),
        }
    )

def evento(request):
    return render(
        request,
        'boda/bodaAdriyCelia.ics',
        content_type="text/calendar"
    )
