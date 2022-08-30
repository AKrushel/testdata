import psycopg2
conn = psycopg2.connect(database="postgres",
                        user='admin', password='p8ASJQDA)4Pnt&(',
                        host='localhost', port='5432')
cur = conn.cursor()
with open('user_accounts.csv', 'r') as f:
    next(f)
    cur.copy_from(f, 'users', sep=',')

conn.commit()
