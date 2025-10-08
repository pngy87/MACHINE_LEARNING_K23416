from PyQt6.QtWidgets import QMessageBox

from retail_project.connectors.employee_connector import EmployeeConnector
from retail_project.uis.LoginMainWindow import Ui_Login


class LoginMainWindowEx(Ui_Login):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_Login.clicked.connect(self.process_login)

    def process_login(self):
        email = self.lineEdit_Email.text()
        pwd = self.lineEdit_Password.text()
        ec = EmployeeConnector()
        ec.connect()
        em = ec.login(email, pwd)
        if em == None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("Login Failed, please check your account again")
            msg.setWindowTitle("Login Failed")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("Congratulations, you are logged in")
            msg.setWindowTitle("Login Ok Ok")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()