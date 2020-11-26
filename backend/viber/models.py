from django.db import models

class PrevSearches(models.Model):
    track_id = models.TextField(blank=True, null=True)
    spotifyUID = models.TextField(blank=True, null=True, db_index=True)

    class Meta:
        db_table = 'prev_search'

class Person(models.Model):
    spotifyUID = models.TextField(blank=True, null=True)
    favoriteSong = models.TextField(blank=True, null=True)
    class Meta:
        db_table = 'person'

class Following(models.Model):
    currentUser = models.TextField(blank=True, null=True)
    followingUID = models.TextField(blank=True, null=True)
    class Meta:
        db_table = 'following'

class SpotifyTable(models.Model):
    rowid = models.TextField(primary_key=True, blank=True, null=False)
    a = models.TextField(blank=True, null=True)
    artist_name = models.TextField(blank=True, null=True)
    track_name = models.TextField(blank=True, null=True)
    track_id = models.TextField(blank=True, null=False)
    popularity = models.IntegerField(blank=True, null=True)
    acousticness = models.FloatField(blank=True, null=True)
    danceability = models.FloatField(blank=True, null=True)
    duration_ms = models.IntegerField(blank=True, null=True)
    energy = models.FloatField(blank=True, null=True)
    instrumentalness = models.FloatField(blank=True, null=True)
    key = models.TextField(blank=True, null=True)
    liveness = models.FloatField(blank=True, null=True)
    loudness = models.FloatField(blank=True, null=True)
    mode = models.TextField(blank=True, null=True)
    speechiness = models.FloatField(blank=True, null=True)
    tempo = models.FloatField(blank=True, null=True)
    time_signature = models.TextField(blank=True, null=True)
    valence = models.FloatField(blank=True, null=True)

    def __lt__(self, other):
        return self.track_name < other.track_name

    class Meta:
        managed = False
        db_table = 'spotify_table'