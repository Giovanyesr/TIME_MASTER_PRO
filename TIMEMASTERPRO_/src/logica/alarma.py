import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import QTimer, QTime, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from src.interface.ui_alarma import AlarmUI
from src.logica.clase_alarma import Alarm

class AlarmApp(AlarmUI):
    def __init__(self):
        super().__init__()
        self.alarms = []

        self.alarm_timer = QTimer(self)
        self.alarm_timer.timeout.connect(self.check_alarm)
        self.alarm_timer.start(1000)

        self.btn_set_alarm.clicked.disconnect()
        self.btn_set_alarm.clicked.connect(self.set_alarm)

    def set_alarm(self):
        alarm_time = self.time_edit.time().toString('HH:mm:ss')
        if alarm_time not in self.alarms:
            self.add_alarm_to_list(alarm_time)
            self.alarms.append(alarm_time)
            QMessageBox.information(self, 'Configuración de Alarma', f'Alarma configurada para las {alarm_time}')

            new_alarm = Alarm(alarm_time=alarm_time)
            new_alarm.save_to_db()

        else:
            QMessageBox.warning(self, 'Configuración de Alarma', f'La alarma para {alarm_time} ya está configurada.')

    def check_alarm(self):
        current_time = QTime.currentTime().toString('HH:mm:ss')
        if current_time in self.alarms:
            self.play_alarm()

    def play_alarm(self):
        sound_file = "../recursos/beep.wav"
        url = QUrl.fromLocalFile(sound_file)
        content = QMediaContent(url)
        player = QMediaPlayer()
        player.setMedia(content)
        player.play()

        QMessageBox.warning(self, '¡Alarma!', '¡Es hora!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    alarm_app = AlarmApp()
    alarm_app.show()
    sys.exit(app.exec_())
