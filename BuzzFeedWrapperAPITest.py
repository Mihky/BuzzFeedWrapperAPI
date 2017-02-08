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
		self.tester.query('Buzzzzzzzzzzzzzz', '16-12-25 12:03:00', '2017-01-01 00:00:00')
		self.assertEqual(len(self.tester.tempJSONData), 0)
		self.tester.tempJSONData = []
		self.tester.query('Buzzzzz', '2016-12-25 12:03:00', '17-1-1 00:00:00')
		self.assertEqual(len(self.tester.tempJSONData), 0)
		self.tester.query('lol', '2016-01-01 00:00:00', '2017-01-30 00:00:00')
		self.assertEqual(len(self.tester.tempJSONData), 25)
		self.tester.query('eGg', '2007-01-01 00:00:00', '2010-01-01 00:00:00')
		self.assertEqual(len(self.tester.tempJSONData), 4)
		titles = ['Ummm... zodiac? Still trampy - just not as depress', 'High energy fun', 'this makes me happier : )', 'I think the graph would be more visualy effective if it showed how much each candidates tax plan wou']
		for index in range(len(self.tester.tempJSONData)):
			self.assertEqual(titles[index], self.tester.tempJSONData[index]['title'])
		self.tester.query('EGG', '2007-01-01 00:00:00', '2009-01-01 00:00:00')
		self.assertEqual(len(self.tester.tempJSONData), 3)

	# Tests the second query option
	def testQueryByKeywords(self):
		self.tester.query('news', None, None, ['Trump', 'BuzzFeed'])
		self.assertEqual(len(self.tester.tempJSONData), 14)
		self.tester.tempJSONData = []
		self.tester.query(1, None, None, ['Trump'])
		self.assertEqual(len(self.tester.tempJSONData), 0)
		self.tester.tempJSONData = []
		self.tester.query('news', None, None, ['Trump', 10])
		self.assertEqual(len(self.tester.tempJSONData), 0)
		self.tester.query('news', None, None, ['TRUmP', 'BuZZfEeD'])
		self.assertEqual(len(self.tester.tempJSONData), 14)

	# Tests the third query option
	def testQueryByThreshold(self):
		self.tester.query('omg?p=2', None, None, None, 0)
		self.assertEqual(len(self.tester.tempJSONData), 19)
		self.tester.query('omg?p=2', None, None, None, 1)
		self.assertEqual(len(self.tester.tempJSONData), 0)
		self.tester.tempJSONData = []
		self.tester.query('OMg?p=2', None, None, None, '2')
		self.assertEqual(len(self.tester.tempJSONData), 0)
		self.tester.tempJSONData = []
		self.tester.query(2, None, None, None, 1)
		self.assertEqual(len(self.tester.tempJSONData), 0)

if __name__ == '__main__':
	unittest.main()
