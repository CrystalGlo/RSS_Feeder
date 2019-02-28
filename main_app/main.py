import sys
from PyQt5 import QtWidgets
from main_app.GUI.rss_gui import Ui_MainWindow
import pymongo


class MainWindow(Ui_MainWindow):
    def __init__(self, dialog):
        # Ui_MainWindow.__init__(self)
        # self.setupUi(dialog)

        self.main_ui = Ui_MainWindow()
        # self.main_ui.setupUi(QtWidgets.QMainWindow)

        # self.window = QtWidgets.QMainWindow()
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self.window)
        # self.window.show()


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
