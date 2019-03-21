import collections

import dateparser as dateparser
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
                  "news_summary": feeds.entries[i]['summary'], "news_date": dateparser.parse(feeds.entries[i]['published'])}])
        # Delete the first empty row used to create rssCollection
        self.rssCollection.delete_many({"rss_address": ""})
        deleteDuplicatedNews(self)

    def updateRssEntries(self):
        rssAddressList = self.rssCollection.distinct("rss_address")
        rssCategory = ""
        updateFreq = ""
        titlesList = []
        for rssAddress in rssAddressList:
            cursor = self.rssCollection.find({"rss_address": rssAddress}, {"_id":0, "rss_category":1, "update_freq":1,
                                                                           "news_title":1})
            for document in cursor:
                rssCategory = document["rss_category"]
                updateFreq = document["update_freq"]
                title = document["news_title"]
                titlesList.append(title)
            duplicatedTitles = [item for item, count in collections.Counter(titlesList).items() if count > 1]
            # get and save updated entries
            getAndSaveRssEntries(self, rssAddress, rssCategory, updateFreq)
            for i in range(0, len(duplicatedTitles)):
                self.rssCollection.delete_one({"news_title": duplicatedTitles[i]})

    def searchNews(self, companyName, keyWord):
        cursorList = []
        # self.rssCollection.create_index({ "$**": "text" })
        if companyName != "" and keyWord == "":
            cursor1 = self.rssCollection.find({"rss_address": {"$regex": companyName, "$options":"i"}}, {"_id":0})
            if cursor1.count() > 0:
                cursorList.append(cursor1)

        elif companyName == "" and keyWord != "":
            cursor2 = self.rssCollection.find({{"rss_category": {"$regex": keyWord, "$options": "i"}}, {"_id": 0}})
            if cursor2.count() > 0:
                cursorList.append(cursor2)
            cursor3 = self.rssCollection.find({{"news_title": {"$regex": keyWord, "$options": "i"}}, {"_id": 0}})
            if cursor3.count() > 0:
                cursorList.append(cursor3)
            cursor4 = self.rssCollection.find({{"news_link": {"$regex": keyWord, "$options": "i"}}, {"_id": 0}})
            if cursor4.count() > 0:
                cursorList.append(cursor4)
            cursor5 = self.rssCollection.find({{"news_summary": {"$regex": keyWord, "$options": "i"}}, {"_id": 0}})
            if cursor5.count() > 0:
                cursorList.append(cursor5)
            cursor6 = self.rssCollection.find({{"news_date": {"$regex": keyWord, "$options": "i"}}, {"_id": 0}})
            if cursor6.count() > 0:
                cursorList.append(cursor6)

        elif companyName != "" and keyWord != "":
            cursor7 = self.rssCollection.find({{"rss_address": {"$regex": companyName, "$options":"i"},
                                                "rss_category": {"$regex": keyWord, "$options": "i"}}, {"_id": 0}})
            if cursor7.count() > 0:
                cursorList.append(cursor7)
            cursor8 = self.rssCollection.find({{"rss_address": {"$regex": companyName, "$options":"i"},
                                                "news_title": {"$regex": keyWord, "$options": "i"}}, {"_id": 0}})
            if cursor8.count() > 0:
                cursorList.append(cursor8)
            cursor9 = self.rssCollection.find({{"rss_address": {"$regex": companyName, "$options":"i"},
                                                "news_link": {"$regex": keyWord, "$options": "i"}}, {"_id": 0}})
            if cursor9.count() > 0:
                cursorList.append(cursor9)
            cursor10 = self.rssCollection.find({{"rss_address": {"$regex": companyName, "$options":"i"},
                                                "news_summary": {"$regex": keyWord, "$options": "i"}}, {"_id": 0}})
            if cursor10.count() > 0:
                cursorList.append(cursor10)
            cursor11 = self.rssCollection.find({{"rss_address": {"$regex": companyName, "$options":"i"},
                                                "news_date": {"$regex": keyWord, "$options": "i"}}, {"_id": 0}})
            if cursor11.count() > 0:
                cursorList.append(cursor11)
        print(len(cursorList))
        return cursorList

    def deleteDuplicatedNews(self):
        rssAddressList = self.rssCollection.distinct("rss_address")
        titlesList = []
        for rssAddress in rssAddressList:
            cursor = self.rssCollection.find({"rss_address": rssAddress}, {"news_title": 1})
            for document in cursor:
                title = document["news_title"]
                titlesList.append(title)

            duplicatedTitles = [item for item, count in collections.Counter(titlesList).items() if count > 1]
            for i in range(0, len(duplicatedTitles)):
                self.rssCollection.delete_one({"news_title": duplicatedTitles[i]})

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
updateRssEntries = RssController.updateRssEntries
deleteDuplicatedNews = RssController.deleteDuplicatedNews
