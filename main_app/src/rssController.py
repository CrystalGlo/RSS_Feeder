import collections
import dateparser as dateparser
import pymongo
import feedparser

class RssController(object):
    def __init__(self):
        # Connect to rssDB
        client = pymongo.MongoClient()
        rssDB = client.get_database("rssDB")
        self.rssCollection = rssDB.get_collection("rss_collection")

    def getAndSaveRssEntries(self, rssAddress, rssCategory, updateFreq):
        # Read entries from RSS address
        feeds = feedparser.parse(rssAddress)
        # Save entries data to rssDB
        for i in range(1, len(feeds.entries)):
            self.rssCollection.insert_many(
                [{"rss_address": rssAddress, "rss_category": rssCategory, "update_freq": updateFreq,
                  "news_title": feeds.entries[i]['title'], "news_link": feeds.entries[i]['link'],
                  "news_summary": feeds.entries[i]['summary'], "news_date": dateparser.parse(feeds.entries[i]['published']),
                  "is_subscribed": True}])
        # Delete the first empty row used to create rssCollection
        self.rssCollection.delete_many({"rss_address": ""})
        self.deleteDuplicatedNews(rssAddress)

    def updateRssEntries(self):
        rssAddressList = self.rssCollection.distinct("rss_address")
        rssCategory = ""
        updateFreq = ""
        for rssAddress in rssAddressList:
            cursor = self.rssCollection.find(
                {"rss_address": rssAddress, "is_subscribed": True},
                {"_id": 0, "rss_category": 1, "update_freq": 1}).sort("news_date", -1)
            for document in cursor:
                rssCategory = document["rss_category"]
                updateFreq = document["update_freq"]
            # get and save updated entries
            self.getAndSaveRssEntries(rssAddress, rssCategory, updateFreq)

    def deleteDuplicatedNews(self, rssAddress):
        titlesList = []
        cursor = self.rssCollection.find({"rss_address": rssAddress}, {"news_title": 1}).sort("news_date", -1)
        for document in cursor:
            title = document["news_title"]
            titlesList.append(title)
        # get duplicated titles in a list
        duplicatedTitles = [item for item, count in collections.Counter(titlesList).items() if count > 1]
        # delete the duplicated news
        for i in range(0, len(duplicatedTitles)):
            self.rssCollection.delete_one({"news_title": duplicatedTitles[i]})

    def getSelectedNewsLink(self, selectedTitle):
        newsLink = ""
        cursor = self.rssCollection.find({"news_title": selectedTitle}, {"_id":0, "news_link":1}).sort("news_date", -1)
        for document in cursor:
            newsLink = document["news_link"]
        return newsLink

    def unsubscribeRss(self, rssAddress):
        self.rssCollection.update_many({"rss_address": rssAddress}, { "$set": {"is_subscribed": False}})

    def getAllExistingData(self):
        documents = []
        self.rssCollection.delete_many({"rss_address": ""})
        cursor = self.rssCollection.find({}, {"_id":0, "news_title":1, "rss_address":1, "news_date":1}).sort("news_date", -1)
        for document in cursor:
            documents.append(document)

        return documents

    def getAllRssAddresses(self):
        rssAddressList = self.rssCollection.distinct("rss_address")

        return rssAddressList

    def getDocumentsCount(self):
        self.rssCollection.delete_many({"rss_address": ""})
        docsCount = self.rssCollection.count_documents({})
        return docsCount

    def searchNews(self, searchWord):
        cursorList = []
        cursor1 = self.rssCollection.find({"rss_address": {"$regex": searchWord, "$options":"i"}}, {"_id":0}).sort("news_date", -1)
        if cursor1.count() > 0:
            cursorList.append(cursor1)
        cursor2 = self.rssCollection.find({"news_title": {"$regex": searchWord, "$options": "i"}}, {"_id":0}).sort("news_date", -1)
        if cursor2.count() > 0:
            cursorList.append(cursor2)
        cursor3 = self.rssCollection.find({"news_link": {"$regex": searchWord, "$options": "i"}}, {"_id":0}).sort("news_date", -1)
        if cursor3.count() > 0:
            cursorList.append(cursor3)
        cursor4 = self.rssCollection.find({"news_summary": {"$regex": searchWord, "$options": "i"}}, {"_id":0}).sort("news_date", -1)
        if cursor4.count() > 0:
            cursorList.append(cursor4)
        # Delete duplicated news
        searchCursorList = self.deleteDuplicatedSearchedNews(cursorList)

        return searchCursorList

    def searchNewsByTitle(self, title):
        cursor = self.rssCollection.find({"news_title": title}).sort("news_date", -1)
        return cursor

    def deleteDuplicatedSearchedNews(self, cursorList):
        unduplicatedCursorList = []
        newsTitlesList = []
        for cursor in cursorList:
            for document in cursor:
                newsTitle = document["news_title"]
                if newsTitle not in newsTitlesList:
                    newsTitlesList.append(newsTitle)
        for i in range(0, len(newsTitlesList)):
            searchCursor = self.rssCollection.find({"news_title": str(newsTitlesList[i])}).sort("news_date", -1)
            unduplicatedCursorList.append(searchCursor)

        return unduplicatedCursorList

    def getNewsTitles(self, cursorList):
        newsTitlesList = []
        for cursor in cursorList:
            for document in cursor:
                title = document["news_title"]
                newsTitlesList.append(title)
        return newsTitlesList