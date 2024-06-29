import sys
import unittest
import sqlite3
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from src.logica.historial import HistorialWindow

class TestHistorialWindow(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])  # Inicializar QApplication para las pruebas


        self.window = HistorialWindow()

    def test_mostrar_alarmas(self):
        # Simular la selección de la opción de Alarmas en el combo box
        self.window.combo_box.setCurrentIndex(0)
        QTest.qWait(100)  # Esperar un breve momento para que se actualice la interfaz

        # Obtener el texto mostrado en la etiqueta de alarmas
        displayed_text = self.window.label_alarmas.text()

        # Conectar a la base de datos y obtener las alarmas registradas
        conn = sqlite3.connect('examen_final_temporizadores.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM alarms')
        alarms = cursor.fetchall()
        conn.close()

        # Verificar que el texto mostrado coincide con los datos de la base de datos
        if alarms:
            for alarma in alarms:
                self.assertIn(f'ID: {alarma[0]}, Hora de Alarma: {alarma[1]}, Creado en: {alarma[2]}', displayed_text)
        else:
            self.assertIn('No hay alarmas registradas.', displayed_text)

    def test_mostrar_temporizadores_estandar(self):
        # Simular la selección de la opción de Temporizadores Estándar en el combo box
        self.window.combo_box.setCurrentIndex(1)
        QTest.qWait(100)  # Esperar un breve momento para que se actualice la interfaz

        # Obtener el texto mostrado en la etiqueta de temporizadores estándar
        displayed_text = self.window.label_temporizadores_estandar.text()

        # Conectar a la base de datos y obtener los temporizadores estándar registrados
        conn = sqlite3.connect('examen_final_temporizadores.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM temporizadores_estandar')
        temporizadores = cursor.fetchall()
        conn.close()

        # Verificar que el texto mostrado coincide con los datos de la base de datos
        if temporizadores:
            for temporizador in temporizadores:
                self.assertIn(f'ID: {temporizador[0]}, Duración: {temporizador[1]} segundos, Iniciado en: {temporizador[2]}', displayed_text)
        else:
            self.assertIn('No hay temporizadores estándar registrados.', displayed_text)

    def test_mostrar_temporizadores_pomodoro(self):
        # Simular la selección de la opción de Temporizadores Pomodoro en el combo box
        self.window.combo_box.setCurrentIndex(2)
        QTest.qWait(100)  # Esperar un breve momento para que se actualice la interfaz

        # Obtener el texto mostrado en la etiqueta de temporizadores Pomodoro
        displayed_text = self.window.label_temporizadores_pomodoro.text()

        # Conectar a la base de datos y obtener los temporizadores Pomodoro registrados
        conn = sqlite3.connect('examen_final_temporizadores.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM temporizadores_pomodoro')
        pomodoros = cursor.fetchall()
        conn.close()

        # Verificar que el texto mostrado coincide con los datos de la base de datos
        if pomodoros:
            for pomodoro in pomodoros:
                self.assertIn(f'ID: {pomodoro[0]}, Duración de Trabajo: {pomodoro[1]} segundos, Duración de Descanso: {pomodoro[2]} segundos, Ciclos: {pomodoro[3]}, Iniciado en: {pomodoro[4]}', displayed_text)
        else:
            self.assertIn('No hay temporizadores Pomodoro registrados.', displayed_text)

    def tearDown(self):
        self.window.close()  # Cerrar la ventana al finalizar las pruebas
        self.app.quit()  # Cerrar QApplication

if __name__ == '__main__':
    unittest.main()
