import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class MainWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.username_input = qtw.QLineEdit()
        self.password_input = qtw.QLineEdit()
        self.password_input.setEchoMode(qtw.QLineEdit.Password)

        cancel_button = qtw.QPushButton("Cancel")
        submit_button = qtw.QPushButton("Submit", clicked=self.authenticate)

        layout = qtw.QFormLayout()  
        username_layout = qtw.QHBoxLayout()

        layout.addRow("Username", self.username_input)
        layout.addRow("Password", self.password_input)

        button_widget = qtw.QWidget()
        button_widget.setLayout(qtw.QHBoxLayout())
        button_widget.layout().addWidget(cancel_button)
        button_widget.layout().addWidget(submit_button)

        layout.addRow("", button_widget)

        self.setLayout(layout)

        self.show()


    def authenticate(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if username == "username" and password == "password":
            qtw.QMessageBox.information(self, "Success", "Youre logged in")
        else:
            qtw.QMessageBox.critical(self, "Error", "Wrong Login details")
        


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
