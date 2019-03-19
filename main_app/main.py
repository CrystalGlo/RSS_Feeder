import sys
from PyQt5 import QtWidgets, QtGui, QtCore

from main_app.GUI.main_gui import Ui_MainWindow
from main_app.GUI.search_gui import Ui_SearchWindow
import pymongo

class MainWindow(Ui_MainWindow):
    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)

def create_rss_db():
    client = pymongo.MongoClient()
    rssDB = client["rssDB"]
    rss_collection = rssDB["rss_collection"]
    rss_collection.insert_one({"rss_address": "", "rss_category": "", "update_freq": "", "news_title": "null title",
                                "news_link": "", "news_summary": "", "news_date": ""})
    # rss_collection.create_index("news_title", unique= True)
    # rss_collection.create_index([('news_title', pymongo.ASCENDING)], unique=True)

if __name__ == "__main__":
    # create the rssDB if it does not exist
    client = pymongo.MongoClient()
    dbList = client.list_database_names()
    if not "rssDB" in dbList:
        create_rss_db()
    # Show main window
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.label_3.setPixmap(QtGui.QPixmap("src/img/rssIcon.png"))
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("src/img/refresh_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    ui.btn_update.setIcon(icon)
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap("src/img/search_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    ui.btn_search.setIcon(icon2)

    SearchWindow = QtWidgets.QMainWindow()
    searchUi = Ui_SearchWindow()
    searchUi.setupUi(SearchWindow)
    searchUi.label_picture.setPixmap(QtGui.QPixmap("src/img/search_icon.png"))

    MainWindow.show()
    sys.exit(app.exec_())
