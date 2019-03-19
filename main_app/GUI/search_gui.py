# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from main_app.src.rssController import RssController

class Ui_SearchWindow(object):
    def submitSearch(self):
        companyName = self.companyName_lineEdit.text()
        keyWord = self.keyWord_lineEdit.text()
        rssController = RssController()
        rssController.searchNews(companyName, keyWord)


    def setupUi(self, SearchWindow):
        SearchWindow.setObjectName("SearchWindow")
        SearchWindow.resize(525, 321)
        SearchWindow.setIconSize(QtCore.QSize(200, 200))
        self.centralwidget = QtWidgets.QWidget(SearchWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(2000, 2000))
        self.centralwidget.setStyleSheet("font: 75 Bold 10pt \"Arial\";\n"
"selection-background-color: rgb(255, 170, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 531, 319))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame.setMaximumSize(QtCore.QSize(318, 317))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_picture = QtWidgets.QLabel(self.frame)
        self.label_picture.setMaximumSize(QtCore.QSize(298, 297))
        self.label_picture.setText("")
        self.label_picture.setPixmap(QtGui.QPixmap("../src/img/search_icon.png"))
        self.label_picture.setObjectName("label_picture")
        self.gridLayout_4.addWidget(self.label_picture, 0, 0, 2, 2)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(-1, 49, 521, 151))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 121, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 71, 16))
        self.label_3.setObjectName("label_3")
        self.companyName_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.companyName_lineEdit.setGeometry(QtCore.QRect(150, 10, 341, 31))
        self.companyName_lineEdit.setStyleSheet("font: 9pt \"Arial\";\n"
"selection-background-color: rgb(255, 170, 0);")
        self.companyName_lineEdit.setObjectName("companyName_lineEdit")
        self.keyWord_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.keyWord_lineEdit.setGeometry(QtCore.QRect(150, 60, 341, 31))
        self.keyWord_lineEdit.setStyleSheet("font: 9pt \"Arial\";")
        self.keyWord_lineEdit.setObjectName("keyWord_lineEdit")
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 250, 521, 61))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.search_btn = QtWidgets.QPushButton(self.frame_3)
        self.search_btn.setGeometry(QtCore.QRect(110, 10, 101, 31))
        self.search_btn.setObjectName("search_btn")
        self.search_btn.clicked.connect(self.submitSearch)
        self.cancel_btn = QtWidgets.QPushButton(self.frame_3)
        self.cancel_btn.setGeometry(QtCore.QRect(310, 10, 101, 31))
        self.cancel_btn.setObjectName("cancel_btn")
        self.cancel_btn.clicked.connect(SearchWindow.close)
        self.gridLayout_3.addWidget(self.frame_3, 1, 0, 1, 1)
        SearchWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SearchWindow)
        QtCore.QMetaObject.connectSlotsByName(SearchWindow)

    def retranslateUi(self, SearchWindow):
        _translate = QtCore.QCoreApplication.translate
        SearchWindow.setWindowTitle(_translate("SearchWindow", "Recherche de bulletins de nouvelles"))
        self.label_2.setText(_translate("SearchWindow", "Nom d\'entreprise : "))
        self.label_3.setText(_translate("SearchWindow", "Mot clé :"))
        self.search_btn.setText(_translate("SearchWindow", "Chercher"))
        self.cancel_btn.setText(_translate("SearchWindow", "Annuler"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchWindow = QtWidgets.QMainWindow()
    ui = Ui_SearchWindow()
    ui.setupUi(SearchWindow)
    SearchWindow.show()
    sys.exit(app.exec_())

