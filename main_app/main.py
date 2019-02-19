import sys
from PyQt5 import QtWidgets
from main_app.GUI.rss_gui import Ui_MainWindow


class MainWindow(Ui_MainWindow):
    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     # Style
#     app.setStyle('Fusion')
#     dark_palette = QPalette()
#
#     dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
#     dark_palette.setColor(QPalette.WindowText, Qt.white)
#     dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
#     dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
#     dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
#     dark_palette.setColor(QPalette.ToolTipText, Qt.white)
#     dark_palette.setColor(QPalette.Text, Qt.white)
#     dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
#     dark_palette.setColor(QPalette.ButtonText, Qt.white)
#     dark_palette.setColor(QPalette.BrightText, Qt.red)
#     dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
#     dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
#     dark_palette.setColor(QPalette.HighlightedText, Qt.black)
#
#     app.setPalette(dark_palette)
#     app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
#
#     dialog = QtWidgets.QDialog()
#     prog = MainWindow(dialog)
#     dialog.show()
#     sys.exit(app.exec_())

