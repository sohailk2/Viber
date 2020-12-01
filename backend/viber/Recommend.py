import lyricsgenius
import os
import lyricsgenius

geniusToken=os.getenv("genius_token")
genius = lyricsgenius.Genius("")

# print(os.environ)
print("token", geniusToken)

posWords = set(line.strip() for line in open('viber/positive-words.txt'))
negWords = set(line.strip() for line in open('viber/negative-words.txt'))


"""
Pseudocode:

    input: songs -> n closest songs based on spotify features

    1) For each song in this list generate a positivity/negativty score
        This score is simple. Running total of positive and negative words
        When encounter positive word, add one
        When encounter negative word, subtract one
        Normalize by number of total words (including words that were neihter positive or negative) in song

    2) Sort list by positivity score for each song

"""
def recommend(orignalSong, songs, viberDB):

    originalSongSent = getSentiment(orignalSong, viberDB)
    # sentiments = list(map(getSentiment, songs[:3], viberDB))
    sentiments = [getSentiment(x, viberDB) for x in songs[:10]]
    
    # sentiments compared with original song
    sentDist = list(map(lambda x : abs(x - originalSongSent), sentiments))

    # sort the songs
    # sortedSongs = [x for _,x in sorted(zip(sentDist,songs))]
    sortedRaw = sorted(zip(sentDist,songs))

    sortedSongs = [x for _,x in sortedRaw]
    sortedSents = [y for y,_ in sortedRaw]

    return sortedSongs, sortedSents



def getSentiment(song, viberDB):
    # first get the lyrics
    cached = viberDB.scores.find_one({"track_id" : song.track_id})
    if cached:
        print("CACHED SONG: ", song.track_name)
        return cached['score']

    lyrics = getLyrics(song)
    posList = []
    negList = []
    length = 0
    for word in lyrics:
        if word in posWords:
            posList.append(word)
        elif word in negWords:
            negList.append(word)
        length += 1
    
    posWordCount = len(posList)
    negWordCount = len(negList)

    print("posList", posWordCount)
    print("negList", negWordCount)

    # adding .001 to account for 0 words found
    score = (posWordCount - negWordCount) / (length + .001)
    cachedVal = { "track_id": song.track_id, "score": score}
    viberDB.scores.insert_one(cachedVal)
    return score

    

def getLyrics(song):
    # print("SONG", song.artist_name, "-", song.track_name)

    geniusSong = genius.search_song(song.track_name, song.artist_name)
    # geniusSong = genius.search_song("POPS", "THEY")
    lyrics = geniusSong.lyrics if geniusSong else ""
    # print(lyrics)
    return lyrics.split(" ")

    file = open("viber/SampleLyrics")
    line = file.read().replace("\n", " ")
    file.close()

    return line.split(" ")