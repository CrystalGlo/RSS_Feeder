import unittest
from pymongo import MongoClient

class TestDatabase(unittest.TestCase):

    def test_db_exists(self):
        client = MongoClient()
        dbList = client.list_database_names()

        self.assertTrue("rssDB" in dbList)

    def test_rss_collection_exists(self):
        client = MongoClient()
        rssDB = client.get_database("rssDB")
        collectionList = rssDB.list_collection_names()

        self.assertTrue("rss_collection" in collectionList)

if __name__ == '__main__':
    unittest.main()

