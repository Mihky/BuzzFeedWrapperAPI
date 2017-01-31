import BuzzFeedWrapperAPI
import unittest

class Tester(unittest.TestCase):

	# Setup the test objects
	def setUp(self):
		print('Success: Instantiated BuzzFeedQuery object!')
		self.queryCounts = 0
		self.queriesSet = set()
		self.tester = BuzzFeedWrapperAPI.BuzzFeedQuery()

	# Reset the test objects
	def tearDown(self):
		print('Success: Reset BuzzFeedQuery object!')
		self.queryCounts = 0
		self.queriesSet.clear()
		self.tester.queryCache = {}

	# Tests setup
	def testSetUp(self):
		self.assertEqual(self.tester.FEEDS_URL, 'http://buzzfeed.com/api/v2/feeds/')
		self.assertEqual(self.tester.queryCache, {})
		self.assertEqual(type(self.tester.queryCache), dict)
		self.assertEqual(type(self.tester.tempJSONData), list)

	# Tests the first query option
	def testQueryByTime(self):
		self.tester.tempJSONData = []
		self.tester.queryTime('Buzzzzzzzz', '16-12-25 12:03:00', '2017-01-01 00:00:00')
		self.assertEqual(len(self.tester.tempJSONData), 0)
		self.tester.tempJSONData = []
		self.tester.queryTime('Buzzzzzzzz', '2016-12-25 12:03:00', '17-1-1 00:00:00')
		self.assertEqual(len(self.tester.tempJSONData), 0)
		self.tester.queryTime('lol', '2016-01-01 00:00:00', '2017-01-30 00:00:00')
		self.assertEqual(len(self.tester.tempJSONData), 25)
		self.tester.queryTime('eGg', '2007-01-01 00:00:00', '2010-01-01 00:00:00')
		self.assertEqual(len(self.tester.tempJSONData), 4)
		titles = ['Ummm... zodiac? Still trampy - just not as depress', 'High energy fun', 'this makes me happier : )', 'I think the graph would be more visualy effective if it showed how much each candidates tax plan wou']
		for index in range(len(self.tester.tempJSONData)):
			self.assertEqual(titles[index], self.tester.tempJSONData[index]['title'])
		self.tester.queryTime('EGG', '2007-01-01 00:00:00', '2009-01-01 00:00:00')
		self.assertEqual(len(self.tester.tempJSONData), 3)

	# Tests the second query option
	def testQueryByKeywords(self):
		self.tester.queryKeyword('news', ['Trump', 'BuzzFeed'])
		self.assertEqual(len(self.tester.tempJSONData), 10)
		self.tester.tempJSONData = []
		self.tester.queryKeyword(1, ['Trump'])
		self.assertEqual(len(self.tester.tempJSONData), 0)
		self.tester.tempJSONData = []
		self.tester.queryKeyword('news', ['Trump', 10])
		self.assertEqual(len(self.tester.tempJSONData), 0)
		self.tester.queryKeyword('news', ['TRUmP', 'BuZZfEeD'])
		self.assertEqual(len(self.tester.tempJSONData), 10)

	# Tests the third query option
	def testQueryByThreshold(self):
		self.tester.queryThreshold('omg?p=2', '2016-12-25 12:03:00', '17-1-1 00:00:00', 0)
		self.assertEqual(len(self.tester.tempJSONData), 6)
		self.tester.queryThreshold('omg?p=2', '2016-12-25 12:03:00', '17-1-1 00:00:00', 1)
		self.assertEqual(len(self.tester.tempJSONData), 0)
		self.tester.tempJSONData = []
		self.tester.queryThreshold('OMg?p=2', '2016-12-25 12:03:00', '17-1-1 00:00:00', '2')
		self.assertEqual(len(self.tester.tempJSONData), 0)
		self.tester.tempJSONData = []
		self.tester.queryThreshold(2, '2016-12-25 12:03:00', '17-1-1 00:00:00', 1)
		self.assertEqual(len(self.tester.tempJSONData), 0)

if __name__ == '__main__':
	unittest.main()
