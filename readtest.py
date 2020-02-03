import psycopg2
import sys


con = None

try:
    con = psycopg2.connect("host='localhost' dbname='testdb' user='pythonspot' password='Dimas98@srg'")
    cur = con.cursor()
    cur.execute("SELECT * FROM snmptest")


    while True:
        row = cur.fetchone()
        print(row)

        if row == None:
            break

        print("Product: " + row[1] + "\t\t\tPrice: " + str(row[2]))

except psycopg2.DatabaseError as e:
    if con:
        con.rollback()

    print 'Error %s' % e
    sys.exit(1)

finally:
    if con:
        con.close()