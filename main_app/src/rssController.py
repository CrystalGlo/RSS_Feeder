import pymongo
import feedparser

class RssController(object):
    # Connect to rssDB
    client = pymongo.MongoClient()
    rssDB = client.get_database("rssDB")
    rssCollection = rssDB.get_collection("rss_collection")

    def getAndSaveRssEntries(self, rssAddress, rssCategory, updateFreq):
        # Read entries from RSS feeds
        feeds = feedparser.parse(rssAddress)
        # Save entries data to rssDB
        for i in range(1, len(feeds.entries)):
            self.rssCollection.insert_many(
                [{"rss_address": rssAddress, "rss_category": rssCategory, "update_freq": updateFreq,
                  "news_title": feeds.entries[i]['title'], "news_link": feeds.entries[i]['link'],
                  "news_summary": feeds.entries[i]['summary'], "news_date": feeds.entries[i]['published']}])
        # Delete the first empty row used to create rssCollection
        self.rssCollection.delete_many({"rss_address": ""})

    def getAllExistingData(self):
        documents = []
        self.rssCollection.delete_many({"rss_address": ""})
        cursor = self.rssCollection.find({}, {"_id":0, "news_title":1, "rss_address":1, "news_date":1})
        for document in cursor:
            documents.append(document)

        return documents

    def getDocumentsCount(self):
        self.rssCollection.delete_many({"rss_address": ""})
        docsCount = self.rssCollection.count_documents({})
        return docsCount


getAndSaveRssEntries = RssController.getAndSaveRssEntries
getAllExistingData = RssController.getAllExistingData
getDocumentsCount = RssController.getDocumentsCount
