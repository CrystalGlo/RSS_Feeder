import unittest
from unittest import mock

from pymongo import MongoClient
from main_app.src.rssController import RssController
from unittest.mock import MagicMock
from mock import patch

class TestRssController(unittest.TestCase):
    def setUp(self):
        self.testRssAddress = "https://investors.guess.com/rss/events.xml"
        self.testCategory = "Actualité"
        self.testUpFreq = "15 minutes"
        client = MongoClient()
        rssDB = client.get_database("rssDB")
        self.rssCollection = rssDB.get_collection("rss_collection")
        self.rssController = RssController()
        print("In method", self._testMethodName)

    def test_getAndSaveRssEntries_save_entries_to_rssDB(self):
        # Count documents in rssCollection before
        nbrDocBefore = self.rssCollection.count_documents({})
        # Call getAndSaveRssEntries function
        self.rssController.getAndSaveRssEntries(self.testRssAddress, self.testCategory, self.testUpFreq)
        nbrDocAfter = self.rssCollection.count_documents({})
        # Assert documents count increased
        self.assertTrue(nbrDocAfter > nbrDocBefore)

    def test_getAndSaveRssEntries_save_correct_rss(self):
        self.assertTrue(self.rssCollection.find({"rss_address": self.testRssAddress}))

    #def test_updateRssEntries_updates_subscribed_rss(self):
        # self.rssController.unsubscribeRss(self.testRssAddress)
        # self.rssController.getAndSaveRssEntries = MagicMock()
        # #self.rssController.getAndSaveRssEntries(self.testRssAddress, self.testCategory, self.testUpFreq)
        #
        # self.rssController.updateRssEntries()
        #
        # self.rssController.getAndSaveRssEntries.assert_called_once_with(self.testRssAddress, self.testCategory, self.testUpFreq)


    # delete rss test
    def tearDown(self):
        self.rssCollection.find_one_and_delete({"rss_address": self.testRssAddress})

if __name__ == '__main__':
    unittest.main()
