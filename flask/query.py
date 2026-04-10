import sqlite3

def executar_query(query, *args, fetch=False, commit=False):
    conn = sqlite3.connect('estoque_papelaria.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    resultado = None
    
    try:
        cursor.execute(query, args)
        
        if commit:
            conn.commit()
        if fetch:
            resultado = cursor.fetchall()
    finally:
        conn.close()
    
    return resultado