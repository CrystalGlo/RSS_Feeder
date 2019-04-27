import sys
import unittest
from unittest import TestCase
from unittest.mock import Mock

from PyQt5 import QtWidgets

from main_app.GUI.add_rss_gui import Ui_AddRssWindow
from main_app.GUI.delete_gui import Ui_DeleteRssWindow
from main_app.GUI.main_gui import Ui_MainWindow
from main_app.GUI.unsubscribe_gui import Ui_UnsubscribeWindow

test_app = QtWidgets.QApplication(sys.argv)
class TestUi_MainWindow(TestCase):
    def setUp(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.mainUi = Ui_MainWindow()
        self.mainUi.setupUi(self.MainWindow)
        self.AddRssWindow = QtWidgets.QMainWindow()
        self.addUi = Ui_AddRssWindow()
        self.DeleteWindow = QtWidgets.QMainWindow()
        self.deleteUi = Ui_DeleteRssWindow()
        self.UnsubscribeWindow = QtWidgets.QMainWindow()
        self.unsubscribeUi = Ui_UnsubscribeWindow()
        self.mock = Mock()
        print("In method", self._testMethodName)


    def test_openAddRssWindow_do_open_addRssWindow(self):
        self.mock.AddRssWindow.show()

        self.mainUi.openAddRssWindow()

        self.mock.AddRssWindow.show.assert_called_once()

    def test_updateData_isCalled_when_updateBtn_isClicked(self):
        self.mock.mainUi.updateData()

        self.mainUi.btn_update.click()

        self.mock.mainUi.updateData.assert_called_once()

    def test_loadPreviousPage_removes1_from_pageIndex(self):
        pageIndexBefore = self.mainUi.pageIndex

        self.mainUi.loadPreviousPage()
        pageIndexAfter = self.mainUi.pageIndex

        self.assertEqual(pageIndexAfter, pageIndexBefore - 1)

    def test_loadNextPage_adds1_to_pageIndex(self):
        pageIndexBefore = self.mainUi.pageIndex

        self.mainUi.loadNextPage()
        pageIndexAfter = self.mainUi.pageIndex

        self.assertEqual(pageIndexAfter, pageIndexBefore + 1)

    def test_showSelectedNewsContent_isCalled_when_detailsBtn_isClicked(self):
        self.mock.mainUi.showSelectedNewsContent()

        self.mainUi.btn_details.click()

        self.mock.mainUi.showSelectedNewsContent.assert_called_once()

    def test_getSelectedTitle_return_exact_selectedTitle(self):
        self.mainUi.tableWidget.selectRow(2)
        selectedTitle = self.mainUi.tableWidget.item(2, 0).text()

        returnedTitle = self.mainUi.getSelectedTitle()

        self.assertEqual(returnedTitle, selectedTitle)

    def test_showSearchArea_isCalled_when_searchBtn_isClicked(self):
        self.mock.mainUi.showSearchArea()

        self.mainUi.btn_search.click()

        self.mock.mainUi.showSearchArea.assert_called_once()

    def test_submitSearch_isCalled_when_submitSearch_isClicked(self):
        self.mock.mainUi.submitSearch()

        self.mainUi.submitSearch_btn.click()

        self.mock.mainUi.submitSearch.assert_called_once()

    def test_cancelSearch_isCalled_when_cancelSearchBtn_isClicked(self):
        self.mock.mainUi.cancelSearch()

        self.mainUi.cancelSearch_btn.click()

        self.mock.mainUi.cancelSearch.assert_called_once()

    def test_cancelSearch_clears_search_and_occurrence_lineEdits(self):
        companyNameLineEdit = self.mainUi.companyName_lineEdit.text()
        keyWordLineEdit = self.mainUi.keyWord_lineEdit.text()
        occurrenceLineEdit = self.mainUi.lineEdit_occurrence.text()

        self.mainUi.cancelSearch_btn.click()

        self.assertFalse(companyNameLineEdit)
        self.assertFalse(keyWordLineEdit)
        self.assertFalse(occurrenceLineEdit)

    def test_submitOccurrence_isCalled_when_submitOccurrenceBtn_isClicked(self):
        self.mock.mainUi.submitOccurrence()

        self.mainUi.submitOccurrence_btn.click()

        self.mock.mainUi.submitOccurrence.assert_called_once()

    def test_clearSearchLineEdits_clears_searchLineEdits(self):
        companyNameLineEdit = self.mainUi.companyName_lineEdit.text()
        keyWordLineEdit = self.mainUi.keyWord_lineEdit.text()

        self.mainUi.clearSearchLineEdits()

        self.assertFalse(companyNameLineEdit)
        self.assertFalse(keyWordLineEdit)

    def test_clearOccurrenceLineEdit_clears_occurrenceLineEdit(self):
        occurrenceLineEdit = self.mainUi.lineEdit_occurrence.text()

        self.mainUi.clearOccurrenceLineEdit()

        self.assertFalse(occurrenceLineEdit)

    def test_cancelOccurrence_isCalled_when_cancelOccurrenceBtn_isClicked(self):
        self.mock.mainUi.cancelOccurrence()

        self.mainUi.cancelOccurrence_btn.click()

        self.mock.mainUi.cancelOccurrence.assert_called_once()

    def test_openUnsubscribeWindow_do_open_UnsubscribeWindow(self):
        self.mock.UnsubscribeWindow.show()

        self.mainUi.openUnsubscribeWindow()

        self.mock.UnsubscribeWindow.show.assert_called_once()

    def test_openDeleteWindow_do_open_DeleteWindow(self):
        self.mock.DeleteWindow.show()

        self.mainUi.openDeleteWindow()

        self.mock.DeleteWindow.show.assert_called_once()


if __name__ == '__main__':
    unittest.main()
