
class Playlist:
	def __init__(self, link=""):
		self.link = link
		self.songs = []

	def add_song(self, name, link=""):
		self.songs.append({ "name": name,
			   				"link": link })
