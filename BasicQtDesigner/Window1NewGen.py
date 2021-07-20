import os
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets

UiPath = os.path.dirname(os.path.realpath(__file__)) + '{0}Window1.ui'.format(os.sep)
Ui_MainWindow, QtBaseClass = uic.loadUiType(UiPath)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())