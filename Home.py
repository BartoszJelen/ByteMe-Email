
from PyQt5 import QtCore, QtGui, QtWidgets
import  Spam_report as spam
import Get_msg as get
from send_window import*
from warning import*
#from send_window import Ui_SendWindow

class Ui_HomeWindow(object ):


    def send_widnow(self, to = 'TO:', subject = 'SUBJECT: ', msg = 'Type msg here'):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SendWindow()
        self.ui.setupUi(self.window, to, subject, msg)
        self.window.show()


    def home_window(self):
        self.listWidget.clear()
        self.listWidget.addItem('YOUR NEW MESSAGES (double click to open message)\n')

        for sender in self.senders_list:
            self.item = QtWidgets.QListWidget()
            # print(sender)
            self.listWidget.addItem(sender)

        for i in range(self.listWidget.count()):
            if self.listWidget.item(i).text() == 'YOUR NEW MESSAGES (double click to open message)\n':
                continue
            else:
                self.listWidget.item(i).setText(self.listWidget.item(i).text() + " MSG" + str(i))

        self.replyButton.hide()
        self.decryptButton.hide()
        self.forwordButton.hide()

    def warning(self):
        print('war')
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_warning()
        self.ui.setupUi(self.window)
        self.window.show()

    def scan(self, spam_report):
        print("scanning")
        self.listWidget.clear()
        self.listWidget.addItem(spam_report)
        # BUG NO DEFULT BEHAVIOR RESTORED AFTER
        self.listWidget.itemClicked.connect(self.warning )


        self.replyButton.hide()
        self.decryptButton.hide()
        self.forwordButton.hide()

    def show_message(self):
        ### prnt for test only
        print(self.listWidget.currentItem().text())
        current_item = self.listWidget.currentItem().text()
        key = current_item[-4:]
        print(key)
        msg = self.email_dic[key]
        print(self.email_dic[key])
        self.listWidget.clear()
        self.listWidget.addItem("Message from: " + current_item + "\n\n" + msg)


        self.forwordButton.show()
        self.decryptButton.show()
        self.replyButton.show()

        self.replyButton.clicked.connect(lambda: self.send_widnow(current_item))
        self.forwordButton.clicked.connect(lambda: self.send_widnow('TO: ', "RE: ", msg) )


    def setupUi(self, MainWindow):
        global senders_list, topic_list, email_dic, date_list, full_emails

        # get EMAIL headers
        # =-=-=-=-=-=-=-=-=-=-=-=- =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        # global senders_list, topic_list, email_dic, date_list, email_body_list
        self.senders_list, self.topic_list, self.email_dic, date_list, full_emails = get.connect(self)
        print(full_emails)


        MainWindow.resize(1256, 711)
        MainWindow.setWindowTitle("Home")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 221, 171))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../new_Gui/dev/byte.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- WIDGETS =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

        self.composeButton = QtWidgets.QPushButton(self.centralwidget)
        self.composeButton.setGeometry(QtCore.QRect(40, 240, 221, 71))
        self.composeButton.setText("COMPOSE")
        self.composeButton.clicked.connect(self.send_widnow)

        self.homeButton = QtWidgets.QPushButton(self.centralwidget)
        self.homeButton.setGeometry(QtCore.QRect(40, 330, 221, 71))
        self.homeButton.setText("HOME")
        self.homeButton.clicked.connect(self.home_window)

        self.scanButton = QtWidgets.QPushButton(self.centralwidget)
        self.scanButton.setGeometry(QtCore.QRect(40, 420, 221, 71))
        self.scanButton.setText("SCAN")
        report = spam.spam_report(full_emails)
        self.scanButton.clicked.connect(lambda: self.scan(report))


        self.trashButton = QtWidgets.QPushButton(self.centralwidget)
        self.trashButton.setGeometry(QtCore.QRect(40, 510, 221, 61))
        self.trashButton.setText("TRASH")


        self.decryptButton = QtWidgets.QPushButton(self.centralwidget)
        self.decryptButton.setGeometry(QtCore.QRect(390, 620, 221, 61))
        self.decryptButton.setText("Decrypt")
        self.decryptButton.hide()

        self.replyButton = QtWidgets.QPushButton(self.centralwidget)
        self.replyButton.setGeometry(QtCore.QRect(620, 620, 221, 61))
        self.replyButton.setText("Reply")
        self.replyButton.hide()

        self.forwordButton = QtWidgets.QPushButton(self.centralwidget)
        self.forwordButton.setGeometry(QtCore.QRect(850, 620, 221, 61))
        self.forwordButton.setText("Forword")
        self.forwordButton.hide()

        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(1000, 20, 118, 28))
        #self.timeEdit.setTime()

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(320, 80, 891, 525))

        self.listWidget.itemDoubleClicked.connect(self.show_message)

        #add Emails to list
        # =-=-=-=-=-=-=-=-=-=-=-=- =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        self.home_window()

        # --------------------------------------------------------------------------
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 10, 191, 71))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1256, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # --------------------------------------------------------------------------


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_HomeWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

