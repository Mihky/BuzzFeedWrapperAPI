import json
import datetime
try:
	from urllib.request import urlopen
except ImportError:
	from urllib2 import urlopen

class BuzzFeedQuery:
	FEEDS_URL = 'http://buzzfeed.com/api/v2/feeds/'

	def __init__(self):
		print ('Start Querying Away!')
		self.queryCache = {}
		# Mainly used for testing
		self.tempJSONData = []

	# Outputs all feed buzzes that were published between the start and end timestamps.
	def queryTime(self, feed, start, end):
		# Checks that all inputs are valid types (should be strings) and that the timestamps are in proper format
		if type(feed) is not str or type(start) is not str or type(end) is not str:
			print('Invalid Query Call')
			return
		try:
			lower = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
			upper = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
		except ValueError:
			print('Error: Improper timestamp format')
			return

		result = []
		if not self.checkCache(feed):
			self.setCache(feed)
		buzzes = self.queryCache[feed]

		for buzz in buzzes:
			current = datetime.datetime.strptime(buzz['published_date'], '%Y-%m-%d %H:%M:%S')
			# checks to see that the current buzz's timestamp is between the start and end time bounds
			if lower <= current and current <= upper:
				result.append(buzz)
		self.tempJSONData = result
		print(json.dumps(result, indent=4, sort_keys=True))

	# Outputs all feed buzzes that have keywords in either their titles/descriptions
	def queryKeyword(self, feed, keywords):
		# Checks that feed is a valid string query 
		if type(feed) is not str:
			print('Invalid Query Call')
			return

		# Checks that input list of keywords are all strings
		for keyword in keywords:
			if type(keyword) is not str:
				print('Invalid Query Call')
				return

		result = []
		keywordMap = {}
		# put all keywords into the hashmap
		for word in keywords:
			keywordMap[word.lower()] = 1
		
		feed = feed.lower()
		if not self.checkCache(feed):
			self.setCache(feed)
		
		buzzes = self.queryCache[feed]
		for buzz in buzzes:
			# Goes through the title and checks if it contains any of the keywords
			for word in buzz['title'].split():
				word = word.lower()
				if word in keywordMap:
					result.append(buzz)
					continue # Skip over the description to the next article if keyword was found in title
			# Goes through description and checks if it contains any of the keywords
			for word in buzz['description'].split():
				word = word.lower()
				if word in keywordMap:
					result.append(buzz)
		self.tempJSONData = result
		print(json.dumps(result, indent=4, sort_keys=True))

	# Outputs the feed buzzes whose number of comments meet some threshold amount
	def queryThreshold(self, feed, start, end, threshold):
		# Checks that feed is a string and that threshold is an int
		if type(feed) is not str or type(threshold) is not int:
			print('Invalid Query Call')
			return
		
		feed = feed.lower()
		if not self.checkCache(feed):
			self.setCache(feed)

		buzzes = self.queryCache[feed]
		result = []
		for buzz in buzzes:
			comments = 0 if buzz['comment_stats'] == 'null' or buzz['comment_stats'] is None else buzz['comment_stats']
			if threshold is not None and comments < threshold:
				continue
			result.append(buzz)
		self.tempJSONData = result
		print(json.dumps(result, indent=4, sort_keys=True))

	# Checks if feed is in the cache, which means that the feed has been queried before
	def checkCache(self, feed):
		if feed in self.queryCache:
			return True
		return False

	# Set the feed's buzzes into the cache
	def setCache(self, feed):
		self.queryCache[feed] = self.getJSONData(feed)

	# Given a feed, returns the buzzes correlated to that feed
	def getJSONData(self, feed):
		queryUrl = '%s%s' % (self.FEEDS_URL, feed)
		response = urlopen(queryUrl)
		jsonData = json.loads(response.read().decode('utf-8'))
		return jsonData['buzzes']
	def test(self, feed):
		print(json.dumps(self.getJSONData(feed), indent=4, sort_keys=True))