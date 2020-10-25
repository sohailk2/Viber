from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import random


def index(request):
    return HttpResponse("Hello, world. You're at the viber index.")

def search(request):
    returnVal = {"data": [
                {"name": "song" +  str(random.randint(1,20)), "artist": "artist1"}, 
                {"name": "song2" +  str(random.randint(1,20)), "artist": "artist2"}, 
                {"name": "song3" +  str(random.randint(1,20)), "artist": "artist3"}, 
                {"name": "song4" +  str(random.randint(1,20)), "artist": "artist4"}]}

    return JsonResponse(returnVal)