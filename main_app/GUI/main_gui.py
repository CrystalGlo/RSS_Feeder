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
from main_app.GUI.unsubscribe_gui import Ui_UnsubscribeWindow
from main_app.GUI.delete_gui import Ui_DeleteRssWindow
from main_app.src.htmlDelegate import HTMLDelegate
from main_app.src.rssController import RssController


class Ui_MainWindow(object):
    def __init__(self):
        self.rssController = RssController()
        self.searchAreaVisible = False
        self.pageIndex = 1
        self.dataList = []
        self.occurrenceWord = ""

    # Add new RSS section
    def openAddRssWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AddRssWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def updateData(self):
        self.occurrenceWord = ""
        self.rssController.updateRssEntries()
        self.dataList = self.rssController.getAllExistingData()
        self.pageIndex = 1
        self.btn_nextpage.setEnabled(True)
        self.displayData(self.dataList, self.pageIndex)

    def loadPreviousPage(self):
        self.btn_nextpage.setEnabled(True)
        self.pageIndex -= 1
        self.displayData(self.dataList, self.pageIndex)

    def loadNextPage(self):
        self.btn_prevpage.setEnabled(True)
        self.pageIndex += 1
        self.displayData(self.dataList, self.pageIndex)

    # Open selected news link in a server section
    def showSelectedNewsContent(self):
        title = self.getSelectedTitle()
        if title != "":
            link = self.rssController.getSelectedNewsLink(title)
            self.detailsView.load(QUrl(link))
            self.detailsView.setWindowTitle(title)
            self.detailsView.show()

    def getSelectedTitle(self):
        title = ""
        selectedRow = self.tableWidget.currentRow()
        if selectedRow >= 0:
            title = self.tableWidget.item(selectedRow, 0).text()
        return title

    # Search by company name and/or keyword
    def showSearchArea(self):
        if not self.searchAreaVisible:
            self.frame_search_collapse.show()
            self.searchAreaVisible = True
        else:
            self.frame_search_collapse.hide()
            self.searchAreaVisible = False

    def submitSearch(self):
        self.clearOccurrenceLineEdit()
        companyName = self.companyName_lineEdit.text().strip()
        keyWord = self.keyWord_lineEdit.text().strip()
        finalCursorList = []
        # Call searchNews function with a non empty attribute
        if companyName != "" or keyWord != "":
            if companyName != "" and keyWord == "":
                finalCursorList = self.rssController.searchNews(companyName)
            elif companyName == "" and keyWord != "":
                finalCursorList = self.rssController.searchNews(keyWord)
            elif companyName != "" and keyWord != "":
                finalCursorList = self.findCompanyNameAndKeyWordNews(companyName, keyWord)
            self.label_searchCount.setText(str(len(finalCursorList))+ " nouvelles trouvées")
            self.setSearchTable(finalCursorList)

    def findCompanyNameAndKeyWordNews(self, companyName, keyWord):
        searchCursorList = []
        companyNameAndKeyWordNewsTitles = []
        companyNameCursorList = self.rssController.searchNews(companyName)
        keyWordCursorList = self.rssController.searchNews(keyWord)
        companyNameNewsTitles = self.rssController.getNewsTitles(companyNameCursorList)
        keyWordNewsTitles = self.rssController.getNewsTitles(keyWordCursorList)
        # Delete duplicated news
        for cnTitle in companyNameNewsTitles:
            for kwTitle in keyWordNewsTitles:
                if cnTitle == kwTitle and cnTitle not in companyNameAndKeyWordNewsTitles:
                    companyNameAndKeyWordNewsTitles.append(cnTitle)
        for title in companyNameAndKeyWordNewsTitles:
            cursor = self.rssController.searchNewsByTitle(title)
            searchCursorList.append(cursor)

        return searchCursorList

    def setSearchTable(self, searchCursorList):
        if len(searchCursorList) == 0:
            self.tableWidget.setRowCount(0)
        else:
            self.pageIndex = 1
            self.btn_nextpage.setEnabled(True)
            documentList = []
            for cursor in searchCursorList:
                for document in cursor:
                    documentList.append(document)
            self.dataList = documentList
            self.displayData(self.dataList, self.pageIndex)

    def cancelSearch(self):
        self.clearSearchLineEdits()
        self.clearOccurrenceLineEdit()
        self.updateData()

    # Show occurrence of company name section
    def submitOccurrence(self):
        self.clearSearchLineEdits()
        self.occurrenceWord = self.lineEdit_occurrence.text().strip()
        if self.occurrenceWord != "":
            cursorList = self.rssController.searchNews(self.occurrenceWord)
            self.label_occurrenceCount.setText(self.occurrenceWord + " trouvé dans \n"+ str(len(cursorList)) + " nouvelles")
            self.setSearchTable(cursorList)
            # Change occurrence font color
            self.colorOccurrence()

    def colorOccurrence(self):
        allItems = self.tableWidget.findItems("", QtCore.Qt.MatchContains)
        selected_items = self.tableWidget.findItems(self.occurrenceWord, QtCore.Qt.MatchContains)
        for item in allItems:
            item.setData(QtCore.Qt.UserRole, self.occurrenceWord if item in selected_items else None)

    def clearSearchLineEdits(self):
        self.keyWord_lineEdit.setText("")
        self.companyName_lineEdit.setText("")
        self.label_searchCount.setText("")

    def clearOccurrenceLineEdit(self):
        self.lineEdit_occurrence.setText("")
        self.label_occurrenceCount.setText("")

    def cancelOccurrence(self):
        self.clearOccurrenceLineEdit()
        self.clearSearchLineEdits()
        self.updateData()

    # Common function of displaying data in the main table by pages
    def displayData(self, dataList, pageIndex):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(25)
        if len(dataList) < 25:
            pagesCount = 1
        else:
            pagesCount = round(len(dataList) / 25)
        self.label_pagenbr.setText("page " + str(pageIndex) + "/" + str(pagesCount))
        startIndex = (pageIndex - 1) * 25
        if pageIndex == 1:
            self.btn_prevpage.setEnabled(False)
        if pageIndex < pagesCount:
            lastIndex = startIndex + 25
        if pageIndex == pagesCount:
            self.btn_nextpage.setEnabled(False)
            lastIndex = len(dataList)
            self.tableWidget.setRowCount(lastIndex - startIndex)
        j = 0
        while j <= 25:
            for i in range(startIndex, lastIndex):
                self.tableWidget.setItem(j, 0, QtWidgets.QTableWidgetItem(dataList[i]['news_title']))
                self.tableWidget.setItem(j, 1, QtWidgets.QTableWidgetItem(dataList[i]['rss_address']))
                self.tableWidget.setItem(j, 2, QtWidgets.QTableWidgetItem(str(dataList[i]['news_date'])))
                j += 1
        if self.occurrenceWord != "":
            self.colorOccurrence()

    # Unsubscribe RSS section
    def openUnsubscribeWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_UnsubscribeWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    # Delete RSS section
    def openDeleteWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_DeleteRssWindow()
        self.ui.setupUi(self.window)
        self.window.show()

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
        self.btn_prevpage = QtWidgets.QPushButton(self.frame_search)
        icon_prev_page = QtGui.QIcon()
        icon_prev_page.addPixmap(QtGui.QPixmap("img/previous_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_prevpage.setIcon(icon_prev_page)
        self.btn_prevpage.setObjectName("btn_prevpage")
        self.horizontalLayout.addWidget(self.btn_prevpage)
        self.btn_prevpage.clicked.connect(self.loadPreviousPage)
        self.label_pagenbr = QtWidgets.QLabel(self.frame_search)
        self.label_pagenbr.setText("page")
        self.label_pagenbr.setObjectName("label_pagenbr")
        self.horizontalLayout.addWidget(self.label_pagenbr)
        self.btn_nextpage = QtWidgets.QPushButton(self.frame_search)
        icon_next_page = QtGui.QIcon()
        icon_next_page.addPixmap(QtGui.QPixmap("img/next_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_nextpage.setIcon(icon_next_page)
        self.btn_nextpage.setObjectName("btn_nextpage")
        self.horizontalLayout.addWidget(self.btn_nextpage)
        self.btn_nextpage.clicked.connect(self.loadNextPage)

        self.btn_update = QtWidgets.QPushButton(self.frame_search)
        self.btn_update.setStyleSheet("font: 75 bold 10pt \"Arial\";")
        self.btn_update.setText(" Actualiser")
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
        # Highlight occurrences
        self.tableWidget.setItemDelegate(HTMLDelegate(self.tableWidget))
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

        self.tableWidget.setRowCount(25)
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
        #self.gridLayout_search_collapse.setSpacing(1)
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
        self.label_searchCount = QtWidgets.QLabel(self.frame_search_collapse)
        self.label_searchCount.setStyleSheet("color: green;\n""font: 75 10pt \"Arial\";")
        self.label_searchCount.setObjectName("label_searchCount")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_searchCount)
        self.label_4 = QtWidgets.QLabel(self.frame_search_collapse)
        self.label_4.setStyleSheet("font: 75 Bold 10pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.companyName_lineEdit = QtWidgets.QLineEdit(self.frame_search_collapse)
        self.companyName_lineEdit.setObjectName("companyName_lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.companyName_lineEdit)
        self.label_5 = QtWidgets.QLabel(self.frame_search_collapse)
        self.label_5.setStyleSheet("font: 75 Bold 10pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.keyWord_lineEdit = QtWidgets.QLineEdit(self.frame_search_collapse)
        self.keyWord_lineEdit.setObjectName("keyWord_lineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.keyWord_lineEdit)
        self.submitSearch_btn = QtWidgets.QPushButton(self.frame_search_collapse)
        self.submitSearch_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.submitSearch_btn.setAutoDefault(False)
        self.submitSearch_btn.setDefault(False)
        self.submitSearch_btn.setFlat(False)
        self.submitSearch_btn.setObjectName("submitSearch_btn")
        self.submitSearch_btn.clicked.connect(self.submitSearch)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.submitSearch_btn)
        self.cancelSearch_btn = QtWidgets.QPushButton(self.frame_search_collapse)
        self.cancelSearch_btn.setObjectName("cancelSearch_btn")
        self.cancelSearch_btn.clicked.connect(self.cancelSearch)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.cancelSearch_btn)
        self.gridLayout_search_collapse.addWidget(self.frame_search_collapse, 0, 0, 1, 1)

        self.label_6 = QtWidgets.QLabel(self.frame_search_collapse)
        self.label_6.setStyleSheet("font: 75 Bold 10pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_occurrence = QtWidgets.QLineEdit(self.frame_search_collapse)
        self.lineEdit_occurrence.setObjectName("lineEdit_occurrence")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.lineEdit_occurrence)
        self.submitOccurrence_btn = QtWidgets.QPushButton(self.frame_search_collapse)
        self.submitOccurrence_btn.setObjectName("submitOccurrence_btn")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.submitOccurrence_btn)
        self.submitOccurrence_btn.clicked.connect(self.submitOccurrence)
        self.cancelOccurrence_btn = QtWidgets.QPushButton(self.frame_search_collapse)
        self.cancelOccurrence_btn.setObjectName("cancelOccurrence_btn")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.cancelOccurrence_btn)
        self.cancelOccurrence_btn.clicked.connect(self.cancelOccurrence)
        self.label_occurrenceCount = QtWidgets.QLabel(self.frame_search_collapse)
        self.label_occurrenceCount.setText("")
        self.label_occurrenceCount.setObjectName("label_occurrenceCount")
        self.label_occurrenceCount.setStyleSheet("color: blue;\n""font: 75 10pt \"Arial\";")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_occurrenceCount)
        self.gridLayout_search_collapse.addWidget(self.frame_search_collapse, 0, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_search_collapse)

        # RSS icon
        self.gridLayout_picture = QtWidgets.QGridLayout()
        self.gridLayout_picture.setObjectName("gridLayout_picture")
        self.frame_picture = QtWidgets.QFrame(self.centralwidget)
        # self.frame_picture.setFrameShape(QtWidgets.QFrame.Panel)
        # self.frame_picture.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_picture.setObjectName("frame_picture")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_picture)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_picture = QtWidgets.QLabel(self.frame_picture)
        self.label_picture.setObjectName("label_picture")
        self.label_picture.setText("")
        rss_pic = QtGui.QPixmap("img/rss_logo2.png").scaled(657, 220)
        self.label_picture.setPixmap(rss_pic)
        self.horizontalLayout.addWidget(self.label_picture)
        self.gridLayout_picture.addWidget(self.frame_picture, 0, 0, 1, 1, QtCore.Qt.AlignCenter)
        self.gridLayout.addLayout(self.gridLayout_picture, 2, 0, 1, 1)

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
        self.actionBtn_unsubscribe.triggered.connect(self.openUnsubscribeWindow)
        self.actionBtn_delete = QtWidgets.QAction(MainWindow)
        self.actionBtn_delete.setObjectName("actionBtn_delete")
        self.actionBtn_delete.triggered.connect(self.openDeleteWindow)
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
        self.btn_search.setText(_translate("MainWindow", "Recherche/Occurrences"))
        self.btn_details.setText(_translate("MainWindow", "Afficher les détails"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Titre"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Source"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Date"))

        self.updateData()
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.setItemDelegate(HTMLDelegate(self.tableWidget))

        self.label_4.setText(_translate("MainWindow", "Nom d\'entreprise :"))
        self.label_5.setText(_translate("MainWindow", "Mot clé :"))
        self.submitSearch_btn.setText(_translate("MainWindow", "Chercher"))
        self.cancelSearch_btn.setText(_translate("MainWindow", "Annuler"))
        self.label_6.setText(_translate("MainWindow", "Occurrence de:"))
        self.submitOccurrence_btn.setText(_translate("MainWindow", "Chercher"))
        self.cancelOccurrence_btn.setText(_translate("MainWindow", "Annuler"))

        self.menuBtns.setTitle(_translate("MainWindow", "Gestion des flux RSS"))
        self.actionBtn_subscribe.setText(_translate("MainWindow", "S\'abonner à un flux RSS"))
        self.actionBtn_subscribe.setChecked(False)
        self.actionBtn_unsubscribe.setText(_translate("MainWindow", "Se désabonner d\'un flux RSS"))
        self.actionBtn_delete.setText(_translate("MainWindow", "Supprimer un flux RSS"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    UnsubscribeWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(UnsubscribeWindow)
    UnsubscribeWindow.show()
    sys.exit(app.exec_())