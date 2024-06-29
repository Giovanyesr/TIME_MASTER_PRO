import sqlite3

class Historial:
    def __init__(self, db_file='examen_final_temporizadores.db'):
        self.db_file = db_file

    def mostrar_alarmas(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM alarms')
        alarmas = cursor.fetchall()

        conn.close()

        print("Historial de Alarmas:")
        for alarma in alarmas:
            print(f"ID: {alarma[0]}, Hora de Alarma: {alarma[1]}, Creado en: {alarma[2]}")

    def mostrar_temporizadores_estandar(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM temporizadores_estandar')
        temporizadores = cursor.fetchall()

        conn.close()

        print("Historial de Temporizadores Estándar:")
        for temporizador in temporizadores:
            print(f"ID: {temporizador[0]}, Duración: {temporizador[1]} segundos, Iniciado en: {temporizador[2]}")

    def mostrar_temporizadores_pomodoro(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM temporizadores_pomodoro')
        pomodoros = cursor.fetchall()

        conn.close()

        print("Historial de Temporizadores Pomodoro:")
        for pomodoro in pomodoros:
            print(f"ID: {pomodoro[0]}, Duración de Trabajo: {pomodoro[1]} segundos, Duración de Descanso: {pomodoro[2]} segundos, Ciclos: {pomodoro[3]}, Iniciado en: {pomodoro[4]}")

if __name__ == '__main__':
    historial = Historial()
    historial.mostrar_alarmas()
    historial.mostrar_temporizadores_estandar()
    historial.mostrar_temporizadores_pomodoro()
