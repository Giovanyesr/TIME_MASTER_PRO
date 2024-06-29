from PyQt5.QtWidgets import QWidget, QLabel, QTimeEdit, QPushButton, QVBoxLayout, QListWidget
from PyQt5.QtCore import Qt, QTimer, QDateTime, QTime
from PyQt5.QtGui import QFont

class AlarmUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Alarm App')
        self.setGeometry(200, 200, 600, 400)
        self.setup_ui()

    def setup_ui(self):
        self.lbl_current_time = QLabel(self)
        self.lbl_current_time.setAlignment(Qt.AlignCenter)
        self.lbl_current_time.setFont(QFont('Arial', 20))
        self.update_current_time()

        self.time_edit = QTimeEdit(self)
        self.time_edit.setFont(QFont('Arial', 16))
        self.time_edit.setAlignment(Qt.AlignCenter)
        self.time_edit.setDisplayFormat('HH:mm:ss')
        self.time_edit.setMinimumTime(QTime(0, 0, 0))
        self.time_edit.setMaximumTime(QTime(23, 59, 59))

        self.btn_set_alarm = QPushButton('Configurar Alarma', self)
        self.btn_set_alarm.setFont(QFont('Arial', 16))
        self.btn_set_alarm.clicked.connect(self.set_alarm)

        self.list_alarms = QListWidget(self)
        self.list_alarms.setFont(QFont('Arial', 12))
        self.list_alarms.setSelectionMode(QListWidget.SingleSelection)
        self.list_alarms.itemClicked.connect(self.select_alarm)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_current_time)
        self.timer.start(1000)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.lbl_current_time)
        v_layout.addWidget(self.time_edit)
        v_layout.addWidget(self.btn_set_alarm)
        v_layout.addWidget(self.list_alarms)

        self.setLayout(v_layout)

    def update_current_time(self):
        current_time = QTime.currentTime().toString('hh:mm:ss')
        self.lbl_current_time.setText(f'Hora actual: {current_time}')

    def set_alarm(self):
        alarm_time = self.time_edit.time().toString('HH:mm:ss')
        self.add_alarm_to_list(alarm_time)

    def add_alarm_to_list(self, alarm_time_str):
        current_datetime = QDateTime.currentDateTime().toString(Qt.DefaultLocaleLongDate)
        alarm_str = f'{alarm_time_str} - Creada el {current_datetime}'
        self.list_alarms.addItem(alarm_str)

    def select_alarm(self, item):
        pass
