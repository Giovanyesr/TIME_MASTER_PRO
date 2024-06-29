# ui_main.py
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QSlider
from PyQt5.QtGui import QIcon, QPixmap

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.layout = QVBoxLayout(self.centralwidget)

        # Ruta absoluta a las imágenes
        ruta_imagenes = "C:/Users/ADMIN/Desktop/Final_Construdeidad/ExamenFinalTemporizadores/src/recursos/"

        # Botones con imágenes desde la carpeta src-recursos
        self.btnImgTemporizadorEstandar = QPushButton(self.centralwidget)
        self.set_button_image(self.btnImgTemporizadorEstandar, ruta_imagenes + "temporizador.jpg", 128)

        self.btnImgPomodoro = QPushButton(self.centralwidget)
        self.set_button_image(self.btnImgPomodoro, ruta_imagenes + "pomodoro.jpg", 128)

        self.btnImgAlarma = QPushButton(self.centralwidget)
        self.set_button_image(self.btnImgAlarma, ruta_imagenes + "alarma.jpg", 128)

        self.btnImgHistorialAlarmas = QPushButton(self.centralwidget)
        self.set_button_image(self.btnImgHistorialAlarmas, ruta_imagenes + "historial.jpg", 128)

        # Botones de texto
        self.btnTemporizadorEstandar = QPushButton("Temporizador Estándar", self.centralwidget)
        self.btnPomodoro = QPushButton("Temporizador Pomodoro", self.centralwidget)
        self.btnAlarma = QPushButton("Alarma", self.centralwidget)
        self.btnHistorialAlarmas = QPushButton("Historial de Alarmas", self.centralwidget)

        # Añadir botones con imágenes y botones de texto al layout
        self.layout.addWidget(self.btnImgTemporizadorEstandar)
        self.layout.addWidget(self.btnTemporizadorEstandar)
        self.layout.addWidget(self.btnImgPomodoro)
        self.layout.addWidget(self.btnPomodoro)
        self.layout.addWidget(self.btnImgAlarma)
        self.layout.addWidget(self.btnAlarma)
        self.layout.addWidget(self.btnImgHistorialAlarmas)
        self.layout.addWidget(self.btnHistorialAlarmas)

        # Botón deslizante para modo oscuro
        self.darkModeSlider = QSlider(QtCore.Qt.Horizontal, self.centralwidget)
        self.darkModeSlider.setMinimum(0)
        self.darkModeSlider.setMaximum(1)
        self.darkModeSlider.setValue(0)  # Valor inicial, 0 para modo claro
        self.darkModeSlider.setTickInterval(1)
        self.darkModeSlider.setTickPosition(QSlider.TicksBelow)
        self.layout.addWidget(self.darkModeSlider, alignment=QtCore.Qt.AlignRight)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Aplicar estilos iniciales
        self.apply_style()

        # Conectar evento de cambio del slider
        self.darkModeSlider.valueChanged.connect(self.apply_style)

    def set_button_image(self, button, image_path, size):
        pixmap = QPixmap(image_path).scaledToWidth(size, mode=QtCore.Qt.SmoothTransformation)
        icon = QIcon(pixmap)
        button.setIcon(icon)
        button.setIconSize(QtCore.QSize(size, size))
        button.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        button.setStyleSheet("QPushButton { border: none; }")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menú Principal"))

    def apply_style(self):
        dark_mode = self.darkModeSlider.value() == 1

        # Estilos para modo claro
        if not dark_mode:
            self.centralwidget.setStyleSheet("")
            self.btnTemporizadorEstandar.setStyleSheet("")
            self.btnPomodoro.setStyleSheet("")
            self.btnAlarma.setStyleSheet("")
            self.btnHistorialAlarmas.setStyleSheet("")
            return

        # Estilos para modo oscuro
        self.centralwidget.setStyleSheet("background-color: black; color: white;")
        self.btnTemporizadorEstandar.setStyleSheet("color: white;")
        self.btnPomodoro.setStyleSheet("color: white;")
        self.btnAlarma.setStyleSheet("color: white;")
        self.btnHistorialAlarmas.setStyleSheet("color: white;")

