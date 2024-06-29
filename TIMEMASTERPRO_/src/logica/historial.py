import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QStackedWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sqlite3

class HistorialWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Historial de Temporizadores')
        self.setGeometry(100, 100, 600, 400)

        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
            }
            QLabel#label_titulo {
                font-size: 18px;
                font-weight: bold;
                color: #333;
                padding-bottom: 10px;
                align-self: center;
            }
            QComboBox {
                font-size: 14px;
                padding: 8px;
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            QStackedWidget {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 4px;
                margin-top: 10px;
                padding: 10px;
            }
            QLabel {
                font-size: 12px;
                margin-bottom: 10px;
                color: #666;
            }
            QLabel#label_alarmas {
                color: #3c8dbc; /* Azul */
            }
            QLabel#label_temporizadores_estandar {
                color: #f39c12; /* Naranja */
            }
            QLabel#label_temporizadores_pomodoro {
                color: #00a65a; /* Verde */
            }
            QLabel h2 {
                font-size: 14px;
                margin-bottom: 5px;
                color: #333;
            }
            QLabel ul {
                margin-left: 20px;
                padding-left: 0;
            }
            QLabel li {
                list-style-type: none;
                margin-bottom: 5px;
            }
        """)

        self.layout = QVBoxLayout(self)

        self.label_titulo = QLabel('Historial')
        self.label_titulo.setObjectName('label_titulo')
        self.layout.addWidget(self.label_titulo, alignment=Qt.AlignTop | Qt.AlignHCenter)

        self.combo_box = QComboBox()
        self.combo_box.addItem('Alarmas')
        self.combo_box.addItem('Temporizadores Estándar')
        self.combo_box.addItem('Temporizadores Pomodoro')
        self.combo_box.currentIndexChanged.connect(self.mostrar_seleccion)

        self.layout.addWidget(self.combo_box, alignment=Qt.AlignTop | Qt.AlignHCenter)

        self.stacked_widget = QStackedWidget()
        self.layout.addWidget(self.stacked_widget)

        self.label_alarmas = QLabel()
        self.label_alarmas.setObjectName('label_alarmas')
        self.stacked_widget.addWidget(self.label_alarmas)

        self.label_temporizadores_estandar = QLabel()
        self.label_temporizadores_estandar.setObjectName('label_temporizadores_estandar')
        self.stacked_widget.addWidget(self.label_temporizadores_estandar)

        self.label_temporizadores_pomodoro = QLabel()
        self.label_temporizadores_pomodoro.setObjectName('label_temporizadores_pomodoro')
        self.stacked_widget.addWidget(self.label_temporizadores_pomodoro)

        self.mostrar_datos()

    def mostrar_datos(self):
        self.mostrar_alarmas()
        self.mostrar_temporizadores_estandar()
        self.mostrar_temporizadores_pomodoro()

    def mostrar_seleccion(self, index):
        self.stacked_widget.setCurrentIndex(index)

    def mostrar_alarmas(self):
        conn = sqlite3.connect('examen_final_temporizadores.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM alarms')
        alarmas = cursor.fetchall()

        conn.close()

        texto = "<h2>Historial de Alarmas:</h2>"
        if alarmas:
            texto += "<ul>"
            for alarma in alarmas:
                texto += f"<li>ID: {alarma[0]}, Hora de Alarma: {alarma[1]}, Creado en: {alarma[2]}</li>"
            texto += "</ul>"
        else:
            texto += "<p>No hay alarmas registradas.</p>"

        self.label_alarmas.setText(texto)

    def mostrar_temporizadores_estandar(self):
        conn = sqlite3.connect('examen_final_temporizadores.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM temporizadores_estandar')
        temporizadores = cursor.fetchall()

        conn.close()

        texto = "<h2>Historial de Temporizadores Estándar:</h2>"
        if temporizadores:
            texto += "<ul>"
            for temporizador in temporizadores:
                texto += f"<li>ID: {temporizador[0]}, Duración: {temporizador[1]} segundos, Iniciado en: {temporizador[2]}</li>"
            texto += "</ul>"
        else:
            texto += "<p>No hay temporizadores estándar registrados.</p>"

        self.label_temporizadores_estandar.setText(texto)

    def mostrar_temporizadores_pomodoro(self):
        conn = sqlite3.connect('examen_final_temporizadores.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM temporizadores_pomodoro')
        pomodoros = cursor.fetchall()

        conn.close()

        texto = "<h2>Historial de Temporizadores Pomodoro:</h2>"
        if pomodoros:
            texto += "<ul>"
            for pomodoro in pomodoros:
                texto += f"<li>ID: {pomodoro[0]}, Duración de Trabajo: {pomodoro[1]} segundos, Duración de Descanso: {pomodoro[2]} segundos, Ciclos: {pomodoro[3]}, Iniciado en: {pomodoro[4]}</li>"
            texto += "</ul>"
        else:
            texto += "<p>No hay temporizadores Pomodoro registrados.</p>"

        self.label_temporizadores_pomodoro.setText(texto)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HistorialWindow()
    window.show()
    sys.exit(app.exec_())
