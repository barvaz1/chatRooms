import sys

from PyQt5.QtGui import QFont
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication

FONT = 'Times'
FONT_SIZE = 15


class OpenScreen(QDialog):
    def __init__(self):
        super(OpenScreen, self).__init__()
        loadUi("openScreen.ui", self)
        # self.button1.clicked.connect(self.goToScreen2)

        # change the text front in the text edit to  "'Times', 15"
        self.textEdit_user_name.setFont(QFont(FONT, FONT_SIZE))
        self.textEdit_password.setFont(QFont(FONT, FONT_SIZE))

        self.button_sign_in.clicked.connect(self.change_screen)

    def change_screen(self):
        global widget
        signUpScreen = SignUpScreen()
        widget.addWidget(signUpScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class SignUpScreen(QDialog):
    def __init__(self):
        super(SignUpScreen, self).__init__()
        loadUi("signUpScreen.ui", self)
        # self.button1.clicked.connect(self.goToScreen2)

        # change the text front in the text edit to  "'Times', 15"


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
