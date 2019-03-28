# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

from main_app.GUI.add_rss_gui import Ui_AddRssWindow
from main_app.src.rssController import RssController

class Ui_MainWindow(object):
    def __init__(self):
        self.rssController = RssController()
        self.searchAreaVisible = False

    def showSearchArea(self):
        if not self.searchAreaVisible:
            self.frame_search_collapse.show()
            self.searchAreaVisible = True
        else:
            self.frame_search_collapse.hide()
            self.searchAreaVisible = False

    def openAddRssWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AddRssWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def submitSearch(self):
        companyName = self.companyName_lineEdit.text().strip()
        keyWord = self.keyWord_lineEdit.text()
        cursorList = self.rssController.searchNews(companyName, keyWord)
        if len(cursorList) == 0:
            print("Liste des curseurs est vide!")
        i = 0
        self.tableWidget.setRowCount(0)
        for cursor in cursorList:
            for document in cursor:
                self.tableWidget.setRowCount(i+1)
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(document['news_title']))
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(document['rss_address']))
                self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(document['news_date'])))
                i = i+1

    def cancelSearch(self):
        self.companyName_lineEdit.setText("")
        self.keyWord_lineEdit.setText("")
        self.updateData()

    def getSelectedTitle(self):
        title = ""
        selectedRow = self.tableWidget.currentRow()
        if selectedRow >= 0:
            title = self.tableWidget.item(selectedRow, 0).text()
        return title

    def showSelectedNewsContent(self):
        title = self.getSelectedTitle()
        link = self.rssController.getSelectedNewsLink(title)
        self.detailsView.load(QUrl(link))
        self.detailsView.setWindowTitle(title)
        self.detailsView.show()

    def updateData(self):
        self.rssController.updateRssEntries()
        docsCount = self.rssController.getDocumentsCount()
        self.tableWidget.setRowCount(docsCount)
        dataList = self.rssController.getAllExistingData()
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
        self.detailsView = QWebEngineView()
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
        self.label_3.setPixmap(QtGui.QPixmap("img/rssIcon.png"))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)

        self.btn_update = QtWidgets.QPushButton(self.frame_search)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_update.sizePolicy().hasHeightForWidth())
        self.btn_update.setSizePolicy(sizePolicy)
        self.btn_update.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/refresh_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_update.setIcon(icon)
        self.btn_update.setIconSize(QtCore.QSize(30, 22))
        self.btn_update.setObjectName("btn_update")
        self.horizontalLayout.addWidget(self.btn_update)
        self.btn_update.clicked.connect(self.updateData)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.btn_details = QtWidgets.QPushButton(self.frame_search)
        self.btn_details.setStyleSheet("font: 75 bold 10pt \"Arial\";")
        self.btn_details.setObjectName("btn_details")
        self.horizontalLayout.addWidget(self.btn_details)
        self.btn_details.clicked.connect(self.showSelectedNewsContent)

        self.btn_search = QtWidgets.QPushButton(self.frame_search)
        self.btn_search.setStyleSheet("font: 75 bold 10pt \"Arial\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/search_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_search.setIcon(icon1)
        self.btn_search.setObjectName("btn_search")
        self.horizontalLayout.addWidget(self.btn_search)
        self.btn_search.clicked.connect(self.showSearchArea)

        self.gridLayout_search.addWidget(self.frame_search, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.gridLayout.addLayout(self.gridLayout_search, 0, 0, 1, 1)
        self.gridLayout_table = QtWidgets.QGridLayout()
        self.gridLayout_table.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_table.setSpacing(6)

        self.gridLayout_table.setObjectName("gridLayout_table")
        self.frame_table = QtWidgets.QFrame(self.centralwidget)
        self.frame_table.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_table.setObjectName("frame_table")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_table)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_table)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setStyleSheet("selection-background-color: rgb(255, 170, 0);")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Panel)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setGridStyle(QtCore.Qt.DotLine)

        docsCount = self.rssController.getDocumentsCount()
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

        # add collapse search Area
        self.gridLayout_search_collapse = QtWidgets.QGridLayout()
        self.gridLayout_search_collapse.setSpacing(1)
        self.gridLayout_search_collapse.setObjectName("gridLayout_search_collapse")
        self.frame_search_collapse = QtWidgets.QFrame(self.frame_table)
        self.frame_search_collapse.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_search_collapse.setStyleSheet("selection-background-color: rgb(255, 170, 0);")
        self.frame_search_collapse.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_search_collapse.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_search_collapse.setObjectName("frame_search_collapse")
        self.frame_search_collapse.hide()
        self.formLayout = QtWidgets.QFormLayout(self.frame_search_collapse)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.frame_search_collapse)
        self.label_4.setStyleSheet("selection-background-color: rgb(255, 170, 0);\n""font: 75 Bold 10pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.companyName_lineEdit = QtWidgets.QLineEdit(self.frame_search_collapse)
        self.companyName_lineEdit.setObjectName("companyName_lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.companyName_lineEdit)
        self.label_5 = QtWidgets.QLabel(self.frame_search_collapse)
        self.label_5.setStyleSheet("selection-background-color: rgb(255, 170, 0);\n""font: 75 Bold 10pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.keyWord_lineEdit = QtWidgets.QLineEdit(self.frame_search_collapse)
        self.keyWord_lineEdit.setObjectName("keyWord_lineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.keyWord_lineEdit)
        self.submitSearch_btn = QtWidgets.QPushButton(self.frame_search_collapse)
        self.submitSearch_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.submitSearch_btn.setAutoDefault(False)
        self.submitSearch_btn.setDefault(False)
        self.submitSearch_btn.setFlat(False)
        self.submitSearch_btn.setObjectName("submitSearch_btn")
        self.submitSearch_btn.clicked.connect(self.submitSearch)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.submitSearch_btn)
        self.cancelSearch_btn = QtWidgets.QPushButton(self.frame_search_collapse)
        self.cancelSearch_btn.setObjectName("cancelSearch_btn")
        self.cancelSearch_btn.clicked.connect(self.cancelSearch)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.cancelSearch_btn)
        self.gridLayout_search_collapse.addWidget(self.frame_search_collapse, 0, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_search_collapse)

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
        self.btn_search.setText(_translate("MainWindow", "Rechercher"))
        self.btn_details.setText(_translate("MainWindow", "Afficher les détails"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Titre"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Source"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Date"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.updateData()
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.label_4.setText(_translate("MainWindow", "Nom d\'entreprise :"))
        self.label_5.setText(_translate("MainWindow", "Mot clé :"))
        self.submitSearch_btn.setText(_translate("MainWindow", "Chercher"))
        self.cancelSearch_btn.setText(_translate("MainWindow", "Annuler"))

        self.menuBtns.setTitle(_translate("MainWindow", "Gestion des flux RSS"))
        self.actionBtn_subscribe.setText(_translate("MainWindow", "S\'abonner à un flux RSS"))
        self.actionBtn_subscribe.setChecked(False)
        self.actionBtn_unsubscribe.setText(_translate("MainWindow", "Se désabonner d\'un flux RSS"))
        self.actionBtn_delete.setText(_translate("MainWindow", "Supprimer un flux RSS"))
