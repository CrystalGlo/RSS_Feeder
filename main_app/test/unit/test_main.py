import unittest
from pymongo import MongoClient
import main

class TestCreateDatabase(unittest.TestCase):
    def test_db_exists(self):
        main.create_rss_db()
        client = MongoClient()
        dbList = client.list_database_names()

        self.assertTrue("rssDB" in dbList)

    def test_rss_collection_exists(self):
        main.create_rss_db()
        client = MongoClient()
        rssDB = client.get_database("rssDB")
        collectionList = rssDB.list_collection_names()

        self.assertTrue("rss_collection" in collectionList)

suite = unittest.TestLoader().loadTestsFromTestCase(TestCreateDatabase)
unittest.TextTestRunner(verbosity=2).run(suite)
