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
<br/>:fire::fire::fire: 
