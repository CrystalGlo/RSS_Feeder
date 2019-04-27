import unittest
import sys
from unittest import TestCase
from unittest.mock import Mock
from PyQt5 import QtWidgets
from main_app.GUI.delete_gui import Ui_DeleteRssWindow

test_app = QtWidgets.QApplication(sys.argv)
class TestUi_DeleteRssWindow(TestCase):
    def setUp(self):
        self.DeleteWindow = QtWidgets.QMainWindow()
        self.deleteUi = Ui_DeleteRssWindow()
        self.deleteUi.setupUi(self.DeleteWindow)
        self.mock = Mock()
        print("In method", self._testMethodName)

    def test_submitRemoval_isCalled_when_btnDelete_isClicked(self):
        self.mock.deleteUi.submitRemoval()

        self.deleteUi.btn_delete.click()

        self.mock.deleteUi.submitRemoval.assert_called_once()


if __name__ == '__main__':
    unittest.main()