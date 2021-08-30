import sys
import client

from PyQt5.QtGui import QFont
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication


SUCCESS = "success"


def change_screen_SignUp():
    global widget

    widget.addWidget(SignUpScreen())
    widget.setCurrentIndex(widget.currentIndex() + 1)


def change_screen_OpenScreen():
    global widget

    widget.addWidget(OpenScreen())
    widget.setCurrentIndex(widget.currentIndex() + 1)

def change_screen_lobby(name):
    global widget

    widget.addWidget(LobbyScreen(name))
    widget.setCurrentIndex(widget.currentIndex() + 1)


class OpenScreen(QDialog):
    def __init__(self):
        super(OpenScreen, self).__init__()
        loadUi("openScreen.ui", self)

        self.button_sign_in.clicked.connect(change_screen_SignUp)
        self.button_login.clicked.connect(self.log_in)

    def log_in(self):
        # try to log in
        msg = client.log_in(self.textEdit_user_name.toPlainText(), self.textEdit_password.toPlainText())

        print(msg)

        if msg == SUCCESS:

            change_screen_lobby(self.textEdit_user_name.toPlainText())
        else:
            # show the Error msg
            self.label_error.setText(msg)
            self.label_error.setStyleSheet("color: red")


class SignUpScreen(QDialog):
    def __init__(self):
        super(SignUpScreen, self).__init__()
        loadUi("signUpScreen.ui", self)

        self.button_back.clicked.connect(change_screen_OpenScreen)  # back to main screen
        self.button_sign_up.clicked.connect(self.sign_up)  # sign up
        # change the text front in the text edit to  "'Times', 15"

    def sign_up(self):
        print(1)
        # self.label_error.setText(
        text = client.sign_up(self.textEdit_user_name.toPlainText(), self.textEdit_lname.toPlainText(),
                              self.textEdit_fname.toPlainText(), self.textEdit_E_mail.toPlainText(),
                              self.textEdit_phone_num.toPlainText(),
                              self.textEdit_password.toPlainText(), self.textEdit_password2.toPlainText())
        print(text)
        self.label_error.setText(text)
        self.label_error.setStyleSheet("color: red")


class LobbyScreen(QDialog):
    def __init__(self, name):
        super(LobbyScreen, self).__init__()
        loadUi("LobbyScreen.ui", self)

        self.name = name
        # change the text front in the text edit to  "'Times', 15"
        self.label_welcome.setText("welcome, " + self.name + "!")
        self.label_welcome.setStyleSheet("""font: 36pt "MV Boli"; background-color: rgb(220, 234, 221); border-color: 
                rgb(255, 169, 21); border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 
                102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));""")
        self.label_welcome.setAlignment(QtCore.Qt.AlignCenter)

widget = None


def main():
    print("main")
    app = QApplication(sys.argv)
    global widget
    widget = QtWidgets.QStackedWidget()

    widget.addWidget(OpenScreen())

    widget.setFixedHeight(700)
    widget.setFixedWidth(900)

    widget.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
