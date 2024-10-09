from classes import *
import psycopg2 as sql

if __name__ == '__main__':
    conn = sql.connect("dbname=711Python user=root password=root")
    cur = conn.cursor()


    # cur.execute("DELETE FROM usagers WHERE id='U'")
    cur.execute("INSERT INTO test (id) VALUES (%s)", (28,))
    #data = cur.execute("SELECT * FROM public.usagers")
    #data = cur.fetchall()

    conn.commit()
    cur.close()
    conn.close()