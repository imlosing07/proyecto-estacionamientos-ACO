import sqlite3
import random
from config import NOMBRE_BD

# Conectar a la base de datos
conn = sqlite3.connect(NOMBRE_BD)
cursor = conn.cursor()
print("Iniciando ....")
# Consultar las filas para asegurarse de que existen datos
cursor.execute("SELECT COUNT(*) FROM estacionamiento")
total_filas = cursor.fetchone()[0]

if total_filas > 0:
    # Actualizar los valores de la columna 'plaza' con números aleatorios entre 10 y 20
    cursor.execute("SELECT id FROM estacionamiento")  # Suponiendo que tienes una columna 'id'
    filas = cursor.fetchall()
    
    for fila in filas:
        nuevo_valor = random.randint(10, 20)
        cursor.execute("UPDATE estacionamiento SET plaza = ? WHERE id = ?", (nuevo_valor, fila[0]))
    
    # Guardar los cambios
    conn.commit()
    print("Los valores de la columna 'plaza' han sido actualizados.")
else:
    print("No hay datos en la tabla para actualizar.")

# Cerrar la conexión
conn.close()

