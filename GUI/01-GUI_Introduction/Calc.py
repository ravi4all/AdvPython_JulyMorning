from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1081, 767)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 170, 331, 61))
        self.label.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 280, 351, 61))
        self.label_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(580, 160, 391, 81))
        self.lineEdit.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(580, 280, 391, 81))
        self.lineEdit_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(580, 430, 391, 81))
        self.lineEdit_3.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 440, 351, 61))
        self.label_3.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 560, 101, 71))
        self.pushButton.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 560, 101, 71))
        self.pushButton_2.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 560, 101, 71))
        self.pushButton_3.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(590, 560, 101, 71))
        self.pushButton_4.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(730, 560, 221, 71))
        self.pushButton_5.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1081, 31))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNormal = QtWidgets.QAction(MainWindow)
        self.actionNormal.setObjectName("actionNormal")
        self.actionScientific = QtWidgets.QAction(MainWindow)
        self.actionScientific.setObjectName("actionScientific")
        self.menuOptions.addAction(self.actionNormal)
        self.menuOptions.addAction(self.actionScientific)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter first number"))
        self.label_2.setText(_translate("MainWindow", "Enter second number"))
        self.label_3.setText(_translate("MainWindow", "Result"))
        self.pushButton.setText(_translate("MainWindow", "+"))
        self.pushButton_2.setText(_translate("MainWindow", "-"))
        self.pushButton_3.setText(_translate("MainWindow", "/"))
        self.pushButton_4.setText(_translate("MainWindow", "*"))
        self.pushButton_5.setText(_translate("MainWindow", "="))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionNormal.setText(_translate("MainWindow", "Normal"))
        self.actionScientific.setText(_translate("MainWindow", "Scientific"))

        self.lineEdit_3.setReadOnly(True)

        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.sub)
        self.pushButton_3.clicked.connect(self.div)
        self.pushButton_4.clicked.connect(self.mul)


    def add(self):
        # print("Add function called...")
        self.num_1 = int(self.lineEdit.text())
        self.num_2 = int(self.lineEdit_2.text())
        self.result = self.num_1 + self.num_2

        self.lineEdit_3.setText(str(self.result))

    def sub(self):
        # print("Sub function called...")
        self.num_1 = int(self.lineEdit.text())
        self.num_2 = int(self.lineEdit_2.text())
        self.result = self.num_1 - self.num_2

        self.lineEdit_3.setText(str(self.result))

    def div(self):
        # print("Div function called...")
        self.num_1 = int(self.lineEdit.text())
        self.num_2 = int(self.lineEdit_2.text())
        self.result = self.num_1 / self.num_2

        self.lineEdit_3.setText(str(self.result))

    def mul(self):
        self.num_1 = int(self.lineEdit.text())
        self.num_2 = int(self.lineEdit_2.text())
        self.result = self.num_1 * self.num_2

        self.lineEdit_3.setText(str(self.result))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

