from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 400)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.timeLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeLabel.setGeometry(QtCore.QRect(50, 50, 400, 150))  # Aumenté el tamaño del label para mayor visibilidad
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(80)  # Ajusté el tamaño de la fuente para que sea más grande
        font.setBold(True)
        self.timeLabel.setFont(font)
        self.timeLabel.setObjectName("timeLabel")

        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(50, 10, 400, 30))  # Aumenté el tamaño del label para mayor visibilidad
        font.setPointSize(16)  # Ajusté el tamaño de la fuente para que sea más grande
        self.statusLabel.setFont(font)
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setObjectName("statusLabel")

        self.startButton = QtWidgets.QPushButton("Empezar", self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(50, 250, 100, 30))  # Ajusté el tamaño y la posición del botón

        self.pauseButton = QtWidgets.QPushButton("Pausar", self.centralwidget)
        self.pauseButton.setGeometry(QtCore.QRect(170, 250, 100, 30))  # Ajusté el tamaño y la posición del botón

        self.resumeButton = QtWidgets.QPushButton("Reanudar", self.centralwidget)
        self.resumeButton.setGeometry(QtCore.QRect(290, 250, 100, 30))  # Ajusté el tamaño y la posición del botón

        self.resetButton = QtWidgets.QPushButton("Reiniciar", self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(410, 250, 100, 30))  # Ajusté el tamaño y la posición del botón

        self.totalTimeSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.totalTimeSpinBox.setGeometry(QtCore.QRect(50, 300, 100, 30))  # Ajusté el tamaño y la posición del spinbox
        self.totalTimeSpinBox.setMaximum(3600)

        self.totalTimeLabel = QtWidgets.QLabel("Tiempo Total (segundos):", self.centralwidget)
        self.totalTimeLabel.setGeometry(QtCore.QRect(170, 300, 200, 30))  # Ajusté el tamaño y la posición del label

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
