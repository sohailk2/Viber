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
        #QUERY the database for the song and picks the ones with the most familiar artists
        song_list = Songs.objects.raw('SELECT track_id, title FROM songs WHERE title = %s ORDER BY artist_familiarity DESC', [songName])

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

    #will be replaced with clicked item
    songName = "Silent Night"
    artistName = "Mariah Carey"

    #find artist_id for given track
    queryVal = 'SELECT track_id, artist_id FROM songs WHERE title = "' + songName + '" AND artist_name = "' + artistName + '"'
    query = Songs.objects.raw(queryVal)
    artistID = query[0].artist_id

    #find genre (term) given artist_id
    query2 = ArtistTerm.objects.raw('SELECT artist_id, term FROM artist_term WHERE artist_id = %s', [artistID])
    term = query2[0].term

    #find other artist_ids with same term
    query3Val = 'SELECT artist_id, term FROM artist_term WHERE term = "' + term + '"'
    query3 = ArtistTerm.objects.raw(query3Val)
    common = query3[0].artist_id

    #SET OPERATION: union of familiar artists and ones with similar genre
    query4Val = 'SELECT track_id, title, artist_name FROM songs WHERE artist_familiarity >= 1.0 UNION SELECT track_id, title, artist_name FROM songs WHERE artist_id = "' + str(common) + '"'
    query4 = Songs.objects.raw(query4Val)

    errorResponse = {'error': True}

    sampleResponse = {"data": [
        {"id":1, "name": query4[0].title, "artist": query4[0].artist_name},
        {"id":2, "name": query4[1].title, "artist": query4[1].artist_name}
    ]}
    return JsonResponse(sampleResponse)

def getSong(request, id):
    #clicked song + artist name
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