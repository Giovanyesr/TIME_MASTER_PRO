# main.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from src.logica.temporizador_estandar import TemporizadorEstandarApp
from src.logica.temporizador_pomodoro import PomodoroTimer
from src.logica.historial import HistorialWindow
from src.logica.alarma import AlarmApp
from src.interface.ui_main import Ui_MainWindow


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnTemporizadorEstandar.clicked.connect(self.open_temporizador_estandar)
        self.ui.btnPomodoro.clicked.connect(self.open_temporizador_pomodoro)
        self.ui.btnHistorialAlarmas.clicked.connect(self.open_historial_alarmas)
        self.ui.btnAlarma.clicked.connect(self.open_alarma)

    def open_temporizador_estandar(self):
        self.temporizador_estandar = TemporizadorEstandarApp()
        self.temporizador_estandar.show()

    def open_temporizador_pomodoro(self):
        self.pomodoro_timer = PomodoroTimer()
        self.pomodoro_timer.show()

    def open_historial_alarmas(self):
        self.historial_alarmas = HistorialWindow()
        self.historial_alarmas.show()

    def open_alarma(self):
        self.alarma_app = AlarmApp()
        self.alarma_app.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainApp()
    mainWindow.show()
    sys.exit(app.exec_())
