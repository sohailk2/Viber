from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from viber.models import Songs, ArtistTerm, PrevSearches
import json
from django.db import connections


import random

# sampleSongs = {'data': [
#         {
#             "track_id" : "1", "title": "Stronger", "song_id": "1", 
#             "release": "2018", "artist_id": "1", "artist_mbid" : "1", 
#             "artist_name" : "Kanye West", "duration" : "3m", 
#             "artist_familiarity" : "IDK", "artist_hotttnesss": "5", "year" : "2018",
#             "track_7digitalid": "1", "shs_perf" : "1", "shs_work" : "1"
#         },
#         {
#             "track_id" : "2", "title": "One Dance", "song_id": "1", 
#             "release": "2016", "artist_id": "1", "artist_mbid" : "1", 
#             "artist_name" : "Drake", "duration" : "3m", 
#             "artist_familiarity" : "IDK", "artist_hotttnesss": "5", "year" : "2018",
#             "track_7digitalid": "1", "shs_perf" : "1", "shs_work" : "1"
#         },
#         {
#             "track_id" : "3", "title": "Kill Em With Kindess", "song_id": "1", 
#             "release": "2012", "artist_id": "1", "artist_mbid" : "1", 
#             "artist_name" : "Selena Gomez", "duration" : "3m", 
#             "artist_familiarity" : "IDK", "artist_hotttnesss": "5", "year" : "2018",
#             "track_7digitalid": "1", "shs_perf" : "1", "shs_work" : "1"
#         },
#         {
#             "track_id" : "4", "title": "The Hills", "song_id": "1", 
#             "release": "2017", "artist_id": "1", "artist_mbid" : "1", 
#             "artist_name" : "The Weeknd", "duration" : "3m", 
#             "artist_familiarity" : "IDK", "artist_hotttnesss": "5", "year" : "2018",
#             "track_7digitalid": "1", "shs_perf" : "1", "shs_work" : "1"
#         },
#         {
#             "track_id" : "5", "title": "Lemonade", "song_id": "1", 
#             "release": "2020", "artist_id": "1", "artist_mbid" : "1", 
#             "artist_name" : "Gunna", "duration" : "3m", 
#             "artist_familiarity" : "IDK", "artist_hotttnesss": "5", "year" : "2018",
#             "track_7digitalid": "1", "shs_perf" : "1", "shs_work" : "1"
#         }

#     ]}

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
    
        #QUERY the database for the song and picks the ones with the most familiar artists
        song_list = Songs.objects.raw('SELECT track_id, title FROM songs WHERE title LIKE \'%{name}%\' ORDER BY artist_familiarity DESC LIMIT 20'.format(name = songName))

        if(len(list(song_list)) == 0):
            returnVal = {"data": []}
        else:
            outputArr = []
            for song in song_list:
                outputArr.append({"track_id" : song.track_id, "title": song.title, "artist_name": song.artist_name})
            returnVal = {"data": outputArr}

        return JsonResponse(returnVal)
    else:
        return JsonResponse({})

@csrf_exempt #remove the security checks for post request
def getPlaylist(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        track_id = body["track_id"]
        spotifyUID = body["UID"]
        cursor = connections['default'].cursor()
        cursor.execute('INSERT INTO prev_search (track_id, spotifyUID) VALUES ("' + track_id + '", "' + spotifyUID + '")')


        rawQueryForSongName = 'SELECT track_id, title FROM songs WHERE track_id = "' + track_id + '"'
        songName = (Songs.objects.raw(rawQueryForSongName))[0].title
        rawQueryForArtistName = 'SELECT track_id, artist_name FROM songs WHERE track_id = "' + track_id + '"'
        artistName = (Songs.objects.raw(rawQueryForArtistName))[0].artist_name

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
        # query4Val = 'SELECT track_id, title, artist_name FROM songs WHERE artist_familiarity >= 1.0'
        query4Val = 'SELECT track_id, title, artist_name FROM songs WHERE artist_id = "' + str(common) + '"'
        # UNION SELECT track_id, title, artist_name FROM songs WHERE artist_id = "' + str(common) + '"'
        query4 = Songs.objects.raw(query4Val)
    
        sampleResponse = {"data": [
            {"track_id":1, "title": query4[0].title, "artist_name": query4[0].artist_name},
            {"track_id":2, "title": query4[1].title, "artist_name": query4[1].artist_name}
        ]}
        return JsonResponse(sampleResponse)
    else:
        return "INVALID"

def getSong(request, id):
    track_id = id
    rawQueryForSongName = 'SELECT track_id, title FROM songs WHERE track_id = "' + track_id + '"'
    songName = (Songs.objects.raw(rawQueryForSongName))[0].title
    rawQueryForArtistName = 'SELECT track_id, artist_name FROM songs WHERE track_id = "' + track_id + '"'
    artistName = (Songs.objects.raw(rawQueryForArtistName))[0].artist_name

    sampleResponse = {"track_id":track_id, "title": songName, "artist_name": artistName}

    return JsonResponse(sampleResponse)

def getSearches(request, id):

    UID = id

    song_list = PrevSearches.objects.raw('SELECT id, track_id FROM prev_search WHERE spotifyUID = "' + UID + '"')

    if(len(list(song_list)) == 0):
        returnVal = {"data": []}
    else:
        outputArr = []
        for song in song_list:
            songInfo = (Songs.objects.raw('SELECT track_id, title FROM songs WHERE track_id = "' + song.track_id + '"'))[0]
            outputArr.append({"track_id" : song.track_id, "title": songInfo.title, "artist_name": songInfo.artist_name})
        returnVal = {"data": outputArr}

    return JsonResponse(returnVal)


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