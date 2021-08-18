import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn

def close_connection(conn):
    if conn:
        conn.close()

def create_user(conn, user):
    """
    Create a new project into the projects table
    :param lst:
    :param conn:
    :param project:
    :return: project id
    """
    sql = """ INSERT INTO USERS (
                      usrID,
                      usrLastName,
                      usrFirstName,
                      usrEmail,
                      usrMobileNumber,
                      usrPWD
                  )
                  VALUES (
                      '{}',
                      '{}',
                      '{}',
                      '{}',
                      '{}',
                      '{}'
                  );"""
    print(1)
    sql = sql.format(user[0], user[1], user[2], user[3], user[4], user[5])
    print(2)
    print(sql)
    print(3)
    cur = conn.cursor()
    print(4)
    cur.execute(sql)
    print(5)
    conn.commit()
    print(6)
    return cur.lastrowid

def check_user(conn, user):
    sql = """SELECT usrID FROM USERS WHERE usrID = 'barvaz12' LIMIT 1"""
    cur = conn.cursor()
    print(cur.execute(sql).fetchall())


    return cur.lastrowid
if __name__ == '__main__':
    create_connection(r"Users.db")

