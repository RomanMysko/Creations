# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!

# noinspection PyUnresolvedReferences
from PyQt5 import QtCore, QtGui, QtWidgets
# noinspection PyUnresolvedReferences
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Solve_button = QtWidgets.QPushButton(self.centralwidget)
        self.Solve_button.setGeometry(QtCore.QRect(30, 140, 81, 31))
        self.Solve_button.setObjectName("Solve_button")
        self.Solve_button.clicked.connect(self.b1_clicked)
        self.Erase_button = QtWidgets.QPushButton(self.centralwidget)
        self.Erase_button.setGeometry(QtCore.QRect(110, 140, 91, 31))
        self.Erase_button.setObjectName("Erase_button")
        self.Erase_button.clicked.connect(self.b2_clicked)
        self.Exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.Exit_button.setGeometry(QtCore.QRect(200, 140, 101, 31))
        self.Exit_button.setObjectName("Exit_button")
        self.Exit_button.clicked.connect(self.b3_clicked)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 141, 31))
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.currentTextChanged.connect(self.combbox_value_change)
        self.radioButton_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_1.setGeometry(QtCore.QRect(180, 10, 82, 17))
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(180, 40, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.Start_label = QtWidgets.QLabel(self.centralwidget)
        self.Start_label.setGeometry(QtCore.QRect(10, 60, 121, 16))
        self.Start_label.setObjectName("Start_label")
        self.Result_label = QtWidgets.QLabel(self.centralwidget)
        self.Result_label.setGeometry(QtCore.QRect(70, 100, 47, 13))
        self.Result_label.setObjectName("Result_label")
        self.Result = QtWidgets.QLineEdit(self.centralwidget)
        self.Result.setGeometry(QtCore.QRect(130, 90, 71, 31))
        self.Result.setObjectName("Result")
        self.Start = QtWidgets.QLineEdit(self.centralwidget)
        self.Start.setGeometry(QtCore.QRect(130, 60, 71, 20))
        self.Start.setObjectName("Start")
        self.End = QtWidgets.QLineEdit(self.centralwidget)
        self.End.setGeometry(QtCore.QRect(240, 60, 61, 20))
        self.End.setObjectName("End")
        self.End_label = QtWidgets.QLabel(self.centralwidget)
        self.End_label.setGeometry(QtCore.QRect(220, 60, 21, 16))
        self.End_label.setObjectName("End_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Solve_button.setText(_translate("MainWindow", "Solve"))
        self.Erase_button.setText(_translate("MainWindow", "Erase"))
        self.Exit_button.setText(_translate("MainWindow", "Exit"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Half division method"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Newton\'s method"))
        self.radioButton_1.setText(_translate("MainWindow", "X*X-4"))
        self.radioButton_2.setText(_translate("MainWindow", "3x^3-6x"))
        self.Start_label.setText(_translate("MainWindow", "Input the starting point"))
        self.Result_label.setText(_translate("MainWindow", "Result  X="))
        self.End_label.setText(_translate("MainWindow", "B ="))

    def combbox_value_change(self):
        _translate = QtCore.QCoreApplication.translate
        if self.comboBox.currentIndex() == 0:
            self.End_label.setVisible(True)
            self.End.setVisible(True)
        elif self.comboBox.currentIndex() == 1:
            self.End_label.setVisible(False)
            self.End.setVisible(False)
        else:
            pass

    @staticmethod
    def pop_up(string):
        msgBox = QMessageBox()
        msgBox.setStyleSheet("QLabel{min-width: 180px;}")
        msgBox.setWindowTitle("Some message")
        msgBox.setText(string)
        msgBox.exec_()

    @property
    def radio_check(self):
        if self.radioButton_1.isChecked():
            return 1
        elif self.radioButton_2.isChecked():
            return 2
        else:
            self.pop_up("Choose an equation")

    def Newton(self, x, eps):
        max_iter = 100
        for i in range(1, max_iter):
            x -= self.f1(x) / self.fp1(x, eps)
            if abs(self.f1(x) / self.fp1(x, eps) <= eps):
                self.Result.setText(str(round(x, 5)))
                break
            if i == 100:
                self.pop_up("Max iteration has been reached")
                return

    def MPD(self, a, b, eps, c):
        if self.f1(a) * self.f1(b) == 0:
            if self.f1(a) == 0:
                self.Result.setText(str(a))
                self.pop_up("A point is our root")
                return
            elif self.f1(b) == 0:
                self.Result.setText(str(b))
                self.pop_up("B point is our root")
                return
        if self.f1(a) * self.f1(b) > 0:
            self.pop_up("No result in this interval")
            return
        elif self.f1(a) * self.f1(b) < 0:
            while abs(b - a) > eps:
                c = (a + b) / 2
                if self.f1(c) == 0:
                    self.Result.setText(str(c))
                    break
                if self.f1(a) * self.f1(c) < 0:
                    b = c
                elif self.f1(b) * self.f1(c) < 0:
                    a = c
                else:
                    self.pop_up("something went wrong during while loop")
                    return
        self.Result.setText(str(round(c, 5)))

    def f1(self, x):
        if self.radio_check == 1:
            return x * x - 4
        elif self.radio_check == 2:
            return 3*x**3 - 6*x

    def fp1(self, x, h):
        return (self.f1(x + h) - self.f1(x)) / h

    def b1_clicked(self):
        eps = 0.0001
        c = ""
        if self.comboBox.currentIndex() == 0:
            a = float(self.Start.text())
            b = float(self.End.text())
            self.MPD(a, b, eps, c)
        elif self.comboBox.currentIndex() == 1:
            x = float(self.Start.text())
            self.Newton(x, eps)
        else:
            self.pop_up("Choose a method pls")

    def b2_clicked(self):
        self.End_label.setVisible(True)
        self.End.setVisible(True)
        self.Result.setText("")
        self.Start.setText("")
        self.End.setText("")
        self.comboBox.setCurrentIndex(-1)
        self.radioButton_1.setAutoExclusive(False)
        self.radioButton_1.setChecked(False)
        self.radioButton_1.setAutoExclusive(True)
        self.radioButton_2.setAutoExclusive(False)
        self.radioButton_2.setChecked(False)
        self.radioButton_2.setAutoExclusive(True)

    @staticmethod
    def b3_clicked():
        sys.exit(0)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
