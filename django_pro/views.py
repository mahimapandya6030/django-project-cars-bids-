from django.shortcuts import redirect
from django.shortcuts import HttpResponse

def main(request):
    return HttpResponse("Hello, world!")