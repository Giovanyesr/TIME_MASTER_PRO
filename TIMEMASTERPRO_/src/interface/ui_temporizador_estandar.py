from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 400)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.timeLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeLabel.setGeometry(QtCore.QRect(50, 50, 400, 150))
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(80)
        font.setBold(True)
        self.timeLabel.setFont(font)
        self.timeLabel.setObjectName("timeLabel")

        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(50, 10, 400, 30))
        font.setPointSize(16)
        self.statusLabel.setFont(font)
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setObjectName("statusLabel")

        self.startButton = QtWidgets.QPushButton("Empezar", self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(50, 250, 100, 30))
        self.startButton.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; }")

        self.pauseButton = QtWidgets.QPushButton("Pausar", self.centralwidget)
        self.pauseButton.setGeometry(QtCore.QRect(170, 250, 100, 30))
        self.pauseButton.setStyleSheet("QPushButton { background-color: #f44336; color: white; }")

        self.resumeButton = QtWidgets.QPushButton("Reanudar", self.centralwidget)
        self.resumeButton.setGeometry(QtCore.QRect(290, 250, 100, 30))
        self.resumeButton.setStyleSheet("QPushButton { background-color: #2196F3; color: white; }")

        self.resetButton = QtWidgets.QPushButton("Reiniciar", self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(410, 250, 100, 30))
        self.resetButton.setStyleSheet("QPushButton { background-color: #607D8B; color: white; }")

        self.totalTimeSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.totalTimeSpinBox.setGeometry(QtCore.QRect(50, 300, 100, 30))
        self.totalTimeSpinBox.setMaximum(3600)

        self.totalTimeLabel = QtWidgets.QLabel("Tiempo Total (segundos):", self.centralwidget)
        self.totalTimeLabel.setGeometry(QtCore.QRect(170, 300, 200, 30))

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Temporizador Estándar"))
        self.timeLabel.setText(_translate("MainWindow", "00:00"))
        self.statusLabel.setText(_translate("MainWindow", "Estado"))
        self.startButton.setText(_translate("MainWindow", "Empezar"))
        self.pauseButton.setText(_translate("MainWindow", "Pausar"))
        self.resumeButton.setText(_translate("MainWindow", "Reanudar"))
        self.resetButton.setText(_translate("MainWindow", "Reiniciar"))
        self.totalTimeLabel.setText(_translate("MainWindow", "Tiempo Total (segundos):"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Estilo adicional para la ventana principal (opcional)
    MainWindow.setStyleSheet("background-color: #FFFFFF;")  # Cambia el color de fondo de la ventana principal

    MainWindow.show()
    sys.exit(app.exec_())
