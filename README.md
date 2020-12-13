# Viber
Song recommendation web app based on musical features, lyric analysis, friend user information. 
Demo Link: https://www.youtube.com/watch?v=aJAPGMODLNY

- Ability to search for songs based on track name and artist name.
- Retrieves sorted recommended songs from a search query based on musical features, lyric sentiment, and a custom friend factor.
- Displays spotify features (valence, danceability, etc…) for each song to make suggestion easy to understand
- Allows you to follow other users.
- Keeps track of your previous song searches.
- Option to set your own favorite song.


Our goal is to retrieve a sorted list of similar songs from the user’s search query. To do this we follow a four step process: find a set of approximate matches, sort by closest to song from musical features, rerank songs through sentiment matches to query, then perform one final rerank factoring in a user’s friends favorite songs. This process will be explained in more detail below. 
Find set of approximate matches
1) First, we retrieved the rowid and track_id  from every song in our sql database.
Then, we chose to grab songs that were between +/- .25 of the song’s features. These features included danceability, energy, loudness, speechiness, etc.
Sort by closest to song from musical features
2) Using the approximate matches we had from step 1, we now rank these by musical similarity to the query. 
This method can be thought of as KNN search in n-dimensional space. In our case, each song is a point of n-dimensions where each dimension is a different musical feature: danceability, energy, loudness, etc…. 
To implement this idea, we performed a query in SQL defining a euclidean distance variable calculated for each song. Then we ORDER_BY this variable to get a list of the top 20 sorted, musically similar songs. 
3) Sentiment Analysis
Our goal of sentiment analysis was to perform deeper analysis of the lyrics. However, to optimize for runtime constraints, we decided to analyze the positive/negative component of the lyrics instead of more complex language features. 
First, we downloaded a dataset of about 10,000 positive/negative words from a study done by the UofC. Next we held a counter of positive and negative words encountered in each lyrics.
The score returned for a lyric = (positive - negative) / len(playlist). We divided by len(playlist) to normalize the score. 
4) Factoring in a user’s friends favorite songs
Firstly, we perform a join on the following and person table on following.followingUID = person.spotifyUID to just find the number of people the user is following.
We then do the same join again to retrieve all the users the current user is following, who also have a specific song set as their favorite song. 
We then add in a “following weight” to all tracks using the formula, with friendFactor set to 0.01: 
(num following with x as fav song/ (total num following + 0.001)) * friendFactor
We then sort the songs based on the newly weighted scores and return the list in descending order of weight.
	

Finally, we gathered all the recommended song’s attributes into one list called outputArr and returned this in our JsonResponse.
