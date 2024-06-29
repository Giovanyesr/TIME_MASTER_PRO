import sys
import unittest
import sqlite3
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtMultimedia import QSound
from unittest.mock import patch
from datetime import datetime
from src.logica.clase_temporizador_pomodoro import Pomodoro
from src.logica.temporizador_pomodoro import PomodoroTimer

class TestPomodoroTimer(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])  # Inicializar QApplication para las pruebas
        self.window = PomodoroTimer()  # Crear una instancia de PomodoroTimer

    @patch.object(QSound, 'play')
    def test_play_sound(self, mock_play):
        self.window.play_sound()
        mock_play.assert_called_once()  # Verificar que QSound.play fue llamado una vez

    def test_start_timer(self):
        # Simular clic en el botón de inicio y verificar el estado del temporizador
        self.window.ui.totalTimeSpinBox.setValue(120)  # Total de segundos
        self.window.ui.workTimeSpinBox.setValue(60)    # Tiempo de trabajo en segundos
        self.window.ui.breakTimeSpinBox.setValue(30)   # Tiempo de descanso en segundos

        self.window.start_timer()

        self.assertTrue(self.window.is_running)  # Verificar que el temporizador está corriendo
        self.assertTrue(self.window.is_working)  # Verificar que está en modo de trabajo inicialmente
        self.assertEqual(self.window.time_left, QTime(0, 1, 0))  # Verificar tiempo de trabajo inicial

        # Verificar que se intentó guardar el Pomodoro en la base de datos
        try:
            conn = sqlite3.connect('examen_final_temporizadores.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM temporizadores_pomodoro WHERE cycles = 0')
            result = cursor.fetchone()
            conn.close()



        except sqlite3.Error as e:
            self.fail(f"Error de Base de Datos: {str(e)}")

    def test_pause_resume_timer(self):
        # Simular clic en el botón de inicio y luego pausa y resumen del temporizador
        self.window.ui.totalTimeSpinBox.setValue(120)  # Total de segundos
        self.window.ui.workTimeSpinBox.setValue(60)    # Tiempo de trabajo en segundos
        self.window.ui.breakTimeSpinBox.setValue(30)   # Tiempo de descanso en segundos

        self.window.start_timer()
        self.window.pause_timer()

        self.assertFalse(self.window.is_running)  # Verificar que el temporizador está pausado
        self.assertTrue(self.window.is_paused)   # Verificar que está en estado de pausa

        self.window.resume_timer()

        self.assertTrue(self.window.is_running)  # Verificar que el temporizador se reanudó correctamente
        self.assertFalse(self.window.is_paused)  # Verificar que ya no está en estado de pausa

    def test_reset_timer(self):
        # Simular clic en el botón de inicio y luego reiniciar el temporizador
        self.window.ui.totalTimeSpinBox.setValue(120)  # Total de segundos
        self.window.ui.workTimeSpinBox.setValue(60)    # Tiempo de trabajo en segundos
        self.window.ui.breakTimeSpinBox.setValue(30)   # Tiempo de descanso en segundos

        self.window.start_timer()
        self.window.reset_timer()

        self.assertFalse(self.window.is_running)  # Verificar que el temporizador está detenido
        self.assertFalse(self.window.is_paused)   # Verificar que no está en estado de pausa
        self.assertEqual(self.window.cycles, 0)   # Verificar que los ciclos se han reiniciado

    def tearDown(self):
        self.window.close()  # Cerrar la ventana al finalizar las pruebas
        self.app.quit()      # Cerrar QApplication

if __name__ == '__main__':
    unittest.main()
