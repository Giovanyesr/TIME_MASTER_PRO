import sqlite3
from datetime import datetime

class Alarm:
    def __init__(self, id=None, alarm_time=None, created_at=None):
        self.id = id
        self.alarm_time = alarm_time
        self.created_at = created_at if created_at else datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def save_to_db(self):
        conn = sqlite3.connect('examen_final_temporizadores.db')
        cursor = conn.cursor()
        if self.id:
            cursor.execute('UPDATE alarms SET alarm_time=?, created_at=? WHERE id=?',
                           (self.alarm_time, self.created_at, self.id))
        else:
            cursor.execute('INSERT INTO alarms (alarm_time, created_at) VALUES (?, ?)',
                           (self.alarm_time, self.created_at))
            self.id = cursor.lastrowid
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_alarms():
        conn = sqlite3.connect('examen_final_temporizadores.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM alarms')
        alarms = cursor.fetchall()
        conn.close()
        return [Alarm(id=row[0], alarm_time=row[1], created_at=row[2]) for row in alarms]

    @staticmethod
    def get_alarm_by_id(alarm_id):
        conn = sqlite3.connect('examen_final_temporizadores.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM alarms WHERE id=?', (alarm_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Alarm(id=row[0], alarm_time=row[1], created_at=row[2])
        return None

    def delete(self):
        conn = sqlite3.connect('examen_final_temporizadores.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM alarms WHERE id=?', (self.id,))
        conn.commit()
        conn.close()
