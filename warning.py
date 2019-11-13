

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_warning(object):

    def setupUi(self, warning):
        warning.setObjectName("warning")
        warning.resize(470, 161)
        warning.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(warning)
        self.centralwidget.setObjectName("centralwidget")

        self.trashButton = QtWidgets.QPushButton(self.centralwidget)
        self.trashButton.setGeometry(QtCore.QRect(110, 110, 88, 27))
        self.trashButton.setText("Trash")

        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setGeometry(QtCore.QRect(260, 110, 88, 27))
        self.openButton.setText("Open")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 0, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("WARNING")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 60, 221, 41))
        self.label_2.setText("This message may contain a virus")

        warning.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(warning)
        self.statusbar.setObjectName("statusbar")
        warning.setStatusBar(self.statusbar)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    warning = QtWidgets.QMainWindow()
    ui = Ui_warning()
    ui.setupUi(warning)
    warning.show()
    sys.exit(app.exec_())
