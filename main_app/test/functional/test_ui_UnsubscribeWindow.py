import unittest
import sys
from unittest import TestCase
from unittest.mock import Mock
from PyQt5 import QtWidgets
from main_app.GUI.unsubscribe_gui import Ui_UnsubscribeWindow

test_app = QtWidgets.QApplication(sys.argv)
class TestUi_UnsubscribeWindow(TestCase):
    def setUp(self):
        self.UnsubscribeWindow = QtWidgets.QMainWindow()
        self.unsubscribeUi = Ui_UnsubscribeWindow()
        self.unsubscribeUi.setupUi(self.UnsubscribeWindow)
        self.mock = Mock()
        print("In method", self._testMethodName)

    def test_submitUnsubscription_isCalled_when_btnSubmit_isClicked(self):
        self.mock.unsubscribeUi.submitUnsubscription()

        self.unsubscribeUi.btn_submit.click()

        self.mock.unsubscribeUi.submitUnsubscription.assert_called_once()

if __name__ == '__main__':
    unittest.main()