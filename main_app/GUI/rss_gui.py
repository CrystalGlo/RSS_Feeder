# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rss_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from main_app.GUI.add_rss_gui import Ui_AddRssWindow
import pprint
import pymongo

class Ui_MainWindow(object):
    def openAddRssWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AddRssWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        # Connect to rssDB
        client = pymongo.MongoClient()
        rssDB = client.get_database("rssDB")
        rssCollection = rssDB.get_collection("rss_collection")

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(839, 551)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 831, 491))
        self.frame.setStyleSheet("selection-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 170, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_search = QtWidgets.QFrame(self.frame)
        self.frame_search.setGeometry(QtCore.QRect(600, 0, 241, 41))
        self.frame_search.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_search.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_search.setObjectName("frame_search")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_search)
        self.gridLayout.setObjectName("gridLayout")
        self.label_search = QtWidgets.QLabel(self.frame_search)
        self.label_search.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_search.setObjectName("label_search")
        self.gridLayout.addWidget(self.label_search, 0, 0, 1, 1)
        self.lineEdit_search = QtWidgets.QLineEdit(self.frame_search)
        self.lineEdit_search.setText("")
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.gridLayout.addWidget(self.lineEdit_search, 0, 1, 1, 1)
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 821, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableWidget.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)
        # Add RSS feeds to the news table
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        for data in rssCollection.find({"rss_address": {"$exists": True}}):
            pprint.pprint(data["news_title"])
            self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(data["news_title"]))
            self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(data["rss_address"]))
            self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(data["news_date"]))

        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 270, 831, 231))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_2)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 821, 221))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 802, 274))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_img = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_img.setText("")
        self.label_img.setPixmap(QtGui.QPixmap("../src/img/nature.jpg"))
        self.label_img.setObjectName("label_img")
        self.gridLayout_3.addWidget(self.label_img, 0, 0, 2, 1)
        self.textBrowser_details = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.textBrowser_details.setObjectName("textBrowser_details")
        self.gridLayout_3.addWidget(self.textBrowser_details, 0, 1, 2, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 16))
        self.label.setStyleSheet("font: 75 bold italic 10pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 170, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(160, 0, 31, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../src/img/rssIcon.png"))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 839, 21))
        self.menubar.setObjectName("menubar")
        self.menu_options = QtWidgets.QMenu(self.menubar)
        self.menu_options.setObjectName("menu_options")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menu_btn_subscribe = QtWidgets.QAction(MainWindow)
        self.menu_btn_subscribe.setObjectName("menu_btn_subscribe")
        self.menu_btn_subscribe.triggered.connect(self.openAddRssWindow)
        self.menu_btn_unsubscribe = QtWidgets.QAction(MainWindow)
        self.menu_btn_unsubscribe.setObjectName("menu_btn_unsubscribe")
        self.menu_btn_delete = QtWidgets.QAction(MainWindow)
        self.menu_btn_delete.setObjectName("menu_btn_delete")
        self.menu_options.addAction(self.menu_btn_subscribe)
        self.menu_options.addSeparator()
        self.menu_options.addAction(self.menu_btn_unsubscribe)
        self.menu_options.addSeparator()
        self.menu_options.addAction(self.menu_btn_delete)
        self.menubar.addAction(self.menu_options.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RSS Feeder"))
        self.label_search.setText(_translate("MainWindow", "Recherche"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nouvelle"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Source"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Date"))
        self.textBrowser_details.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Détails de la nouvelle sélectionnée</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Liste des Flux RSS"))
        self.menu_options.setTitle(_translate("MainWindow", "Gestion des Flux RSS"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menu_btn_subscribe.setText(_translate("MainWindow", "S\'abonner à un flux RSS"))
        self.menu_btn_unsubscribe.setText(_translate("MainWindow", "Se désabonner d\'un flux RSS"))
        self.menu_btn_delete.setText(_translate("MainWindow", "Supprimer un flux RSS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

