#!/usr/bin/python3
"""Module to filter states by user"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    user = argv[1]
    pwd = argv[2]
    dbname = argv[3]
    sname = argv[4]

    dbase = MySQLdb.connect(host="localhost",
                            port=3306,
                            user=user,
                            pwd=pwd,
                            db=dbname)

    cursor = dbase.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name \
        LIKE BINARY '{}' ORDER BY id ASC".format(sname))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    dbase.close()
