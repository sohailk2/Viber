from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from viber.models import Songs, ArtistTerm
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
        
        songName = "Silent Night"
        #queries the database for the song and picks the ones with the most familiar artists
        song_list = Songs.objects.raw('SELECT track_id, title FROM songs WHERE title = %s ORDER BY artist_familiarity DESC', [songName])
        # a = ArtistTerm.objects.raw('SELECT artist_id from artist_term WHERE term = "country rock"')
        # print(len(list(a)))

        if(len(list(song_list)) <= 4):
            returnVal = {"data": [
                {"id" : 1, "name": song_list[0].title, "artist": song_list[0].artist_name}]}
        else:
            returnVal = {"data": [
                    {"id" : 1, "name": song_list[0].title, "artist": song_list[0].artist_name}, 
                    {"id" : 2, "name": song_list[1].title, "artist": song_list[1].artist_name}, 
                    {"id" : 3, "name": song_list[2].title, "artist": song_list[2].artist_name}, 
                    {"id" : 4, "name": song_list[3].title, "artist": song_list[3].artist_name}]}

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

def getSearches(request, id):
    searches = {'data': [
        {"id" : "1", "name": "searched song 1", "artist": "artist1"},
        {"id" : "2", "name": "searched song 1", "artist": "artist1"},
        {"id" : "3", "name": "searched song 3", "artist": "artist1"}

    ]}
    return JsonResponse(searches)


def getFriends(request, id):
    searches = {'data': [
        {"id" : "1", "name": "friend 1", "artist": "artist1"},
        {"id" : "2", "name": "friend 2", "artist": "artist1"},
    ]}
    return JsonResponse(searches)