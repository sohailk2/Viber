from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


import random

sampleSongs = {'data': [
        {
            "track_id" : "1", "title": "Stronger", "song_id": "1", 
            "release": "2018", "artist_id": "1", "artist_mbid" : "1", 
            "artist_name" : "Kanye West", "duration" : "3m", 
            "artist_familiarity" : "IDK", "artist_hotttnesss": "5", "year" : "2018",
            "track_7digitalid": "1", "shs_perf" : "1", "shs_work" : "1"
        },
        {
            "track_id" : "2", "title": "One Dance", "song_id": "1", 
            "release": "2016", "artist_id": "1", "artist_mbid" : "1", 
            "artist_name" : "Drake", "duration" : "3m", 
            "artist_familiarity" : "IDK", "artist_hotttnesss": "5", "year" : "2018",
            "track_7digitalid": "1", "shs_perf" : "1", "shs_work" : "1"
        },
        {
            "track_id" : "3", "title": "Kill Em With Kindess", "song_id": "1", 
            "release": "2012", "artist_id": "1", "artist_mbid" : "1", 
            "artist_name" : "Selena Gomez", "duration" : "3m", 
            "artist_familiarity" : "IDK", "artist_hotttnesss": "5", "year" : "2018",
            "track_7digitalid": "1", "shs_perf" : "1", "shs_work" : "1"
        },
        {
            "track_id" : "4", "title": "The Hills", "song_id": "1", 
            "release": "2017", "artist_id": "1", "artist_mbid" : "1", 
            "artist_name" : "The Weeknd", "duration" : "3m", 
            "artist_familiarity" : "IDK", "artist_hotttnesss": "5", "year" : "2018",
            "track_7digitalid": "1", "shs_perf" : "1", "shs_work" : "1"
        },
        {
            "track_id" : "5", "title": "Lemonade", "song_id": "1", 
            "release": "2020", "artist_id": "1", "artist_mbid" : "1", 
            "artist_name" : "Gunna", "duration" : "3m", 
            "artist_familiarity" : "IDK", "artist_hotttnesss": "5", "year" : "2018",
            "track_7digitalid": "1", "shs_perf" : "1", "shs_work" : "1"
        }

    ]}

sampleFriends = {'data': [
        {"id" : "1", "display_name": "sohail"},
        {"id" : "2", "display_name": "mesa"},
        {"id" : "3", "display_name": "mihika"},
        {"id" : "4", "display_name": "charlie"},
        {"id" : "5", "display_name": "abdu"}
    ]}

def index(request):
    return HttpResponse("Hello, world. You're at the viber index.")

@csrf_exempt #remove the security checks for post request
def search(request):
    if request.method == 'POST':
        print("request ->", request.body)
        body = json.loads(request.body)
        songName = body["songName"]
        # call search function to da

        returnVal = sampleSongs

        return JsonResponse(returnVal)
    else:
        return JsonResponse({})

def getPlaylist(request, id):

    errorResponse = {'error': True}

    sampleResponse = sampleSongs
    return JsonResponse(sampleResponse)

def getSong(request, id):
    # song = {
    #         "track_id" : "1", "title": "Stronger", "song_id": "1", 
    #         "release": "2018", "artist_id": "1", "artist_mbid" : "1", 
    #         "artist_name" : "Kanye West", "duration" : "3m", 
    #         "artist_familiarity" : "IDK", "artist_hotttnesss": "5", "year" : "2018",
    #         "track_7digitalid": "1", "shs_perf" : "1", "shs_work" : "1"
    #     }
    song = sampleSongs["data"][id - 1]
    return JsonResponse(song)

def getSearches(request, id):
    searches = sampleSongs
    return JsonResponse(searches)


def getFriends(request, id):
    searches = sampleFriends
    return JsonResponse(searches)

@csrf_exempt #remove the security checks for post request
def delFriend(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        userID = body["currUser"]
        friendID = body["friend"]

    return JsonResponse({})


@csrf_exempt #remove the security checks for post request
def addFriend(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        userID = body["currUser"]
        friendID = body["friend"]

    return JsonResponse({})