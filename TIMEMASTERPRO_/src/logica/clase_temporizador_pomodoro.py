import sqlite3
from datetime import datetime

class Pomodoro:
    def __init__(self, id=None, work_duration=None, break_duration=None, cycles=None, started_at=None):
        self.id = id
        self.work_duration = work_duration
        self.break_duration = break_duration
        self.cycles = cycles
        self.started_at = started_at if started_at else datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def connect():
        return sqlite3.connect('examen_final_temporizadores.db')

    def save_to_db(self):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            if self.id:
                cursor.execute('UPDATE temporizadores_pomodoro SET work_duration=?, break_duration=?, cycles=?, started_at=? WHERE id=?',
                               (self.work_duration, self.break_duration, self.cycles, self.started_at, self.id))
            else:
                cursor.execute('INSERT INTO temporizadores_pomodoro (work_duration, break_duration, cycles, started_at) VALUES (?, ?, ?, ?)',
                               (self.work_duration, self.break_duration, self.cycles, self.started_at))
                self.id = cursor.lastrowid
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error SQLite: {e}")
        finally:
            conn.close()

    @staticmethod
    def get_all_pomodoros():
        try:
            conn = Pomodoro.connect()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM temporizadores_pomodoro')
            pomodoros = cursor.fetchall()
            return [Pomodoro(id=row[0], work_duration=row[1], break_duration=row[2], cycles=row[3], started_at=row[4]) for row in pomodoros]
        except sqlite3.Error as e:
            print(f"Error SQLite: {e}")
            return []
        finally:
            conn.close()

    @staticmethod
    def get_pomodoro_by_id(pomodoro_id):
        try:
            conn = Pomodoro.connect()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM temporizadores_pomodoro WHERE id=?', (pomodoro_id,))
            row = cursor.fetchone()
            if row:
                return Pomodoro(id=row[0], work_duration=row[1], break_duration=row[2], cycles=row[3], started_at=row[4])
            return None
        except sqlite3.Error as e:
            print(f"Error SQLite: {e}")
            return None
        finally:
            conn.close()

    def delete(self):
        try:
            conn = Pomodoro.connect()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM temporizadores_pomodoro WHERE id=?', (self.id,))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error SQLite: {e}")
        finally:
            conn.close()

if __name__ == "__main__":
    try:
        # Ejemplo de uso para probar la clase Pomodoro
        # Crear una instancia de Pomodoro y guardarla en la bd
        pomodoro = Pomodoro(work_duration=25*60, break_duration=5*60, cycles=4)
        pomodoro.save_to_db()

        # Obtener todos los pomodoros desde la bd
        pomodoros = Pomodoro.get_all_pomodoros()
        for p in pomodoros:
            print(f"Pomodoro ID: {p.id}, Work Duration: {p.work_duration}, Break Duration: {p.break_duration}, Cycles: {p.cycles}, Started At: {p.started_at}")

        # Ejemplo de obtener un Pomodoro por su ID
        pomodoro_id = 1  # ID del Pomodoro a obtener
        p = Pomodoro.get_pomodoro_by_id(pomodoro_id)
        if p:
            print(f"Pomodoro encontrado - ID: {p.id}, Work Duration: {p.work_duration}, Break Duration: {p.break_duration}, Cycles: {p.cycles}, Started At: {p.started_at}")
        else:
            print(f"No se encontró Pomodoro con ID {pomodoro_id}")
    except sqlite3.Error as e:
        print(f"Error SQLite: {e}")
