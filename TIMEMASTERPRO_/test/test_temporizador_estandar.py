import sys
import unittest
import sqlite3
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtMultimedia import QSound
from unittest.mock import patch, MagicMock
from src.logica.clase_temporizador_estandar import TemporizadorEstandar
from src.logica.temporizador_estandar import TemporizadorEstandarApp

class TestTemporizadorEstandarApp(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])  # Inicializar QApplication para las pruebas
        self.window = TemporizadorEstandarApp()  # Crear una instancia de la aplicación

    @patch.object(QSound, 'play')
    def test_play_sound(self, mock_play):
        self.window.play_sound()
        mock_play.assert_called_once()  # Verificar que QSound.play fue llamado una vez

    def test_start_timer(self):
        # Simular clic en el botón de inicio y verificar el estado del temporizador
        self.window.ui.totalTimeSpinBox.setValue(60)  # Configurar 60 segundos
        self.window.start_timer()

        self.assertTrue(self.window.is_running)  # Verificar que el temporizador está corriendo
        self.assertEqual(self.window.time_left, QTime(0, 1, 0))  # Verificar tiempo restante

        # Verificar que se intentó guardar el temporizador en la base de datos
        try:
            conn = sqlite3.connect('examen_final_temporizadores.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM temporizadores_estandar WHERE duration = 60')
            result = cursor.fetchone()
            conn.close()

            self.assertIsNotNone(result)  # Verificar que se encontró el temporizador en la base de datos

        except sqlite3.Error as e:
            self.fail(f"Error de Base de Datos: {str(e)}")

    def test_pause_resume_timer(self):
        # Simular clic en el botón de inicio y luego pausa y resumen del temporizador
        self.window.ui.totalTimeSpinBox.setValue(60)  # Configurar 60 segundos
        self.window.start_timer()

        self.window.pause_timer()
        self.assertFalse(self.window.is_running)  # Verificar que el temporizador está pausado

        self.window.resume_timer()
        self.assertTrue(self.window.is_running)  # Verificar que el temporizador se reanudó correctamente

    def test_reset_timer(self):
        # Simular clic en el botón de inicio y luego reiniciar el temporizador
        self.window.ui.totalTimeSpinBox.setValue(60)  # Configurar 60 segundos
        self.window.start_timer()

        self.window.reset_timer()
        self.assertFalse(self.window.is_running)  # Verificar que el temporizador está detenido
        self.assertEqual(self.window.time_left, QTime(0, 0))  # Verificar que el tiempo restante se reinició

    def tearDown(self):
        self.window.close()  # Cerrar la ventana al finalizar las pruebas
        self.app.quit()  # Cerrar QApplication

if __name__ == '__main__':
    unittest.main()
