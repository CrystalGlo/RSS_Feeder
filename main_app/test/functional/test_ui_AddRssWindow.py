import unittest
import sys
from unittest import TestCase
from unittest.mock import Mock
from PyQt5 import QtWidgets
from main_app.GUI.add_rss_gui import Ui_AddRssWindow

test_app = QtWidgets.QApplication(sys.argv)
class TestUi_AddRssWindow(TestCase):
    def setUp(self):
        self.AddRssWindow = QtWidgets.QMainWindow()
        self.addUi = Ui_AddRssWindow()
        self.addUi.setupUi(self.AddRssWindow)
        self.mock = Mock()
        print("In method", self._testMethodName)

    def test_validate_isCalled_when_submitAddBtn_isClicked(self):
        self.mock.addUi.validate()

        self.addUi.btn_submit_add.click()

        self.mock.addUi.validate.assert_called_once()


if __name__ == '__main__':
    unittest.main()
