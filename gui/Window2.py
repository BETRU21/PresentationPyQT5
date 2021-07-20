import os
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
import matplotlib.pyplot as plt
import numpy as np
import random

#from .tools.threadWorker import Worker

application_path = os.path.abspath("")

UiPath = os.path.dirname(os.path.realpath(__file__)) + '{0}Window1.ui'.format(os.sep)
Ui_MainWindow, QtBaseClass = uic.loadUiType(UiPath)

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(application_path + "{0}gui{0}misc{0}logo{0}logo.ico".format(os.sep)))
        self.connect_widgets()

    def connect_widgets(self):
        self.pb_changeState.clicked.connect(self.make_RGB)

    def make_RGB(self):
        X = 1920
        Y = 1080

        array = np.zeros((Y,X,3), dtype=np.uint8)

        for x in range(X):
            for y in range(Y):
                R = random.randrange(0,255)
                G = random.randrange(0,255)
                B = random.randrange(0,255)
                area = np.array([R,G,B])
                array[y,x,:] = area
        plt.imshow(array)
        plt.show()
        print(array)

