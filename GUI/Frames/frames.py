from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pymysql

connection = pymysql.connect(host='localhost',
                user='root',
                port = 3306,
                db='pythondb_connect',
                autocommit = True,
                )

cursor = connection.cursor()

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1088, 792)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 300, 331, 91))
        self.pushButton.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 300, 331, 91))
        self.pushButton_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1081, 741))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(80, 180, 361, 71))
        self.label.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(80, 260, 361, 71))
        self.label_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(80, 330, 361, 71))
        self.label_3.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(80, 410, 361, 71))
        self.label_4.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(500, 180, 371, 71))
        self.lineEdit.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(500, 260, 371, 71))
        self.lineEdit_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(500, 340, 371, 71))
        self.lineEdit_3.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(500, 420, 371, 71))
        self.lineEdit_4.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 570, 421, 81))
        self.pushButton_3.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1081, 741))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(230, 20, 631, 91))
        self.label_5.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1088, 31))
        self.menubar.setObjectName("menubar")
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLogin = QtWidgets.QAction(MainWindow)
        self.actionLogin.setObjectName("actionLogin")
        self.actionRegsiter = QtWidgets.QAction(MainWindow)
        self.actionRegsiter.setObjectName("actionRegsiter")
        self.menuMain.addAction(self.actionLogin)
        self.menuMain.addAction(self.actionRegsiter)
        self.menubar.addAction(self.menuMain.menuAction())

        self.frame.hide()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Register Now"))
        self.pushButton_2.setText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Enter Name"))
        self.label_2.setText(_translate("MainWindow", "Enter Email ID"))
        self.label_3.setText(_translate("MainWindow", "Enter Password"))
        self.label_4.setText(_translate("MainWindow", "Enter Company"))
        self.pushButton_3.setText(_translate("MainWindow", "Register"))
        self.label_5.setText(_translate("MainWindow", "Welcome to Management System"))
        self.menuMain.setTitle(_translate("MainWindow", "Main"))
        self.actionLogin.setText(_translate("MainWindow", "Login"))
        self.actionRegsiter.setText(_translate("MainWindow", "Home"))

        self.pushButton.clicked.connect(self.registerScreen)
        self.pushButton_3.clicked.connect(self.registration)

        self.actionRegsiter.triggered.connect(self.homeScreen)

    def homeScreen(self):
        self.frame.hide()

    def checkEmailId(self, emailId):
        print("Checking EmaildId")
        query = "SELECT * FROM employees"
        cursor.execute(query)

        for data in cursor:
            if emailId in data:
                # print("User Already Exist")
                raise ValueError("User Already Exist")

    def registerScreen(self):
        self.frame.show()
        self.frame_2.hide()

    def registration(self):

        username = self.lineEdit.text()
        email = self.lineEdit_2.text()
        password = self.lineEdit_3.text()
        company = self.lineEdit_4.text()

        # print("Details", username, email, password, company)
        try:
            self.checkEmailId(email)
            query = "INSERT INTO employees VALUES (%s,%s,%s,%s)"
            cursor.execute(query, (username, email, password, company))
            print("Data Inserted Successfully...")
            self.frame_2.show()
        except ValueError as err:
            # print(err)
            self.emailValidationPopUp()

    def emailValidationPopUp(self):
        QMessageBox.about(self,"Error","User Already Exist")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

