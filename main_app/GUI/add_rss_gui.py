# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_rss_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtWidgets
import feedparser
import pymongo

class Ui_AddRssWindow(object):
    def getAndSaveRssFeeds(self):
        # Connect to rssDB
        client = pymongo.MongoClient()
        rssDB = client.get_database("rssDB")
        rssCollection = rssDB.get_collection("rss_collection")
        # Get main RSS information
        rssAddress = self.rss_adress_lineEdit.text()
        rssCategory = self.category_comboBox.currentText()
        updateFreq = self.update_frequency_comboBox.currentText()
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

    def setupUi(self, AddRssWindow):
        AddRssWindow.setObjectName("AddRssWindow")
        AddRssWindow.resize(452, 218)
        self.centralwidget = QtWidgets.QWidget(AddRssWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 451, 151))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 170, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.rss_adress_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.rss_adress_lineEdit.setObjectName("rss_adress_lineEdit")
        self.gridLayout.addWidget(self.rss_adress_lineEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 170, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.category_comboBox = QtWidgets.QComboBox(self.frame)
        self.category_comboBox.setObjectName("category_lineEdit")
        self.gridLayout.addWidget(self.category_comboBox, 1, 1, 1, 1)
        self.category_comboBox.addItems(["Actualité","Sport","Politique","Technologie","Célébrités","Fashion","Autres"])
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 170, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.update_frequency_comboBox = QtWidgets.QComboBox(self.frame)
        self.update_frequency_comboBox.setObjectName("update_frequency_comboBox")
        self.gridLayout.addWidget(self.update_frequency_comboBox, 2, 1, 1, 1)
        self.update_frequency_comboBox.clear()
        self.update_frequency_comboBox.addItems(["15 minutes", "30 minutes", "45 minutes"])
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(70, 150, 311, 51))
        self.frame_2.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_submit_add = QtWidgets.QPushButton(self.frame_2)
        self.btn_submit_add.setObjectName("btn_submit_add")
        self.gridLayout_2.addWidget(self.btn_submit_add, 0, 0, 1, 1)
        self.btn_submit_add.clicked.connect(self.getAndSaveRssFeeds)

        self.btn_cancel_add = QtWidgets.QPushButton(self.frame_2)
        self.btn_cancel_add.setObjectName("btn_cancel_add")
        self.gridLayout_2.addWidget(self.btn_cancel_add, 0, 1, 1, 1)
        self.btn_cancel_add.clicked.connect(AddRssWindow.close)

        AddRssWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AddRssWindow)
        self.statusbar.setObjectName("statusbar")
        AddRssWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddRssWindow)
        QtCore.QMetaObject.connectSlotsByName(AddRssWindow)

    def retranslateUi(self, AddRssWindow):
        _translate = QtCore.QCoreApplication.translate
        AddRssWindow.setWindowTitle(_translate("AddRssWindow", "Nouveau Flux RSS"))
        self.label.setText(_translate("AddRssWindow", "Adresse du flux RSS : "))
        self.label_3.setText(_translate("AddRssWindow", "Catégorie :"))
        self.label_2.setText(_translate("AddRssWindow", "Fréquence de mise à jour :"))
        self.btn_submit_add.setText(_translate("AddRssWindow", "Valider"))
        self.btn_cancel_add.setText(_translate("AddRssWindow", "Annuler"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    AddRssWindow = QtWidgets.QMainWindow()
    ui = Ui_AddRssWindow()
    ui.setupUi(AddRssWindow)
    AddRssWindow.show()
    sys.exit(app.exec_())

