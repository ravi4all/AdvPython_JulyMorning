from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pymysql

connection = pymysql.connect(host='localhost',
                user='root',
                port = 3306,
                db='testengine',
                autocommit = True,
                )

cursor = connection.cursor()

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1087, 778)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(340, 70, 371, 71))
        self.comboBox.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 560, 341, 91))
        self.pushButton.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 210, 921, 61))
        self.label.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 280, 921, 61))
        self.label_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 350, 921, 61))
        self.label_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 420, 921, 61))
        self.label_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1091, 751))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(70, 80, 901, 91))
        self.label_5.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(120, 240, 271, 71))
        self.radioButton.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(120, 450, 271, 71))
        self.radioButton_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_3.setGeometry(QtCore.QRect(120, 380, 271, 71))
        self.radioButton_3.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_4.setGeometry(QtCore.QRect(120, 310, 271, 71))
        self.radioButton_4.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.radioButton_4.setObjectName("radioButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 540, 401, 101))
        self.pushButton_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1091, 751))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(110, 170, 351, 111))
        self.label_6.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(440, 170, 551, 101))
        self.lineEdit.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 1101, 751))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(380, 80, 341, 81))
        self.label_7.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(120, 200, 341, 91))
        self.label_8.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(120, 310, 341, 91))
        self.label_9.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(470, 210, 431, 81))
        self.lineEdit_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(470, 320, 431, 81))
        self.lineEdit_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 530, 391, 81))
        self.pushButton_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 1081, 731))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_2.setGeometry(QtCore.QRect(110, 60, 451, 81))
        self.comboBox_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 320, 371, 71))
        self.pushButton_4.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setGeometry(QtCore.QRect(490, 200, 101, 61))
        self.label_10.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_5.setGeometry(QtCore.QRect(620, 70, 371, 71))
        self.pushButton_5.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 1081, 741))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_11 = QtWidgets.QLabel(self.frame_5)
        self.label_11.setGeometry(QtCore.QRect(60, 70, 471, 61))
        self.label_11.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_4.setGeometry(QtCore.QRect(60, 130, 941, 71))
        self.lineEdit_4.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_12 = QtWidgets.QLabel(self.frame_5)
        self.label_12.setGeometry(QtCore.QRect(60, 250, 471, 61))
        self.label_12.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_5)
        self.label_13.setGeometry(QtCore.QRect(60, 390, 471, 61))
        self.label_13.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_5)
        self.label_14.setGeometry(QtCore.QRect(60, 460, 471, 61))
        self.label_14.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_5)
        self.label_15.setGeometry(QtCore.QRect(60, 320, 471, 61))
        self.label_15.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_15.setObjectName("label_15")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_5.setGeometry(QtCore.QRect(270, 250, 501, 61))
        self.lineEdit_5.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_6.setGeometry(QtCore.QRect(270, 390, 501, 61))
        self.lineEdit_6.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_7.setGeometry(QtCore.QRect(270, 320, 501, 61))
        self.lineEdit_7.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_8.setGeometry(QtCore.QRect(270, 460, 501, 61))
        self.lineEdit_8.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_16 = QtWidgets.QLabel(self.frame_5)
        self.label_16.setGeometry(QtCore.QRect(60, 560, 471, 61))
        self.label_16.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_16.setObjectName("label_16")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_9.setGeometry(QtCore.QRect(270, 560, 501, 61))
        self.lineEdit_9.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_6.setGeometry(QtCore.QRect(640, 650, 381, 51))
        self.pushButton_6.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setGeometry(QtCore.QRect(0, 0, 1081, 741))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_17 = QtWidgets.QLabel(self.frame_6)
        self.label_17.setGeometry(QtCore.QRect(130, 150, 411, 81))
        self.label_17.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_17.setObjectName("label_17")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_10.setGeometry(QtCore.QRect(540, 150, 501, 71))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_7.setGeometry(QtCore.QRect(350, 340, 421, 61))
        self.pushButton_7.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setGeometry(QtCore.QRect(0, 0, 1091, 731))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_7)
        self.comboBox_3.setGeometry(QtCore.QRect(370, 120, 341, 61))
        self.comboBox_3.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_18 = QtWidgets.QLabel(self.frame_7)
        self.label_18.setGeometry(QtCore.QRect(130, 120, 171, 51))
        self.label_18.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame_7)
        self.label_19.setGeometry(QtCore.QRect(130, 340, 201, 51))
        self.label_19.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_19.setObjectName("label_19")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_7)
        self.comboBox_4.setGeometry(QtCore.QRect(360, 330, 351, 61))
        self.comboBox_4.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_8.setGeometry(QtCore.QRect(780, 120, 191, 61))
        self.pushButton_8.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_9.setGeometry(QtCore.QRect(790, 330, 191, 61))
        self.pushButton_9.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_9.setObjectName("pushButton_9")
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        self.frame_8.setGeometry(QtCore.QRect(0, 0, 1091, 751))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_11.setGeometry(QtCore.QRect(480, 160, 411, 61))
        self.lineEdit_11.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_12.setGeometry(QtCore.QRect(480, 250, 411, 61))
        self.lineEdit_12.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_13.setGeometry(QtCore.QRect(480, 340, 411, 61))
        self.lineEdit_13.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_14.setGeometry(QtCore.QRect(480, 430, 411, 61))
        self.lineEdit_14.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_20 = QtWidgets.QLabel(self.frame_8)
        self.label_20.setGeometry(QtCore.QRect(100, 160, 320, 61))
        self.label_20.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame_8)
        self.label_21.setGeometry(QtCore.QRect(100, 250, 321, 61))
        self.label_21.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame_8)
        self.label_22.setGeometry(QtCore.QRect(100, 340, 321, 61))
        self.label_22.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.frame_8)
        self.label_23.setGeometry(QtCore.QRect(100, 430, 321, 61))
        self.label_23.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_23.setObjectName("label_23")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_10.setGeometry(QtCore.QRect(350, 570, 371, 81))
        self.pushButton_10.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_24 = QtWidgets.QLabel(self.frame_8)
        self.label_24.setGeometry(QtCore.QRect(360, 40, 411, 71))
        self.label_24.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_24.setObjectName("label_24")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1087, 31))
        self.menubar.setObjectName("menubar")
        self.menuCategory = QtWidgets.QMenu(self.menubar)
        self.menuCategory.setObjectName("menuCategory")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuLogin = QtWidgets.QMenu(self.menubar)
        self.menuLogin.setObjectName("menuLogin")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPython = QtWidgets.QAction(MainWindow)
        self.actionPython.setObjectName("actionPython")
        self.actionJava = QtWidgets.QAction(MainWindow)
        self.actionJava.setObjectName("actionJava")
        self.actionGeneral_Knowledge = QtWidgets.QAction(MainWindow)
        self.actionGeneral_Knowledge.setObjectName("actionGeneral_Knowledge")
        self.actionC = QtWidgets.QAction(MainWindow)
        self.actionC.setObjectName("actionC")
        self.actionHome = QtWidgets.QAction(MainWindow)
        self.actionHome.setObjectName("actionHome")
        self.actionRegister = QtWidgets.QAction(MainWindow)
        self.actionRegister.setObjectName("actionRegister")
        self.actionLogin = QtWidgets.QAction(MainWindow)
        self.actionLogin.setObjectName("actionLogin")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionTeacher = QtWidgets.QAction(MainWindow)
        self.actionTeacher.setObjectName("actionTeacher")
        self.actionStudent = QtWidgets.QAction(MainWindow)
        self.actionStudent.setObjectName("actionStudent")
        self.actionRegister_2 = QtWidgets.QAction(MainWindow)
        self.actionRegister_2.setObjectName("actionRegister_2")
        self.menuCategory.addAction(self.actionPython)
        self.menuCategory.addAction(self.actionJava)
        self.menuCategory.addAction(self.actionGeneral_Knowledge)
        self.menuCategory.addAction(self.actionC)
        self.menuOptions.addAction(self.actionHome)
        self.menuOptions.addAction(self.actionRegister_2)
        self.menuOptions.addAction(self.actionExit)
        self.menuLogin.addAction(self.actionTeacher)
        self.menuLogin.addAction(self.actionStudent)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuLogin.menuAction())
        self.menubar.addAction(self.menuCategory.menuAction())

        self.frame_8.hide()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Select Subject"))
        self.comboBox.setItemText(1, _translate("MainWindow", "C++"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Python"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Java"))
        self.comboBox.setItemText(4, _translate("MainWindow", "GK"))
        self.pushButton.setText(_translate("MainWindow", "Start Test"))
        self.label.setText(_translate("MainWindow", "1. Test will be of 30 minutes"))
        self.label_2.setText(_translate("MainWindow", "1. Test will be of 30 minutes"))
        self.label_3.setText(_translate("MainWindow", "1. Test will be of 30 minutes"))
        self.label_4.setText(_translate("MainWindow", "1. Test will be of 30 minutes"))
        self.label_5.setText(_translate("MainWindow", "Question : Who is the prime minister of India ?"))
        self.radioButton.setText(_translate("MainWindow", "option_1"))
        self.radioButton_2.setText(_translate("MainWindow", "option_1"))
        self.radioButton_3.setText(_translate("MainWindow", "option_1"))
        self.radioButton_4.setText(_translate("MainWindow", "option_1"))
        self.pushButton_2.setText(_translate("MainWindow", "Next Question"))
        self.label_6.setText(_translate("MainWindow", "Final Score"))
        self.label_7.setText(_translate("MainWindow", "Login"))
        self.label_8.setText(_translate("MainWindow", "User Name"))
        self.label_9.setText(_translate("MainWindow", "User Password"))
        self.pushButton_3.setText(_translate("MainWindow", "Login"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Choose Subject"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Python"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "C++"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Java"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "GK"))
        self.pushButton_4.setText(_translate("MainWindow", "Add New Subject"))
        self.label_10.setText(_translate("MainWindow", "OR"))
        self.pushButton_5.setText(_translate("MainWindow", "Create Test"))
        self.label_11.setText(_translate("MainWindow", "Enter Question"))
        self.label_12.setText(_translate("MainWindow", "Option 1"))
        self.label_13.setText(_translate("MainWindow", "Option 3"))
        self.label_14.setText(_translate("MainWindow", "Option 4"))
        self.label_15.setText(_translate("MainWindow", "Option 2"))
        self.label_16.setText(_translate("MainWindow", "Answer"))
        self.pushButton_6.setText(_translate("MainWindow", "Create Question"))
        self.label_17.setText(_translate("MainWindow", "Enter the name of Subject"))
        self.pushButton_7.setText(_translate("MainWindow", "Insert Subject"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Teacher"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Student"))
        self.label_18.setText(_translate("MainWindow", "Login As"))
        self.label_19.setText(_translate("MainWindow", "Register As"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Teacher"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Student"))
        self.pushButton_8.setText(_translate("MainWindow", "Login"))
        self.pushButton_9.setText(_translate("MainWindow", "Register"))
        self.label_20.setText(_translate("MainWindow", "Enter College ID"))
        self.label_21.setText(_translate("MainWindow", "Enter Your Name"))
        self.label_22.setText(_translate("MainWindow", "Enter Your Email"))
        self.label_23.setText(_translate("MainWindow", "Enter Your Password"))
        self.pushButton_10.setText(_translate("MainWindow", "Register"))
        self.label_24.setText(_translate("MainWindow", "Register As"))
        self.menuCategory.setTitle(_translate("MainWindow", "Teacher"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuLogin.setTitle(_translate("MainWindow", "Login"))
        self.actionPython.setText(_translate("MainWindow", "Create Test"))
        self.actionJava.setText(_translate("MainWindow", "View Test"))
        self.actionGeneral_Knowledge.setText(_translate("MainWindow", "General Knowledge"))
        self.actionC.setText(_translate("MainWindow", "C++"))
        self.actionHome.setText(_translate("MainWindow", "Home"))
        self.actionRegister.setText(_translate("MainWindow", "Register"))
        self.actionLogin.setText(_translate("MainWindow", "Login"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionTeacher.setText(_translate("MainWindow", "Teacher"))
        self.actionStudent.setText(_translate("MainWindow", "Student"))
        self.actionRegister_2.setText(_translate("MainWindow", "Register"))

        self.pushButton_8.clicked.connect(self.loginUser)
        self.pushButton_3.clicked.connect(self.login)

        self.pushButton_9.clicked.connect(self.registerUser)
        self.pushButton_10.clicked.connect(self.registration)

        self.actionHome.triggered.connect(self.showHome)

    def showHome(self):
        self.frame_8.hide()

    def loginUser(self):
        self.frame_4.hide()
        self.frame_3.show()
        self.user = self.comboBox_3.currentText()
        self.loginTable = ""
        # print(user)
        if self.user == "Teacher":
            self.label_7.setText("Login As Teacher")
            self.loginTable = "teachers"
        elif self.user == "Student":
            self.label_7.setText("Login As Student")
            self.loginTable = "students"


    def login(self):
        self.loginId = self.lineEdit_2.text()
        self.loginPassword = self.lineEdit_3.text()

        if self.loginTable == "teachers":
            query = "SELECT * FROM teachers WHERE teacherEmail = %s AND teacherPassword = %s"
            cursor.execute(query, (self.loginId, self.loginPassword))
            self.loginTeacher()
        elif self.loginTable == "students":
            query = "SELECT * FROM students WHERE studentEmail = %s AND studentPassword = %s"
            cursor.execute(query, (self.loginId, self.loginPassword))
            self.loginStudent()

    def loginTeacher(self):
        self.frame_5.hide()
        self.frame_4.show()

    def loginStudent(self):
        pass


    def registerUser(self):
        self.frame_8.show()
        self.user = self.comboBox_4.currentText()
        self.registerTable = ""
        # print(user)
        if self.user == "Teacher":
            self.label_24.setText("Register As Teacher")
            self.registerTable = "teachers"
        elif self.user == "Student":
            self.label_24.setText("Register As Student")
            self.registerTable = "students"

    def registration(self):
        self.userid = self.lineEdit_11.text()
        self.username = self.lineEdit_12.text()
        self.useremail = self.lineEdit_13.text()
        self.userpassword = self.lineEdit_14.text()

        query = "INSERT INTO "+ self.registerTable +" VALUES (%s, %s, %s, %s)"
        print(query)
        cursor.execute(query, (self.userid,
                               self.username,
                               self.useremail,
                               self.userpassword))
        print("Data Inserted Successfully")
        QMessageBox.about(self, "Success", "Registered Successfully")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

