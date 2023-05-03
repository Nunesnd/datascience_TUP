import psycopg2

def inserir_postgre(cidade, estado, vitimas):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="desafio_21_dias",
        user="postgres",
        password="D1360nun#$"
    )
    
    cursor = conn.cursor()
    query = f"INSERT INTO vitimas_covid (cidade, estado, vitimas) VALUES ('{cidade}', '{estado}', {vitimas})"
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
    
    