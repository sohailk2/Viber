from django.db import models

# Create your models here.
# the sql stuff?

class Person(models.Model):
    display_name = models.TextField(primary_key=True, blank=True, null=False)
    #spotify?
    external_urls_spotify = models.TextField(blank=True, null=True)
    followers_count = models.IntegerField(blank=True, null=True)
    followers_href = models.TextField(blank=True, null=True)
    href = models.TextField(blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)
    images = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    uri = models.TextField(blank=True, null=True)

class PERSONS_TABLE:
    managed = False
    db_table = 'persons'
def __str__(self):
    return self.title
# {
#   "display_name": "charlie4",
#   "external_urls": {
#     "spotify": "https://open.spotify.com/user/charlie4"
#   },
#   "followers": {
#     "href": null,
#     "total": 20
#   },
#   "href": "https://api.spotify.com/v1/users/charlie4",
#   "id": "charlie4",
#   "images": [],
#   "type": "user",
#   "uri": "spotify:user:charlie4"
# }
