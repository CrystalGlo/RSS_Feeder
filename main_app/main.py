import sys
from PyQt5 import QtWidgets
from main_app.GUI.main_gui import Ui_MainWindow
import pymongo


class MainWindow(Ui_MainWindow):
    def __init__(self):
        self.main_ui = Ui_MainWindow()

def create_rss_db():
    client = pymongo.MongoClient()
    rssDB = client["rssDB"]
    rss_collection = rssDB["rss_collection"]
    rss_collection.insert_one({"rss_address": "", "rss_category": "", "update_freq": "", "news_title": "",
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
    MainWindow.show()
    sys.exit(app.exec_())
