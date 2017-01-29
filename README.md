# BuzzFeedWrapperAPI
# How to Run Code
- [ ] Download repo 
- [ ] Open Terminal/Command Prompt/GitBash and CD into repo
- [ ] Run line 'python -i BuzzFeedWrapperAPI.py' to enter into interactive mode.
- [ ] Create BuzzFeedQuery() object and start querying

## Commands 
1. BuzzFeedQuery.queryTime(feed, start, end): given feed, start timestamp, & end timestamp, output buzzes of the given feed published between those times

2. BuzzFeedQuery.queryKeyword(feed, keywords): given feed & keywords, output buzzes of the given feed containing any of the keywords in the buzz 'title' or 'description'
 
3. BuzzFeedQuery.queryThreshold(feed, start, end, threshold): given feed, start timestamp, end timestamp, & threshold, output buzzes of the given feed whose number of comments meets a certain threshold number

## Inputs
:star: feed: string
<br/>:star: timestamp: same format that the JSON data follows: 
<br/>'Year(4-digit)-Month(2-digit)-Day(2-digit) Hour(2-digit)-Minute(2-digit)-Second(2-digit)'. 
<br/>(e.g. New Years 2017 == '2017-01-01 00:00:00')
<br/>:star: keywords: list of string
<br/>:star: threshold: integer

### Example of how to use program:
$ python -i BuzzFeedWrapperAPI.py
<br/>>>> buzzFeedAPI = BuzzFeedQuery()
<br/>>>> buzzFeedAPI.queryTime('lol', '2016-12-25 00:00:00', '2017-01-01 00:00:00')
<br/>... output ...
<br/>>>> buzzFeedAPI.queryKeyword('cats', [gato, cat, dog, garfield, ate, clifford, the, big, red, dog])
<br/>... output ...
<br/>>>> buzzFeedAPI.queryThreshold('viral', '2016-12-25 00:00:00', '2017-1-1 00:00:00', 100)
<br/>... output ...
- - - -

# Design Decisions
__1.__ Created an internal cache, '__queryCache__', used to save the user's queries. Keys: all previous user queries; Values: buzzes related to the query. This makes it faster to load buzzes for a feed if the user has already made a query using that feed word. Instead of:
<br /> >>>>>>>'open url' -> 'retrieve/load JSON data -> 'get the buzzes from data' 
<br /> for every query, I want to save time by saying :speaking_head: "Hey if a user already searched for the same feed (e.g. 'lol') before, let's save {'lol':lol buzzes} into our cache, so if he/she searches for it again we can pull it from our cache. 
<br />:warning: *A drawback of this cache is that it needs to be updated in case an article is added/deleted, but updates should be taken care of in the 'added' and 'deleted' methods.*
<br/>__2.__ Three functions for the separate tasks (__queryTime, queryKeyword, queryThreshold__). Python doesn't support method overloading, so I just made three different methods to handle each query. I tried to use multiple dispatch library in order to method overload, but because I only needed to implement 3 tasks I separated them.
<br/>__3.__ Various helper methods to abstract away common processes when querying (__checkCache, setCache, getJSONData__)
<br/>__4.__ Decided to simply print the list of queried articles instead of return simply because in terminal I printed the data out in the JSON data format, which returning doesn't do. And, for this assignment, I'm not really doing anything with the query result.
<br/>:fire: One thing I would definitely change about my implementation though is task 2. I currently have it so that I look through every title + description and check if the words are in the hashmap of keywords, which takes a long time. I would redesign the API so that when the article is published, I would save the words in the title and desription into a hashmap of all words in every title and description published so far. The values would then be a list of articles that contain the key word. Because I'm given a list of articles already made, I chose to simply go through the title and description of all the articles.

# Algorithms
- For tasks 1 and 3, the algorithm is very synonymous. You iterate through the list of buzzes and add it to the filtered list if it passes some condition or some constraint. So for both of these tasks, the runtime and space is linear.
- For task 2, I put the inputed key words into a hashmap (dictionary) mainly for lookup speed O(1) compared to O(n) of the given array. I go through each of the articles, and go through the title and description and look up if the current word is in the map and append if it is and continue to the next article, else move on to the next word.
