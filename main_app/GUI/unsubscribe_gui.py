from PyQt5 import QtCore, QtGui, QtWidgets
from main_app.src.rssController import RssController

class Ui_UnsubscribeWindow(object):
    def submitUnsubscription(self):
        rssAddress = self.lineEdit_rssAddress.text().strip()
        existingRssAddresses = []
        if rssAddress == "":
            self.label_error.setText("L'adresse RSS ne doit pas être vide.")
        else:
            rssController = RssController()
            existingRssAddresses = rssController.getAllRssAddresses()
            if rssAddress not in existingRssAddresses:
                self.label_error.setText("Cette adresse RSS n'existe pas.")
            else:
                self.label_error.setText("")
                rssController.unsubscribeRss(rssAddress)
                self.btn_cancel.click()

    def setupUi(self, UnsubscribeWindow):
        UnsubscribeWindow.setObjectName("UnsubscribeWindow")
        UnsubscribeWindow.resize(451, 182)
        self.centralwidget = QtWidgets.QWidget(UnsubscribeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 431, 44))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_address = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame_address.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_address.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_address.setObjectName("frame_address")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_address)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_address)
        self.label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 170, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_rssAddress = QtWidgets.QLineEdit(self.frame_address)
        self.lineEdit_rssAddress.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.lineEdit_rssAddress.setObjectName("lineEdit_rssAddress")
        self.horizontalLayout.addWidget(self.lineEdit_rssAddress)
        self.gridLayout.addWidget(self.frame_address, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(80, 90, 301, 81))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_btn = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.frame_btn.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.frame_btn.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_btn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btn.setObjectName("frame_btn")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_btn)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_submit = QtWidgets.QPushButton(self.frame_btn)
        self.btn_submit.setObjectName("btn_submit")
        self.btn_submit.clicked.connect(self.submitUnsubscription)
        self.horizontalLayout_2.addWidget(self.btn_submit)
        self.btn_cancel = QtWidgets.QPushButton(self.frame_btn)
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_cancel.clicked.connect(UnsubscribeWindow.close)
        self.horizontalLayout_2.addWidget(self.btn_cancel)
        self.gridLayout_2.addWidget(self.frame_btn, 0, 1, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 0, 431, 36))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_error = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.frame_error.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_error.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_error.setObjectName("frame_error")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_error)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_error = QtWidgets.QLabel(self.frame_error)
        self.label_error.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")
        self.horizontalLayout_3.addWidget(self.label_error)
        self.gridLayout_3.addWidget(self.frame_error, 0, 0, 1, 1)
        UnsubscribeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(UnsubscribeWindow)
        QtCore.QMetaObject.connectSlotsByName(UnsubscribeWindow)

    def retranslateUi(self, UnsubscribeWindow):
        _translate = QtCore.QCoreApplication.translate
        UnsubscribeWindow.setWindowTitle(_translate("UnsubscribeWindow", "Se désabonner d\'un flux RSS"))
        self.label.setText(_translate("UnsubscribeWindow", "Adresse du flux RSS:       "))
        self.btn_submit.setText(_translate("UnsubscribeWindow", "Se désabonner"))
        self.btn_cancel.setText(_translate("UnsubscribeWindow", "Annuler"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UnsubscribeWindow = QtWidgets.QMainWindow()
    ui = Ui_UnsubscribeWindow()
    ui.setupUi(UnsubscribeWindow)
    UnsubscribeWindow.show()
    sys.exit(app.exec_())

