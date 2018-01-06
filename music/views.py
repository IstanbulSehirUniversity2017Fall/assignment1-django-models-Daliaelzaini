
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>this will be a list of all albums</h1>")


def details(request, album_id):
    return HttpResponse("<h2> album id details:" +str(album_id) + "</h2>")