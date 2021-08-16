import sys
import client

from PyQt5.QtGui import QFont
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication


class OpenScreen(QDialog):
    def __init__(self):
        super(OpenScreen, self).__init__()
        loadUi("openScreen.ui", self)
        # self.button1.clicked.connect(self.goToScreen2)

        self.button_sign_in.clicked.connect(self.change_screen_SignUp)

    def change_screen_SignUp(self):
        global widget
        signUpScreen = SignUpScreen()
        widget.addWidget(signUpScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class SignUpScreen(QDialog):
    def __init__(self):
        super(SignUpScreen, self).__init__()
        loadUi("signUpScreen.ui", self)

        self.button_back.clicked.connect(self.change_screen_OpenScreen)  # back to main screen
        self.button_sign_up.clicked.connect(self.sign_up)  # sign up
        # change the text front in the text edit to  "'Times', 15"

    def change_screen_OpenScreen(self):
        global widget
        openScreen = OpenScreen()
        widget.addWidget(openScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def sign_up(self):
        print(1)
        # self.label_error.setText(
        client.sign_up(self.textEdit_user_name.toPlainText(), self.textEdit_lname.toPlainText(),
                       self.textEdit_fname.toPlainText(), self.textEdit_E_mail.toPlainText(),
                       self.textEdit_phone_num.toPlainText(),
                       self.textEdit_password.toPlainText(), self.textEdit_password2.toPlainText())


widget = None


def main():
    print("main")
    app = QApplication(sys.argv)
    global widget
    widget = QtWidgets.QStackedWidget()
    openScreen = OpenScreen()

    widget.addWidget(openScreen)

    widget.setFixedHeight(700)
    widget.setFixedWidth(900)

    widget.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
