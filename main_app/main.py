import sys
from PyQt5 import QtWidgets, QtGui
from main_app.GUI.main_gui import Ui_MainWindow
import pymongo

def create_rss_db():
    client = pymongo.MongoClient()
    dbList = client.list_database_names()
    if not "rssDB" in dbList:
        rssDB = client["rssDB"]
        rss_collection = rssDB["rss_collection"]
        rss_collection.insert_one({"rss_address": "", "rss_category": "", "update_freq": "", "news_title": "null title",
                                "news_link": "", "news_summary": "", "news_date": "", "is_subscribed": ""})

class MainWindow(Ui_MainWindow):
    # create the rssDB if it does not exist
    create_rss_db()
    # Show main window
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.label_3.setPixmap(QtGui.QPixmap("GUI/img/rssIcon.png"))
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("GUI/img/refresh_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    ui.btn_update.setIcon(icon)
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap("GUI/img/search_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    ui.btn_search.setIcon(icon2)
    icon3 = QtGui.QIcon()
    icon3.addPixmap(QtGui.QPixmap("GUI/img/occurrence_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    ui.btn_occurrence.setIcon(icon3)
    MainWindow.show()
    sys.exit(app.exec_())
