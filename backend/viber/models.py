from django.db import models

class Songs(models.Model):
    track_id = models.TextField(primary_key=True, blank=True, null=False)
    title = models.TextField(blank=True, null=True)
    song_id = models.TextField(blank=True, null=True)
    release = models.TextField(blank=True, null=True)
    artist_id = models.TextField(blank=True, null=True)
    artist_mbid = models.TextField(blank=True, null=True)
    artist_name = models.TextField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    artist_familiarity = models.FloatField(blank=True, null=True)
    artist_hotttnesss = models.FloatField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    track_7digitalid = models.IntegerField(blank=True, null=True)
    shs_perf = models.IntegerField(blank=True, null=True)
    shs_work = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'songs'
        app_label = 'tracks'

    def __str__(self):
        return self

class ArtistMbtag(models.Model):
    artist = models.ForeignKey('Artists', models.DO_NOTHING, blank=True, null=True)
    mbtag = models.ForeignKey('Mbtags', models.DO_NOTHING, db_column='mbtag', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artist_mbtag'
        app_label = 'genre'

class ArtistTerm(models.Model):
    artist_id = models.TextField(primary_key=True, blank=True, null=True)
    term = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artist_term'
        app_label = 'genre'

class Artists(models.Model):
    artist_id = models.TextField(primary_key=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artists'
        app_label = 'genre'

class Mbtags(models.Model):
    mbtag = models.TextField(primary_key=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mbtags'
        app_label = 'genre'

class Terms(models.Model):
    term = models.TextField(primary_key=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'terms'
        app_label = 'genre'

class PrevSearches(models.Model):
    track_id = models.TextField(blank=True, null=True)
    spotifyUID = models.TextField(blank=True, null=True)

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
    genre = models.TextField(blank=True, null=True)
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