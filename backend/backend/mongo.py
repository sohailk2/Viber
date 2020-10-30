from pymongo import MongoClient
from bson.objectid import ObjectId

from util.playlist import Playlist


class MongoHandler:
    """
    Handler class to interface with the respective MongoDB.

    ...

    Attributes
    ----------
    db : pymongo.database.Database
        our playlist's database object

    Methods
    -------
    insert_playlist(playlist)
        Insert playlist data in DB, returns its ID

    query_playlist(id)
        Returns playlist object if ID is valid

    """

    MONGO_URL = "mongodb://127.0.0.1:27017/"

    def __init__(self):
        """
        Connects to the Mongo database
        """

        client = MongoClient(MongoHandler.MONGO_URL)
        self.db = client.viber

    def insert_playlist(self, playlist):
        """
        Inserts input playlist data into database

        Parameters
        ----------
        playlist : Playlist
            Playlist object

        Returns
        -------
        str
            newly created ObjectId from the database 
        """

        entry = {
            "link" : playlist.link,
            "songs" : playlist.songs
        }
        result = self.db.playlists.insert_one(entry)
        print(result.inserted_id)
        return result.inserted_id

    def query_playlist(self, oid):
        """
        Returns a playlist object corresponding to the input database ID

        Parameters
        ----------
        id : str
            ObjectId of playlist in database

        Returns
        -------
        Playlist
            Corresponding playlist data, None if invalid input 
        """

        result = self.db.playlists.find_one({"_id": ObjectId(oid)})
        playlist = Playlist(result["link"])
        for song in result["songs"]:
            playlist.add_song(song["name"], song["link"])
        return playlist



if __name__ == "__main__":
    # mongo = MongoHandler()

    # playlist = Playlist("sample playlist url")
    # playlist.add_song("song 1", "song url 1")
    # playlist.add_song("song 2", "song url 2")
    # oid = mongo.insert_playlist(playlist)

    # playlist = mongo.query_playlist("5f9b9a39e56d92d434a884cc")
    # oid = mongo.insert_playlist(playlist)
