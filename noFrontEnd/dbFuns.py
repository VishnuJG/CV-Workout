import sqlite3
import os
from datetime import date

# to get the current working directory
directory = os.getcwd()


def dbHealthCheck():
    con = sqlite3.connect(directory+'\\test.db')
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    x = cursor.fetchall()
    if ('Profiles',) not in x:
        con.execute('''CREATE TABLE Profiles
                 (USERNAME TEXT PRIMARY KEY NOT NULL,
                 AGE INT,
                 EMAIL varchar(200));''')
        con.commit()
    con.close()


def dbVerificationfun(inp_val):
    con = sqlite3.connect(directory+'\\test.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Profiles;")
    for row in cursor:
        if inp_val in row:
            return row[2]
    return None


def dbUpdatefun(inp_uname, update_key, update_val):
    con = sqlite3.connect(directory+'\\test.db')
    cursor = con.cursor()
    tdate = str(date.today())
    cursor.execute(
        f"SELECT * FROM '{inp_uname}_stats' WHERE Date=?;", (tdate,))
    if cursor.fetchone():
        cursor.execute(
            f"UPDATE '{inp_uname}_stats' SET {update_key} = {update_key} + ? WHERE Date = ?;", (update_val, tdate))
        con.commit()
    else:
        cursor.execute(
            f"INSERT INTO '{inp_uname}_stats' VALUES(?,0,0,0,0,0,0,0,0,0,0,0,0);", (tdate,))
        cursor.execute(
            f"UPDATE '{inp_uname}_stats' SET {update_key} = {update_key} + ? WHERE Date = ?;", (update_val, tdate))
        con.commit()
    con.close()


def dbNewUserfun(inp_username, inp_age, inp_email):
    con = sqlite3.connect(directory+'\\test.db')
    cursor = con.cursor()
    con.execute("INSERT INTO Profiles (USERNAME, AGE, EMAIL) VALUES (?, ?, ?);",
                (inp_username, inp_age, inp_email))
    user_name = inp_username + "_stats"
    con.execute(f"CREATE TABLE '{inp_username}_stats' (Date DATE, armreps_left int, armreps_right int, legcurls_left int, legcurls_right int, armleft_maxangle int, armleft_minangle int, armright_maxangle int, armright_minangle int, legleft_maxangle int, legleft_minangle int, legright_maxangle int, legright_minangle int);")
    con.commit()
    con.close()
