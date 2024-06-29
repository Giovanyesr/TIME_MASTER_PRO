import sys
import unittest
import os
import sqlite3
from PyQt5.QtWidgets import QApplication
from src.logica.clase_alarma import Alarm
from src.interface.ui_alarma import AlarmUI

class TestAlarm(unittest.TestCase):
    def setUp(self):
        # Asegurar que la base de datos esté en la misma ubicación que las pruebas
        current_dir = os.path.dirname(__file__)  # Directorio actual de las pruebas
        db_path = os.path.join(current_dir, '../src/logica/examen_final_temporizadores.db')

        # Inicializar la base de datos y la tabla alarms si no existen
        self.db_path = db_path
        self.initialize_database()

        # Inicializar QApplication para las pruebas
        self.app = QApplication([])  # [] es necesario para PyQt5

        # Ejemplo de configuración inicial de una alarma
        self.test_alarm_time = '12:00:00'
        self.test_alarm = Alarm(alarm_time=self.test_alarm_time)

    def initialize_database(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alarms (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                alarm_time TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def test_save_to_db(self):
        self.test_alarm.save_to_db()
        saved_alarm = Alarm.get_alarm_by_id(self.test_alarm.id)
        self.assertIsNotNone(saved_alarm)
        self.assertEqual(saved_alarm.alarm_time, self.test_alarm_time)

    # Puedes agregar más pruebas según sea necesario...

    def tearDown(self):
        # Finalizar la aplicación al finalizar las pruebas
        self.app.quit()

if __name__ == '__main__':
    unittest.main()
