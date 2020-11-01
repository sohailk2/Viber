from django.db import models

# Create your models here.
# the sql stuff?

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

    def __str__(self):
        return self
