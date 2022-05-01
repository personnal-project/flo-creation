from django.http import HttpResponse



def index(request):
    return HttpResponse("Bonjour, vous etes sur la page principale de vue")