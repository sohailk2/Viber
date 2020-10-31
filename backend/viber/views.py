from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


import random


def index(request):
    return HttpResponse("Hello, world. You're at the viber index.")

@csrf_exempt #remove the security checks for post request
def search(request):
    if request.method == 'POST':
        print("request ->", request.body)
        body = json.loads(request.body)
        songName = body["songName"]
        # call search function to da

        returnVal = {"data": [
                {"id" : 1, "name": "song" +  str(random.randint(1,20)), "artist": "artist1"}, 
                {"id" : 2, "name": "song2" +  str(random.randint(1,20)), "artist": "artist2"}, 
                {"id" : 3, "name": "song3" +  str(random.randint(1,20)), "artist": "artist3"}, 
                {"id" : 4, "name": "song4" +  str(random.randint(1,20)), "artist": "artist4"}]}

        return JsonResponse(returnVal)
    else:
        return {}

def getPlaylist(request, id):

    errorResponse = {'error': True}

    sampleResponse = {"data": [
        {"id":1, "name": "song1", "artist": "artist"},
        {"id":2, "name": "song2", "artist": "artist"}
    ]}
    return JsonResponse(sampleResponse)

def getSong(request, id):
    song = {"id" : id, "name": "song" + str(id), "artist": "artist1"}
    return JsonResponse(song)