from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from viber.models import PrevSearches, Following, Person, SpotifyTable
import json
from django.db import connections

import random

from viber import Recommend as Rec

from dotenv import load_dotenv
load_dotenv()

def index(request):
    return HttpResponse("Hello, world. You're at the viber index.")

@csrf_exempt #remove the security checks for post request
def search(request):
    if request.method == 'POST':
        print("request ->", request.body)
        body = json.loads(request.body)
        songName = body["songName"]
    
        song_list = SpotifyTable.objects.raw('SELECT rowid, track_name FROM spotify_table WHERE track_name LIKE \'%{name}%\''.format(name = songName))

        if(len(list(song_list)) == 0):
            returnVal = {"data": []}
        else:
            outputArr = []
            for song in song_list:
                outputArr.append({"track_id" : song.track_id, "title": song.track_name, "artist_name": song.artist_name})
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
        #insert into previous searches table
        cursor.execute('INSERT INTO prev_search (track_id, spotifyUID) VALUES ("' + track_id + '", "' + spotifyUID + '")')

        rawQueryForSongName = 'SELECT rowid, track_id FROM spotify_table WHERE track_id = "' + track_id + '"'
        song = (SpotifyTable.objects.raw(rawQueryForSongName))[0]

        query = ("""SELECT rowid, track_name FROM spotify_table WHERE 
            danceability BETWEEN {danceability1} AND {danceability2} AND
            energy BETWEEN {energy1} AND {energy2} AND
            loudness BETWEEN {loudness1} AND {loudness2} AND
            speechiness BETWEEN {speechiness1} AND {speechiness2} AND
            acousticness BETWEEN {acousticness1} AND {acousticness2} AND
            instrumentalness BETWEEN {instrumentalness1} AND {instrumentalness2} AND
            valence BETWEEN {valence1} AND {valence2} AND
            tempo BETWEEN {tempo1} AND {tempo2}
            LIMIT 20
            """).format(
            danceability1=song.danceability-0.25, danceability2=song.danceability+0.25, 
            energy1=song.energy-0.25, energy2=song.energy+0.25,
            loudness1=song.loudness-0.25,loudness2=song.loudness+0.25,
            speechiness1=song.speechiness-0.25, speechiness2=song.speechiness+0.25,
            acousticness1=song.acousticness-0.25, acousticness2=song.acousticness+0.25,
            instrumentalness1=song.instrumentalness-0.25, instrumentalness2=song.instrumentalness+0.25,
            valence1=song.valence-0.25, valence2=song.valence+0.25,
            tempo1=song.tempo-25, tempo2=song.tempo+25)
        similiarSongs = SpotifyTable.objects.raw(query)

        sortedSentSongs, sortedSentsInfo = Rec.recommend(song, similiarSongs)

        temp = Following.objects.raw(('SELECT following.id, followingUID FROM following JOIN person ON following.followingUID = person.spotifyUID WHERE following.currentUser = \'{uid}\'').format(uid = spotifyUID))
        numFollowing = len(temp) * 0.1
        
        for idx in range(len(sortedSentSongs)):
            temp2 = Following.objects.raw(('SELECT following.id, followingUID FROM following JOIN person ON following.followingUID = person.spotifyUID WHERE following.currentUser = \'{uid}\' AND person.favoriteSong = \"{favSong}\"').format(uid = spotifyUID, favSong = sortedSentSongs[idx].track_name))
            sortedSentsInfo[idx] += (len(temp2)/numFollowing+0.001)*0.01

        sortedSentSongs = [x for _,x in sorted(zip(sortedSentsInfo,sortedSentSongs), reverse=True)]
        sortedSentsInfo = [y for y,_ in sorted(zip(sortedSentsInfo,sortedSentSongs), reverse=True)]

        if(len(list(sortedSentSongs)) == 0):
            returnVal = {"data": []}
        else:
            outputArr = []
            for song in sortedSentSongs:
                outputArr.append({"track_id" : song.track_id, "title": song.track_name, "artist_name": song.artist_name})
            returnVal = {"data": outputArr}

        return JsonResponse(returnVal)

    else:
        return "INVALID"

def getSong(request, id):
    track_id = id
    #finding associated song title and artist name
    rawQueryForSongName = 'SELECT rowid, track_id, track_name FROM spotify_table WHERE track_id = "' + track_id + '"'
    songName = (SpotifyTable.objects.raw(rawQueryForSongName))[0].track_name
    rawQueryForArtistName = 'SELECT rowid, track_id, artist_name FROM spotify_table WHERE track_id = "' + track_id + '"'
    artistName = (SpotifyTable.objects.raw(rawQueryForArtistName))[0].artist_name

    sampleResponse = {"track_id":track_id, "title": songName, "artist_name": artistName}
    return JsonResponse(sampleResponse)

def getSearches(request, id):

    UID = id

    #querying database to return previous searches
    song_list = PrevSearches.objects.raw('SELECT id, track_id FROM prev_search WHERE spotifyUID = "' + UID + '"')

    if(len(list(song_list)) == 0):
        returnVal = {"data": []}
    else:
        outputArr = []
        for song in song_list:
            #finding associated song title and artist name
            songInfo = (SpotifyTable.objects.raw('SELECT rowid, track_id, track_name FROM spotify_table WHERE track_id = "' + song.track_id + '"'))[0]
            
            outputArr.append({"track_id" : song.track_id, "title": songInfo.track_name, "artist_name": songInfo.artist_name})
        outputArr.reverse()
        returnVal = {"data": outputArr}

    return JsonResponse(returnVal)


def getFriends(request, id):
    #query database to find current user's friends
    friendsList = Following.objects.raw('SELECT id, followingUID FROM following WHERE currentUser = "' + id + '"')
    outputArr = []
    for friend in friendsList:
        outputArr.append({"id" : friend.id, "display_name": friend.followingUID})
    returnVal = {"data": outputArr}
    return JsonResponse(returnVal)

@csrf_exempt #remove the security checks for post request
def delFriend(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        userID = body["currUser"]
        friendID = body["friend"]

        cursor = connections['default'].cursor()
        #delete person user is following from database
        cursor.execute('DELETE FROM following WHERE currentUser = "' + userID + '" AND followingUID = "' + friendID + '"')

    return JsonResponse({})

@csrf_exempt #remove the security checks for post request

def addFriend(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        userID = body["currUser"]
        friendID = body["friend"]
        cursor = connections['default'].cursor()
        #insert person user would like to follow
        cursor.execute('INSERT INTO following (currentUser, followingUID) VALUES ("' + userID + '", "' + friendID + '")')
    return JsonResponse({})

def getFavSong(request, id):
    #query database to get user's favorite song
    favSong = Person.objects.raw('SELECT id, favoriteSong FROM person WHERE spotifyUID = "' + id + '"')[0]
    return JsonResponse({"song" : favSong.favoriteSong})

@csrf_exempt #remove the security checks for post request
def setFavSong(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        userID = body["UID"]
        favSong = body["song"]

        cursor = connections['default'].cursor()
        #update database to change user's favorite song
        cursor.execute('UPDATE person SET favoriteSong = "' + favSong + '" WHERE spotifyUID = "' + userID + '"')
    
    return JsonResponse({"success" : "true"})

# just make a new user if not a new user
@csrf_exempt
def loginUser(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        userID = body["UID"]

        cursor = connections['default'].cursor()
        #insert person into database on first time login
        cursor.execute('INSERT INTO person (spotifyUID, favoriteSong) VALUES ("' + userID + '", "Click to add favorite song")')

    return JsonResponse({"success" : "true"})