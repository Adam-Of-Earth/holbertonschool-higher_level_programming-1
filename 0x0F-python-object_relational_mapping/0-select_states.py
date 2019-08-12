#!/usr/bin/python3
"""Script to lists all states form a db"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    user = argv[1]
    pwd = argv[2]
    dbname = argv[3]

    dbase = MySQLdb.connect(host="localhost",
                            port=3306,
                            user=user,
                            passwd=pwd,
                            db=dbname)
    cursor = dbase.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print("{}".format(row))
    cursor.close()
    dbase.close()
