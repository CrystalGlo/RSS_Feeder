import unittest
from pymongo import MongoClient
from main_app.src.rssController import RssController

class TestRssController(unittest.TestCase):
    testRssAddress = "http://rss.allocine.fr/ac/actualites"
    client = MongoClient()
    rssDB = client.get_database("rssDB")
    rssCollection = rssDB.get_collection("rss_collection")
    rssCollection.find_one_and_delete({"rss_address": testRssAddress})

    def test_getAndSaveRssEntries_save_entries_to_rssDB(self):
        # count documents in rssCollection before
        nbrDocBefore = self.rssCollection.count_documents({})

        RssController.getAndSaveRssEntries(RssController ,self.testRssAddress, "Actualité", "15 minutes")
        nbrDocAfter = self.rssCollection.count_documents({})

        self.assertTrue(nbrDocAfter > nbrDocBefore)

    def test_getAndSaveRssEntries_save_correct_rss(self):
        self.assertTrue(self.rssCollection.find({"rss_address": self.testRssAddress}))


suite = unittest.TestLoader().loadTestsFromTestCase(TestRssController)
unittest.TextTestRunner(verbosity=2).run(suite)
