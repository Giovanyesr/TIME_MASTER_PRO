from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.timeLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeLabel.setGeometry(QtCore.QRect(50, 50, 300, 150))
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        self.timeLabel.setFont(font)
        self.timeLabel.setObjectName("timeLabel")

        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(50, 10, 300, 30))
        font.setPointSize(14)
        self.statusLabel.setFont(font)
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setObjectName("statusLabel")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(50, 210, 300, 30))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")

        self.lapsosLabel = QtWidgets.QLabel(self.centralwidget)
        self.lapsosLabel.setGeometry(QtCore.QRect(50, 250, 300, 50))
        self.lapsosLabel.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lapsosLabel.setFont(font)
        self.lapsosLabel.setObjectName("lapsosLabel")

        button_width = 100
        button_height = 40
        button_margin = 20
        button_x = 90

        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(button_x, 320 + button_margin, button_width, button_height))
        self.startButton.setObjectName("startButton")
        self.startButton.setStyleSheet("background-color: #4CAF50; color: white;")

        self.pauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.pauseButton.setGeometry(QtCore.QRect(button_x + 110, 320 + button_margin, button_width, button_height))
        self.pauseButton.setObjectName("pauseButton")
        self.pauseButton.setStyleSheet("background-color: #f44336; color: white;")

        self.resumeButton = QtWidgets.QPushButton(self.centralwidget)
        self.resumeButton.setGeometry(QtCore.QRect(button_x, 380 + button_margin, button_width, button_height))
        self.resumeButton.setObjectName("resumeButton")
        self.resumeButton.setStyleSheet("background-color: #2196F3; color: white;")

        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(button_x + 110, 380 + button_margin, button_width, button_height))
        self.resetButton.setObjectName("resetButton")
        self.resetButton.setStyleSheet("background-color: #607D8B; color: white;")

        spinbox_width = 100
        spinbox_height = 30

        self.totalTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.totalTimeLabel.setGeometry(QtCore.QRect(50, 500, 200, 30))
        self.totalTimeLabel.setObjectName("totalTimeLabel")

        self.totalTimeSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.totalTimeSpinBox.setGeometry(QtCore.QRect(250, 500, spinbox_width, spinbox_height))
        self.totalTimeSpinBox.setMaximum(3600)
        self.totalTimeSpinBox.setObjectName("totalTimeSpinBox")

        self.workTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.workTimeLabel.setGeometry(QtCore.QRect(50, 540, 200, 30))
        self.workTimeLabel.setObjectName("workTimeLabel")

        self.workTimeSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.workTimeSpinBox.setGeometry(QtCore.QRect(250, 540, spinbox_width, spinbox_height))
        self.workTimeSpinBox.setMaximum(3600)
        self.workTimeSpinBox.setObjectName("workTimeSpinBox")

        self.breakTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.breakTimeLabel.setGeometry(QtCore.QRect(50, 580, 200, 30))
        self.breakTimeLabel.setObjectName("breakTimeLabel")

        self.breakTimeSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.breakTimeSpinBox.setGeometry(QtCore.QRect(250, 580, spinbox_width, spinbox_height))
        self.breakTimeSpinBox.setMaximum(3600)
        self.breakTimeSpinBox.setObjectName("breakTimeSpinBox")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Temporizador Pomodoro"))
        self.timeLabel.setText(_translate("MainWindow", "00:00"))
        self.startButton.setText(_translate("MainWindow", "Empezar"))
        self.pauseButton.setText(_translate("MainWindow", "Pausar"))
        self.resumeButton.setText(_translate("MainWindow", "Reanudar"))
        self.resetButton.setText(_translate("MainWindow", "Reiniciar"))
        self.lapsosLabel.setText(_translate("MainWindow", "Completado: 0 ciclos"))
        self.totalTimeLabel.setText(_translate("MainWindow", "Tiempo Total (segundos):"))
        self.workTimeLabel.setText(_translate("MainWindow", "Tiempo de Trabajo (segundos):"))
        self.breakTimeLabel.setText(_translate("MainWindow", "Tiempo de Descanso (segundos):"))
        self.statusLabel.setText(_translate("MainWindow", "Trabajando"))
