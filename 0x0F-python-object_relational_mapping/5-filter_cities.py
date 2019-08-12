#!/usr/bin/python3
"""module to list all cities from a db that match argument"""


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
                            passwd=pwd,
                            db=dbname)

    cursor = dbase.cursor()
    cursor.execute(
        "SELECT cities.name FROM cities \
        INNER JOIN states ON states.id = cities.state_id \
        WHERE states.name = %s;", (sname,))
    rows = cursor.fetchall()
    s = []
    for row in rows:
        s.append(row[0])
    print(', '.join(s))
    cursor.close()
    dbase.close()
