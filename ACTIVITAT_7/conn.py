# Importo la llibreria
import psycopg2

# Faig l'intent de connexió a la bbdd amb les mateixes dades del fitxer docker-compose  
try:
    # Establecer la conexión a la base de datos
    conn = psycopg2.connect(
        database="dbM7",
        user="abde",
        password="AKAT2016",
        host="localhost",
        port="5432"
    )
    connection = conn.cursor()  # Crear el cursor
    print("Connexió a la base de dades establerta correctament.")
# Si passa un error al intentar connectar-se a la base de dades, s'imprimirà aquest text.
except psycopg2.OperationalError as error:
    print("Error al connectar a la base de dades:", error)
# Si hi ha un error, no es crea la connexió ni el cursor.
# Faig això per evitar errors.
    conn, connection = None, None 
