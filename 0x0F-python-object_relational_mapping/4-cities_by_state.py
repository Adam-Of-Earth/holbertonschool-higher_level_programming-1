#!/usr/bin/python3
"""Module to list all cities from a SQL database"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    user = argv[1]
    pwd = argv[2]
    dbname = argv[3]
    dbase = MySQLdb.connect(host="localhost",
                            port=3306,
                            user=user,
                            passwd=pwd,
                            db=dbname)

    cursor = dbase.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name \
        FROM cities INNER JOIN states ON states.id = cities.state_id \
        ORDER BY cities.id ASC;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    dbase.close()
