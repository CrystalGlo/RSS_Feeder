import pymongo
import feedparser

class RssController(object):
    def getAndSaveRssEntries(self, rssAddress, rssCategory, updateFreq):
        # Connect to rssDB
        client = pymongo.MongoClient()
        rssDB = client.get_database("rssDB")
        rssCollection = rssDB.get_collection("rss_collection")
        if rssAddress != "":
            # Read entries from RSS feeds
            feeds = feedparser.parse(rssAddress)
            # Save entries data to rssDB
            for i in range(1, len(feeds.entries)):
                rssCollection.insert_many(
                    [{"rss_address": rssAddress, "rss_category": rssCategory, "update_freq": updateFreq,
                      "news_title": feeds.entries[i]['title'], "news_link": feeds.entries[i]['link'],
                      "news_summary": feeds.entries[i]['summary'], "news_date": feeds.entries[i]['published']}])
        # Delete the first empty row used to create rssCollection
        rssCollection.find_one_and_delete({"rss_address": ""})


getAndSaveRssEntries = RssController.getAndSaveRssEntries
