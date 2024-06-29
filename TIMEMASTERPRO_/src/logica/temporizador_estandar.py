import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtMultimedia import QSound
from src.interface.ui_temporizador_estandar import Ui_MainWindow
from src.logica.clase_temporizador_estandar import TemporizadorEstandar
import sqlite3

class TemporizadorEstandarApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        self.is_running = False
        self.time_left = QTime(0, 0)

        self.ui.startButton.clicked.connect(self.start_timer)
        self.ui.pauseButton.clicked.connect(self.pause_timer)
        self.ui.resumeButton.clicked.connect(self.resume_timer)
        self.ui.resetButton.clicked.connect(self.reset_timer)

        self.update_ui()

    def update_ui(self):
        self.ui.timeLabel.setText(self.time_left.toString("mm:ss"))

    def start_timer(self):
        total_seconds = self.ui.totalTimeSpinBox.value()
        self.time_left = QTime(0, 0).addSecs(total_seconds)
        self.timer.start(1000)
        self.is_running = True
        self.update_ui()

        try:
            # Crear una instancia de TemporizadorEstandar y guardarla en la bd
            new_temporizador = TemporizadorEstandar(duration=total_seconds)
            new_temporizador.save_to_db()
        except sqlite3.Error as e:
            self.show_error_message("Error de Base de Datos", f"No se pudo guardar el temporizador en la bd:\n{str(e)}")

    def pause_timer(self):
        if self.is_running:
            self.timer.stop()
            self.is_running = False
            self.update_ui()

    def resume_timer(self):
        if not self.is_running:
            self.timer.start(1000)
            self.is_running = True
            self.update_ui()

    def reset_timer(self):
        self.timer.stop()
        self.is_running = False
        self.time_left = QTime(0, 0)
        self.update_ui()

    def update_timer(self):
        if self.time_left > QTime(0, 0):
            self.time_left = self.time_left.addSecs(-1)
            self.update_ui()
        else:
            self.timer.stop()
            self.is_running = False
            self.play_sound()

    def play_sound(self):
        sound_file = "../recursos/beep.wav"
        QSound.play(sound_file)

    def show_error_message(self, title, message):
        QMessageBox.critical(self, title, message, QMessageBox.Ok)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    temporizador_app = TemporizadorEstandarApp()
    temporizador_app.show()
    sys.exit(app.exec_())
