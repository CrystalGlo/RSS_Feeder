import unittest
from pymongo import MongoClient
from main_app.src.rssController import RssController
from unittest.mock import MagicMock


class TestRssController(unittest.TestCase):
    def setUp(self):
        self.testRssAddress = "https://investors.guess.com/rss/events.xml"
        self.testCategory = "Actualité"
        self.testUpFreq = "15 minutes"
        client = MongoClient()
        rssDB = client.get_database("rssDB")
        self.rssCollection = rssDB.get_collection("rss_collection")
        self.rssController = RssController()
        self.rssController.getAndSaveRssEntries(self.testRssAddress, self.testCategory, self.testUpFreq)
        document = self.rssCollection.find_one({"rss_address": self.testRssAddress}, {"_id": 0, "news_title": 1})
        self.title = document['news_title']
        print("In method", self._testMethodName)

    def test_getAndSaveRssEntries_save_entries_to_rssDB(self):
        self.rssCollection.delete_many({"rss_address": self.testRssAddress})
        # Count documents in rssCollection before
        nbrDocBefore = self.rssCollection.count_documents({})
        # Call getAndSaveRssEntries function
        self.rssController.getAndSaveRssEntries(self.testRssAddress, self.testCategory, self.testUpFreq)
        nbrDocAfter = self.rssCollection.count_documents({})
        # Assert documents count increased
        self.assertTrue(nbrDocAfter > nbrDocBefore)

    def test_getAndSaveRssEntries_save_correct_rss(self):
        self.assertTrue(self.rssCollection.find({"rss_address": self.testRssAddress}))

    def test_updateRssEntries_updates_only_subscribed_rss(self):
        self.rssController.unsubscribeRss(self.testRssAddress)
        self.rssController.getAndSaveRssEntries = MagicMock()

        self.rssController.updateRssEntries()

        assert ((self.testRssAddress, self.testCategory,
                 self.testUpFreq),) not in self.rssController.getAndSaveRssEntries.call_args_list

    def test_getSelectedNewsLink_return_appropriate_link(self):
        originalDoc = self.rssCollection.find_one({"rss_address": self.testRssAddress, "news_title": self.title},
                                                  {"_id": 0, "news_link": 1})
        appropriateLink = originalDoc['news_link']

        returnedLink = self.rssController.getSelectedNewsLink(self.title)

        self.assertEqual(returnedLink, appropriateLink)

    def test_deleteDuplicatedNews_delete_duplicated_titles(self):
        document = self.rssCollection.find_one({"rss_address": self.testRssAddress}, {"_id":0})
        news_link = document["news_link"]
        news_summary = document["news_summary"]
        news_date = document["news_date"]
        is_subscribed = document["is_subscribed"]
        # insert the same line to have duplicated lines
        self.rssCollection.insert_many(
            [{"rss_address": self.testRssAddress, "rss_category": self.testCategory, "update_freq": self.testUpFreq,
              "news_title": self.title, "news_link": news_link, "news_summary": news_summary,
              "news_date": news_date, "is_subscribed": is_subscribed}])
        countBefore = self.rssCollection.count_documents({"rss_address": self.testRssAddress, "news_title": self.title})

        self.rssController.deleteDuplicatedNews(self.testRssAddress)

        countAfter = self.rssCollection.count_documents({"rss_address": self.testRssAddress, "news_title": self.title})

        self.assertTrue(countAfter < countBefore)
        self.assertTrue(countAfter == 1)

    def test_unsubscribeRss_set_isSubscribed_toFalse(self):
        self.rssCollection.update_many({"rss_address": self.testRssAddress}, {"$set": {"is_subscribed": True}})

        self.rssController.unsubscribeRss(self.testRssAddress)
        document = self.rssCollection.find_one({"rss_address": self.testRssAddress}, {"_id":0, "is_subscribed":1})
        isSubscribed = document["is_subscribed"]

        self.assertEqual(isSubscribed, False)

    def test_getAllExistingData_returns_all_data(self):
        cursor = self.rssCollection.find({})
        docsCount = self.rssCollection.count_documents({})

        returnedDocs = self.rssController.getAllExistingData()

        self.assertEqual(len(returnedDocs), docsCount)
        for document in cursor:
            self.assertTrue(document in returnedDocs)

    def test_getAllRssAddresses_returns_all_rssAddresses(self):
        existingAddressList = self.rssCollection.distinct("rss_address")

        returnedAddressList = self.rssController.getAllRssAddresses()

        self.assertEqual(len(returnedAddressList), len(existingAddressList))
        for address in existingAddressList:
            self.assertTrue(address in returnedAddressList)

    def test_getDocumentsCount_return_exact_docsCount(self):
        existingDocsCount = self.rssCollection.count_documents({})

        returnedDocsCount = self.rssController.getDocumentsCount()

        self.assertEqual(returnedDocsCount, existingDocsCount)

    def test_searchNewsByTitle_return_correct_documents(self):
        cursor = self.rssCollection.find({"news_title": self.title}).sort("news_date", -1)

        returnedCursor = self.rssController.searchNewsByTitle(self.title)

        self.assertEqual(returnedCursor.count(), cursor.count())
        for document in returnedCursor:
            self.assertTrue(document in cursor)

    # delete test rss address
    def tearDown(self):
        self.rssCollection.delete_many({"rss_address": self.testRssAddress})


if __name__ == '__main__':
    unittest.main()


