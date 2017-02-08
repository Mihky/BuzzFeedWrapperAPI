# BuzzFeedWrapperAPI
# How to :running::dash: (Run) Code
- [ ] Download repo (and Python 3.6.0 if you haven't)
- [ ] Open Terminal/Command Prompt/GitBash and CD into repo
- [ ] Run line 'python -i BuzzFeedWrapperAPI.py' to enter into interactive mode.
- [ ] Create BuzzFeedQuery() object and start querying

## Commands 
### Inputs
:star: feed: string
<br/>:star: timestamp: string (e.g. New Years 2017 == '2017-01-01 00:00:00')
<br/>:star: keywords: list of strings
<br/>:star: threshold: integer
<br/>

1. Query by Time:
 - BuzzFeedQuery.query(feed, start, end): given feed, start timestamp, & end timestamp, output buzzes of the given feed published between those times

2. Query by Keywords: 
 - BuzzFeedQuery.query(feed, None, None, keywords): given feed & keywords, output buzzes of the given feed containing any of the keywords in the buzz 'title' or 'description'
 
3. Query by Threshold: 
 - BuzzFeedQuery.query(feed, None, None, None, threshold): given feed & threshold, output buzzes of the given feed whose number of comments meets a certain threshold number

### Example of how to use program:
$ python -i BuzzFeedWrapperAPI.py
<br/>>>> buzzFeedAPI = BuzzFeedQuery()
<br/>>>> buzzFeedAPI.query('lol', '2016-12-25 00:00:00', '2017-01-01 00:00:00')
<br/>... output ...
<br/>>>> buzzFeedAPI.query('cats', None, None, ['gato', 'cat', 'dog', 'garfield', 'ate', 'clifford', 'the', 'big', 'red', 'dog'])
<br/>... output ...
<br/>>>> buzzFeedAPI.query('viral', None, None, None, 100)
<br/>... output ...
- - - -

# Design Decisions
__1.__ Created an internal cache, '__queryCache__', used to save the user's queries. Keys: all previous user queries; Values: buzzes related to the query. This makes it faster to load buzzes for a feed if the user has already made a query using that feed word. Instead of 'open url' -> 'retrieve/load JSON data' -> 'get the buzzes from data' for every query, I want to save time by saying, :speaking_head: "Hey if a user already searched for the same feed (e.g. 'lol') before, let's save {'lol':lol buzzes} into our cache, so if he/she searches for it again we can pull it from our cache. 
<br />:warning: *A drawback of this cache is that it needs to be updated in case an article is added/deleted, but updates should be taken care of in the 'added' and 'deleted' methods.*
<br/><br/>__2.__ Overloaded a general '__query__' method with all parameters other than the feed set initially to __None__. Every query is guaranteed to have a feed input, but the rest of the parameters are entirely up to the user's query type. Within this __query__ method, there are 3 additional methods depending on which type of query the inputs result to.
<br/><br/>__3.__ Various helper methods to abstract away common processes when querying (__checkCache, setCache, getJSONData__)
<br/><br/>__4.__ Decided to simply print the list of queried articles instead of return simply because in terminal I printed the data out in the JSON data format, which returning doesn't do. And, for this assignment, I'm not really doing anything with the query result, so I just decided to pretty print the output instead of returning it.
<br/>:fire: One thing I would definitely change about my implementation though is task 2. I currently have it so that I look through every title + description and check if the words are in the hashmap of keywords. I would redesign the API so that when the article is published, I would save the each of the words in the title and desription into a hashmap of all words in every title and description published so far. The values would then be a list of articles that contain the key word.

# Algorithms
• For tasks 1 and 3, the algorithm is very synonymous. You iterate through the list of buzzes and add it to the filtered list if it passes some condition or some constraint. So for both of these tasks, the runtime and space is linear.
<br/>• For task 2, I put the inputed key words into a hashmap (dictionary) mainly for lookup speed O(1) compared to O(n) of the given array. I go through each of the articles, and go through the title and description and look up if the current word is in the map and append if it is and continue to the next article, else move on to the next word.

# Testing
:microscope: Unit tests in the BuzzFeedWrapperAPITest.py file. Tested for invalid inputs, valid inputs, correct output, correct internal data within data structures, and handle HTTP 500 Errors.
