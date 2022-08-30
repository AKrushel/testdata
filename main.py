import psycopg2
conn = psycopg2.connect(database="postgres",
                        user='admin', password='p8ASJQDA)4Pnt&(',
                        host='localhost', port='5432')

cur = conn.cursor()

sql = '''CREATE TABLE DETAILS(i int NOT NULL,\
c1 char(20),\
c2 float,
c3 float,
c4 float,
c5 float,
c6 float,
c7 float,
c8 float,
c9 float,
c10 float,
c11 float,
c12 float,
c13 float,
c14 float,
c15 float,
c16 float,
c17 float,
c18 float,
c19 float,
c20 float,
c21 float,
c22 float,
c23 float,);'''

cur.execute(sql)

with open('testdata.csv', 'r') as f:
    next(f)
    cur.copy_from(f, 'users', sep=',')

conn.commit()
