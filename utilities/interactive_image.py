"""
Module for show image in interactive window
"""
import sys

import matplotlib
import matplotlib.pyplot as plt
import cv2
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np

matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, img: np.array, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.img = img

        # Create the matplotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        sc = MplCanvas(width=5, height=4, dpi=100)

        # plot the pandas DataFrame, passing in the
        # matplotlib Canvas axes.
        plt.imshow(self.img)
        plt.show()

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()


if __name__ == '__main__':
    path = '/Users/dmitry/Library/CloudStorage/GoogleDrive-ceo@gangai.pro/Мой диск/Проекты/virtual ads/chess board ' \
           'foto/6125290719.jpg'
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow(img)
