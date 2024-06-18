from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World, you're at the projects app")