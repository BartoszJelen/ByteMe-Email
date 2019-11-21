
from PyQt5 import QtCore, QtGui, QtWidgets
import  Spam_report as spam
import Get_msg as get
from send_window import*
import Encryptors



class Ui_HomeWindow:


    def send_widnow(self, to = 'TO:', subject = 'SUBJECT: ', msg = 'Type msg here'):
        '''opens send window'''

        self.window = QtWidgets.QMainWindow()
        # Ui_SendWindow imported from send_window
        self.ui = Ui_SendWindow()
        self.ui.setupUi(self.window, to, subject, msg)
        self.window.show()


    def home_window(self):
        ''' creates home window'''

        self.listWidget.clear()
        self.listWidget.addItem('YOUR NEW MESSAGES (double click to open message)\n')

        # import messages
        for sender in self.senders_list:
            self.item = QtWidgets.QListWidget()
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
        ''' creates warrning window form Ui_warrning class (end of the code)'''

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_warning()
        self.ui.setupUi(self.window)
        self.window.show()

    def scan(self, spam_report):
        '''creates scan report window'''

        self.listWidget.clear()
        self.listWidget.addItem(spam_report)
        # BUG NO DEFULT BEHAVIOR RESTORED AFTER
        self.listWidget.itemClicked.connect(self.warning)


        self.replyButton.hide()
        self.decryptButton.hide()
        self.forwordButton.hide()

    def show_message(self):
        '''updates home window with selected message'''

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

        # ACTIONS
        self.replyButton.clicked.connect(lambda: self.send_widnow(current_item))
        self.forwordButton.clicked.connect(lambda: self.send_widnow('TO: ', "RE: ", msg) )
        self.decryptButton.clicked.connect(lambda: decrypt(msg))

        def decrypt(msg):
            '''decrypts message'''
            try:
                key_from_msg = msg.strip()
                key1 = key_from_msg[-1]
                key1 = int(key1)

                decrypted_msg = Encryptors.Decrypt_Cezar(key1, msg)
                decrypted_msg = decrypted_msg.strip()
                decrypted_msg = decrypted_msg[0:-1]
                self.listWidget.clear()
                self.listWidget.addItem("Message from: " + current_item + "\n\n" + decrypted_msg)
            except:
                ''' implement pop window here '''
                print("sth went wrong")

            #self.listWidget.addItem("Message from: " + current_item + "\n\n" + decrypted_msg)

    def setupUi(self, MainWindow):
        '''home window / main function'''

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

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(320, 80, 891, 525))

        # show message on double click
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


# EXTENDS HOME WINDOW CLASS
class Ui_warning(Ui_HomeWindow):

    def move_to_trash(self):
        ''' moves msg to trash'''
        pass

    def show_message_scan(self):
        '''opens home window '''

        pass

    def setupUi(self, warning):
        warning.setObjectName("warning")
        warning.resize(470, 161)
        warning.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(warning)
        self.centralwidget.setObjectName("centralwidget")

        self.trashButton = QtWidgets.QPushButton(self.centralwidget)
        self.trashButton.setGeometry(QtCore.QRect(110, 110, 88, 27))
        self.trashButton.setText("Trash")
        self.trashButton.clicked.connect(self.move_to_trash)

        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setGeometry(QtCore.QRect(260, 110, 88, 27))
        self.openButton.setText("Open")
        self.openButton.clicked.connect(self.show_message_scan)

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
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_HomeWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
