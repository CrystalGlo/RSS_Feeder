# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rss_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Flux RSS")
        Dialog.resize(763, 462)
        self.top_frame = QtWidgets.QFrame(Dialog)
        self.top_frame.setGeometry(QtCore.QRect(0, 10, 761, 41))
        self.top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")
        self.add_btn = QtWidgets.QPushButton(self.top_frame)
        self.add_btn.setGeometry(QtCore.QRect(10, 0, 141, 31))
        self.add_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 170, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.add_btn.setObjectName("add_btn")
        self.unsubscribe_btn = QtWidgets.QPushButton(self.top_frame)
        self.unsubscribe_btn.setGeometry(QtCore.QRect(160, 0, 161, 31))
        self.unsubscribe_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.unsubscribe_btn.setObjectName("unsubscribe_btn")
        self.search_label = QtWidgets.QLabel(self.top_frame)
        self.search_label.setGeometry(QtCore.QRect(450, 0, 71, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.search_label.sizePolicy().hasHeightForWidth())
        self.search_label.setSizePolicy(sizePolicy)
        self.search_label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.search_label.setObjectName("search_label")
        self.search_lineEdit = QtWidgets.QLineEdit(self.top_frame)
        self.search_lineEdit.setGeometry(QtCore.QRect(520, 0, 231, 21))
        self.search_lineEdit.setText("")
        self.search_lineEdit.setObjectName("search_lineEdit")
        self.list_scroll_area = QtWidgets.QScrollArea(Dialog)
        self.list_scroll_area.setGeometry(QtCore.QRect(10, 50, 741, 181))
        self.list_scroll_area.setWidgetResizable(True)
        self.list_scroll_area.setObjectName("list_scroll_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 739, 179))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.list_tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.list_tableWidget.setGeometry(QtCore.QRect(0, 0, 741, 181))
        self.list_tableWidget.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"")
        self.list_tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.list_tableWidget.setRowCount(10)
        self.list_tableWidget.setColumnCount(3)
        self.list_tableWidget.setObjectName("list_tableWidget")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(189, 189, 189))
        self.list_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(189, 189, 189))
        self.list_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(189, 189, 189))
        self.list_tableWidget.setHorizontalHeaderItem(2, item)
        self.list_scroll_area.setWidget(self.scrollAreaWidgetContents)
        self.details_scroll_area = QtWidgets.QScrollArea(Dialog)
        self.details_scroll_area.setGeometry(QtCore.QRect(10, 240, 741, 201))
        self.details_scroll_area.setWidgetResizable(True)
        self.details_scroll_area.setObjectName("details_scroll_area")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 739, 199))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.picture_graphic_view = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents_2)
        self.picture_graphic_view.setGeometry(QtCore.QRect(10, 10, 181, 161))
        self.picture_graphic_view.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.picture_graphic_view.setObjectName("picture_graphic_view")
        self.details_textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.details_textBrowser.setGeometry(QtCore.QRect(215, 10, 511, 181))
        self.details_textBrowser.setObjectName("details_textBrowser")
        self.details_scroll_area.setWidget(self.scrollAreaWidgetContents_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Flux RSS"))
        self.add_btn.setText(_translate("Dialog", "S\'abonner à un flux RSS"))
        self.unsubscribe_btn.setText(_translate("Dialog", "Se désabonner d\'un flux RSS"))
        self.search_label.setText(_translate("Dialog", "Recherche"))
        item = self.list_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Nouvelle"))
        item = self.list_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Source"))
        item = self.list_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Date"))
        self.details_textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Détails du flux RSS sélectionné</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

