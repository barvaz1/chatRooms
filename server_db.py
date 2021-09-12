import sqlite3
from sqlite3 import Error

SUCCESS = "success"

NAME = "name"


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


###################################################
# Entry claim: All information about the new user
# Exit claim: Error Message, or userName
###################################################
def create_user(conn, user):
    # is the user is ok?
    msg = check_user(conn, user)
    if msg != SUCCESS:
        return msg

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

    sql = sql.format(user[0], user[1], user[2], user[3], user[4], user[5])

    cur = conn.cursor()

    cur.execute(sql)

    conn.commit()
    # cur.lastrowid
    # return the name(cmd) and usrName
    return NAME + " " + user[0]


def check_user(conn, user):
    # check if the user name existsin the data base
    sql = """SELECT usrID FROM USERS WHERE usrID = '{}' LIMIT 1"""
    sql = sql.format(user[0])
    cur = conn.cursor()
    print(cur.execute(sql).fetchall())

    if cur.execute(sql).fetchall():
        return "user name exists"

    # check if the user name exists in the data base
    sql = """SELECT usrID FROM USERS WHERE usrEmail = '{}' LIMIT 1"""
    sql = sql.format(user[3])
    cur = conn.cursor()
    print(cur.execute(sql).fetchall())

    if cur.execute(sql).fetchall():
        return "user email exists"

    # check if the user number exists in the data base
    sql = """SELECT usrID FROM USERS WHERE usrMobileNumber = '{}' LIMIT 1"""
    sql = sql.format(user[4])
    cur = conn.cursor()
    print(cur.execute(sql).fetchall())

    if cur.execute(sql).fetchall():
        print("user mobile number exists")
        return "user mobile number exists"

    return SUCCESS


def check_password(conn, user_name, password):
    sql = """SELECT usrPWD FROM USERS WHERE usrID = '{}'  LIMIT 1"""
    sql = sql.format(user_name)
    cur = conn.cursor()
    answer = cur.execute(sql).fetchall()

    if answer[0][0] == password:
        return NAME + " " + user_name
    return "check your password"


if __name__ == '__main__':
    create_connection(r"Users.db")
