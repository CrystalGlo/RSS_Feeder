import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from main_app.GUI.main_gui import Ui_MainWindow
import pymongo
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from src.rssController import RssController

# class MainWindow(Ui_MainWindow):
#     def __init__(self, dialog):
#         Ui_MainWindow.__init__(self)
#         self.setupUi(dialog)

def create_rss_db():
    client = pymongo.MongoClient()
    rssDB = client["rssDB"]
    rss_collection = rssDB["rss_collection"]
    rss_collection.insert_one({"rss_address": "", "rss_category": "", "update_freq": "", "news_title": "null title",
                                "news_link": "", "news_summary": "", "news_date": ""})

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
    MainWindow.show()
    # show the first news details
    ui.tableWidget.selectRow(0)
    selectedRow = ui.tableWidget.currentRow()
    if selectedRow >= 0:
        title = ui.tableWidget.item(selectedRow, 0).text()
        if title != "":
            rssController = RssController()
            news_link = rssController.getSelectedNewsLink(title)
            web = QWebEngineView()
            web.load(QUrl(news_link))
            web.show()

    sys.exit(app.exec_())
