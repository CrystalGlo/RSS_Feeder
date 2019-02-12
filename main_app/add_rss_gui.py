# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_rss_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(442, 245)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 131, 21))
        self.label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.rss_adress_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.rss_adress_lineEdit.setGeometry(QtCore.QRect(190, 20, 231, 31))
        self.rss_adress_lineEdit.setObjectName("rss_adress_lineEdit")
        self.update_frequency_comboBox = QtWidgets.QComboBox(Dialog)
        self.update_frequency_comboBox.setGeometry(QtCore.QRect(190, 120, 231, 31))
        self.update_frequency_comboBox.setObjectName("update_frequency_comboBox")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 161, 16))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.category_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.category_lineEdit.setGeometry(QtCore.QRect(190, 70, 231, 31))
        self.category_lineEdit.setObjectName("category_lineEdit")
        self.add_submit_btn = QtWidgets.QPushButton(Dialog)
        self.add_submit_btn.setGeometry(QtCore.QRect(50, 190, 91, 31))
        self.add_submit_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 170, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.add_submit_btn.setObjectName("add_submit_btn")
        self.add_cancel_btn = QtWidgets.QPushButton(Dialog)
        self.add_cancel_btn.setGeometry(QtCore.QRect(260, 190, 91, 31))
        self.add_cancel_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.add_cancel_btn.setObjectName("add_cancel_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "S'abonner à un nouveau RSS"))
        self.label.setText(_translate("Dialog", "Adresse du flux RSS : "))
        self.label_2.setText(_translate("Dialog", "Fréquence de mise à jour :"))
        self.label_3.setText(_translate("Dialog", "Catégorie :"))
        self.add_submit_btn.setText(_translate("Dialog", "Valider"))
        self.add_cancel_btn.setText(_translate("Dialog", "Annuler"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

