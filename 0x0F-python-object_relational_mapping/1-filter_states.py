#!/usr/bin/python3
"""Script to filter states from an SQL table"""


from sys import argv
import MySQLdb


if __name__ == '__main__':
    user = argv[1]
    pwd = argv[2]
    dbname = argv[3]

    dbase = MySQLdb.connect(host="localhost",
                            port=3306,
                            user=user,
                            passwd=pwd,
                            db=dbname)
    cursor = dbase.cursor()
    cursor.execute("SELECT * FROM states WHERE name \
    LIKE BINARY 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    dbase.close()
