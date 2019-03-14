# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from main_app.GUI.add_rss_gui import Ui_AddRssWindow
from main_app.src.rssController import RssController

class Ui_MainWindow(object):
    def openAddRssWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AddRssWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        if self.ui.btn_submit_add.isChecked:
            rssController = RssController()
            dataList = rssController.getAllExistingData()
            for i in range(0, len(dataList)):
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(dataList[i]['news_title']))
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(dataList[i]['rss_address']))
                self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(dataList[i]['news_date'])))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(874, 487)
        MainWindow.setStyleSheet("font: 10pt \"Arial\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(2000, 2000))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_search = QtWidgets.QGridLayout()
        self.gridLayout_search.setObjectName("gridLayout_search")
        self.frame_search = QtWidgets.QFrame(self.centralwidget)
        self.frame_search.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(241, 161, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame_search.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_search.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_search.setObjectName("frame_search")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_search)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_search)
        self.label_2.setStyleSheet("font: 75 bold italic 10pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame_search)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../src/img/rssIcon.png"))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.frame_search)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_search = QtWidgets.QLineEdit(self.frame_search)
        self.lineEdit_search.setStyleSheet("selection-background-color: rgb(255, 170, 0);")
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.horizontalLayout.addWidget(self.lineEdit_search)
        self.gridLayout_search.addWidget(self.frame_search, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.gridLayout.addLayout(self.gridLayout_search, 0, 0, 1, 1)
        self.gridLayout_table = QtWidgets.QGridLayout()
        self.gridLayout_table.setObjectName("gridLayout_table")
        self.frame_table = QtWidgets.QFrame(self.centralwidget)
        self.frame_table.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_table.setObjectName("frame_table")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_table)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_table)
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setStyleSheet("selection-background-color: rgb(255, 170, 0);")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Panel)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setGridStyle(QtCore.Qt.DotLine)
        rssController = RssController()
        docsCount = rssController.getDocumentsCount()
        self.tableWidget.setRowCount(docsCount)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(0, 0, item)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.gridLayout_table.addWidget(self.frame_table, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_table, 1, 0, 1, 1)
        self.gridLayout_details = QtWidgets.QGridLayout()
        self.gridLayout_details.setObjectName("gridLayout_details")
        self.scrollArea_details = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_details.setFrameShape(QtWidgets.QFrame.Panel)
        self.scrollArea_details.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea_details.setWidgetResizable(True)
        self.scrollArea_details.setObjectName("scrollArea_details")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 852, 188))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textBrowser_details = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_details.setObjectName("textBrowser_details")
        self.horizontalLayout_3.addWidget(self.textBrowser_details)
        self.scrollArea_details.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_details.addWidget(self.scrollArea_details, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_details, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 874, 22))
        self.menubar.setStyleSheet("font: 10pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 170, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.menubar.setObjectName("menubar")
        self.menuBtns = QtWidgets.QMenu(self.menubar)
        self.menuBtns.setStyleSheet("border-color: rgb(209, 139, 0);")
        self.menuBtns.setObjectName("menuBtns")
        MainWindow.setMenuBar(self.menubar)
        self.actionBtn_subscribe = QtWidgets.QAction(MainWindow)
        self.actionBtn_subscribe.setObjectName("actionBtn_subscribe")
        self.actionBtn_subscribe.triggered.connect(self.openAddRssWindow)
        self.actionBtn_unsubscribe = QtWidgets.QAction(MainWindow)
        self.actionBtn_unsubscribe.setObjectName("actionBtn_unsubscribe")
        self.actionBtn_delete = QtWidgets.QAction(MainWindow)
        self.actionBtn_delete.setObjectName("actionBtn_delete")
        self.menuBtns.addAction(self.actionBtn_subscribe)
        self.menuBtns.addSeparator()
        self.menuBtns.addAction(self.actionBtn_unsubscribe)
        self.menuBtns.addSeparator()
        self.menuBtns.addAction(self.actionBtn_delete)
        self.menubar.addAction(self.menuBtns.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RSS Feeder"))
        self.label_2.setText(_translate("MainWindow", "Liste des bulletins de nouvelles"))
        self.label.setText(_translate("MainWindow", "Rechercher"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Titre"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Source"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Date"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        rssController = RssController()
        dataList = rssController.getAllExistingData()
        for i in range(0, len(dataList)):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(dataList[i]['news_title']))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(dataList[i]['rss_address']))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(dataList[i]['news_date'])))

        self.textBrowser_details.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium; font-weight:600;\">Détails de la nouvelle sélectionnée</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:xx-large; font-weight:600;\"><br /></p></body></html>"))
        self.menuBtns.setTitle(_translate("MainWindow", "Gestion des flux RSS"))
        self.actionBtn_subscribe.setText(_translate("MainWindow", "S\'abonner à un flux RSS"))
        self.actionBtn_subscribe.setChecked(False)
        self.actionBtn_unsubscribe.setText(_translate("MainWindow", "Se désabonner d\'un flux RSS"))
        self.actionBtn_delete.setText(_translate("MainWindow", "Supprimer un flux RSS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

