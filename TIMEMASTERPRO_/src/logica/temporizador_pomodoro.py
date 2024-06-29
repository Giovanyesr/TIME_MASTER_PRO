import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtMultimedia import QSound
from src.interface.ui_temporizador_pomodoro import Ui_MainWindow
from datetime import datetime
from src.logica.clase_temporizador_pomodoro import Pomodoro

class PomodoroTimer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        self.is_working = True
        self.is_running = False
        self.is_paused = False
        self.cycles = 0
        self.time_left = QTime(0, 0)
        self.total_cycles = 0

        self.ui.startButton.clicked.connect(self.start_timer)
        self.ui.pauseButton.clicked.connect(self.pause_timer)
        self.ui.resumeButton.clicked.connect(self.resume_timer)
        self.ui.resetButton.clicked.connect(self.reset_timer)

        self.update_ui()

    def update_ui(self):
        self.ui.lapsosLabel.setText(f"Ciclos completados: {self.cycles}")
        self.ui.timeLabel.setText(self.time_left.toString("mm:ss"))

        if not self.is_running or not self.is_working:
            self.ui.statusLabel.setText("Descansando")
        else:
            self.ui.statusLabel.setText("Trabajando")

        self.update_background_color()

    def start_timer(self):
        total_seconds = self.ui.totalTimeSpinBox.value()
        work_seconds = self.ui.workTimeSpinBox.value()
        break_seconds = self.ui.breakTimeSpinBox.value()

        if total_seconds % work_seconds != 0:
            QMessageBox.critical(self, "Error", "Error, ingrese datos válidos.")
            return

        self.total_time = QTime(0, 0).addSecs(total_seconds)
        self.work_time = QTime(0, 0).addSecs(work_seconds)
        self.break_time = QTime(0, 0).addSecs(break_seconds)

        self.time_left = self.work_time if self.is_working else self.break_time
        self.total_cycles = total_seconds // work_seconds

        self.is_running = True
        self.is_paused = False
        self.timer.start(1000)
        self.update_ui()

    def pause_timer(self):
        if self.is_running and not self.is_paused:
            self.timer.stop()
            self.is_running = False
            self.is_paused = True
            self.ui.centralwidget.setStyleSheet("background-color: red;")
            self.ui.statusLabel.setText("En pausa")
            self.update_ui()

    def resume_timer(self):
        if self.is_paused:
            self.timer.start(1000)
            self.is_running = True
            self.is_paused = False
            self.ui.centralwidget.setStyleSheet("background-color: orange;")
            self.ui.statusLabel.setText("Trabajando")
            self.update_ui()

    def reset_timer(self):
        self.timer.stop()
        self.is_running = False
        self.is_paused = False
        self.cycles = 0
        self.is_working = True
        self.time_left = QTime(0, 0)
        self.total_cycles = 0

        self.ui.totalTimeSpinBox.setValue(0)
        self.ui.workTimeSpinBox.setValue(0)
        self.ui.breakTimeSpinBox.setValue(0)

        self.ui.timeLabel.setText("")
        self.ui.progressBar.setValue(0)

        self.update_ui()

    def update_timer(self):
        if not self.is_running:
            return

        self.time_left = self.time_left.addSecs(-1)
        if self.time_left == QTime(0, 0):
            self.timer.stop()
            self.is_running = False
            self.is_working = not self.is_working
            if not self.is_working:
                self.cycles += 1
                self.update_ui()

                if self.cycles >= self.total_cycles:
                    self.show_final_message()
                    self.save_to_db()
                    self.reset_timer()
                    return

                self.time_left = self.break_time
            else:
                self.time_left = self.work_time

            self.timer.start(1000)
            self.is_running = True

        self.ui.timeLabel.setText(self.time_left.toString("mm:ss"))
        self.update_progress_bar()
        self.update_background_color()

    def update_progress_bar(self):
        total_seconds = self.work_time.minute() * 60 + self.work_time.second() if self.is_working else self.break_time.minute() * 60 + self.break_time.second()
        elapsed_seconds = total_seconds - (self.time_left.minute() * 60 + self.time_left.second())
        self.ui.progressBar.setValue(int((elapsed_seconds / total_seconds) * 100))

    def update_background_color(self):
        if self.is_paused:
            self.ui.centralwidget.setStyleSheet("background-color: red;")
            self.ui.statusLabel.setText("En pausa")
        elif not self.is_running:
            self.ui.centralwidget.setStyleSheet("background-color: white;")
            self.ui.statusLabel.setText("Inicio")
        elif self.is_working:
            self.ui.centralwidget.setStyleSheet("background-color: orange;")
            self.ui.statusLabel.setText("Trabajando")
        else:
            self.ui.centralwidget.setStyleSheet("background-color: green;")
            self.ui.statusLabel.setText("Descansando")

    def show_final_message(self):
        self.play_sound()
        QMessageBox.information(self, "Información", "Pomodoro Finalizado")

    def play_sound(self):
        sound_file = "../recursos/beep.wav"
        QSound.play(sound_file)

    def save_to_db(self):
        pomodoro = Pomodoro(work_duration=self.ui.workTimeSpinBox.value(),
                            break_duration=self.ui.breakTimeSpinBox.value(),
                            cycles=self.cycles,
                            started_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        pomodoro.save_to_db()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = PomodoroTimer()
    mainWindow.show()
    sys.exit(app.exec_())
