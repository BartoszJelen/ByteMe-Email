import  Spam_report as spam
import Send_msg as send_msg
import Get_msg as get
from Home import*
import Home
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SendWindow(object):


    def home_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HomeWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow, to = 'TO:', subject = 'SUBJECT: ', msg = 'Type msg here'):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1256, 711)
        MainWindow.setWindowTitle("Compose")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 221, 171))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../new_Gui/dev/byte.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.composeButton = QtWidgets.QPushButton(self.centralwidget)
        self.composeButton.setGeometry(QtCore.QRect(40, 240, 221, 71))
        self.composeButton.setText("compose")

        self.homeButton = QtWidgets.QPushButton(self.centralwidget)
        self.homeButton.setGeometry(QtCore.QRect(40, 330, 221, 71))
        self.homeButton.setText('Home')
        self.homeButton.clicked.connect(self.home_window)

        self.scanButton = QtWidgets.QPushButton(self.centralwidget)
        self.scanButton.setGeometry(QtCore.QRect(40, 420, 221, 71))
        self.scanButton.setText("SCAN")
        self.scanButton.clicked.connect(self.home_window)
        #report = spam.spam_report(full_emails)
        #self.scanButton.clicked.connect(lambda: Home.scan(report))

        self.trashButton = QtWidgets.QPushButton(self.centralwidget)
        self.trashButton.setGeometry(QtCore.QRect(40, 510, 221, 61))
        self.trashButton.setText("TRASH")

        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(790, 100, 181, 41))
        self.sendButton.setText("Send")
        self.sendButton.clicked.connect((lambda: send_msg.send("rideruniversitytest2019@gmail.com", "Rider2019",
                                                           self.toTextEdit.toPlainText(),
                                                           self.subjectTextEdit.toPlainText(),
                                                           self.msgTextEdit.toPlainText())))

        self.encdecButton = QtWidgets.QPushButton(self.centralwidget)
        self.encdecButton.setGeometry(QtCore.QRect(790, 40, 181, 41))
        self.encdecButton.setText("Encrypt")

        self.msgTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.msgTextEdit.setGeometry(QtCore.QRect(310, 190, 891, 381))
        self.msgTextEdit.setPlainText(msg)

        self.toTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.toTextEdit.setGeometry(QtCore.QRect(310, 20, 291, 61))
        self.toTextEdit.setPlainText(str(to))

        self.subjectTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.subjectTextEdit.setGeometry(QtCore.QRect(310, 90, 291, 61))
        self.subjectTextEdit.setPlainText(subject)

        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(1030, 10, 194, 28))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SendWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
