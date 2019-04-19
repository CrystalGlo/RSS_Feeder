from PyQt5 import QtCore, QtGui, QtWidgets
from main_app.src.rssController import RssController

class Ui_DeleteRssWindow(object):
    def submitRemoval(self):
        rssAddress = self.lineEdit_address.text().strip()
        if rssAddress == "":
            self.label_error.setText("L'adresse RSS ne doit pas être vide.")
        else:
            rssController = RssController()
            existingRssAddresses = rssController.getAllRssAddresses()
            if rssAddress not in existingRssAddresses:
                self.label_error.setText("Cette adresse RSS n'existe pas.")
            else:
                self.label_error.setText("")
                rssController.deleteRss(rssAddress)
                self.btn_cancel.click()

    def setupUi(self, DeleteRssWindow):
        DeleteRssWindow.setObjectName("DeleteRssWindow")
        DeleteRssWindow.resize(452, 211)
        self.centralwidget = QtWidgets.QWidget(DeleteRssWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 431, 36))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_error = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame_error.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_error.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_error.setObjectName("frame_error")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_error)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_error = QtWidgets.QLabel(self.frame_error)
        self.label_error.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")
        self.horizontalLayout.addWidget(self.label_error)
        self.gridLayout.addWidget(self.frame_error, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 431, 51))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_address = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.frame_address.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_address.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_address.setObjectName("frame_address")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_address)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_address)
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 170, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_address = QtWidgets.QLineEdit(self.frame_address)
        self.lineEdit_address.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.lineEdit_address.setObjectName("lineEdit_address")
        self.horizontalLayout_2.addWidget(self.lineEdit_address)
        self.gridLayout_2.addWidget(self.frame_address, 0, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(80, 110, 301, 91))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_btns = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.frame_btns.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.frame_btns.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns.setObjectName("frame_btns")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_btns)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_delete = QtWidgets.QPushButton(self.frame_btns)
        self.btn_delete.setObjectName("btn_delete")
        self.btn_delete.clicked.connect(self.submitRemoval)
        self.horizontalLayout_3.addWidget(self.btn_delete)
        self.btn_cancel = QtWidgets.QPushButton(self.frame_btns)
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_cancel.clicked.connect(DeleteRssWindow.close)
        self.horizontalLayout_3.addWidget(self.btn_cancel)
        self.gridLayout_3.addWidget(self.frame_btns, 0, 0, 1, 1)
        DeleteRssWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DeleteRssWindow)
        QtCore.QMetaObject.connectSlotsByName(DeleteRssWindow)

    def retranslateUi(self, DeleteRssWindow):
        _translate = QtCore.QCoreApplication.translate
        DeleteRssWindow.setWindowTitle(_translate("DeleteRssWindow", "Supprimer un flux RSS"))
        self.label_2.setText(_translate("DeleteRssWindow", "Adresse du flux RSS :        "))
        self.btn_delete.setText(_translate("DeleteRssWindow", "Supprimer"))
        self.btn_cancel.setText(_translate("DeleteRssWindow", "Annuler"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DeleteRssWindow = QtWidgets.QMainWindow()
    ui = Ui_DeleteRssWindow()
    ui.setupUi(DeleteRssWindow)
    DeleteRssWindow.show()
    sys.exit(app.exec_())

