from django.http import HttpResponse

#this is the first page of the BCM app
def bcmHome(request):
    return HttpResponse("WebAPP BCM")