from PyQt5.QtWidgets import QApplication, QMainWindow
from gui.Window1Final import Window


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Window()
    ui.setWindowTitle("This is the window title")
    ui.show()
    sys.exit(app.exec_())