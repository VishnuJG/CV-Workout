import sqlite3
import os
from datetime import date

# to get the current working directory
directory = os.getcwd()

# con = sqlite3.connect(directory+'\\test.db')
# cursor = con.cursor()


# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(cursor.fetchall())

# cursor.execute("SELECT * FROM Profiles;")
# for row in cursor:
#     print ("USERNAME = ", row[0])
#     print ("AGE = ", row[1])
#     print ("EMAIL = ", row[2])
#     print ("ARML = ", row[3])
#     print ("ARMR = ", row[4])
#     print ("LEGL = ", row[5])
#     print ("LEGR = ", row[6], "\n")


# con.execute('''CREATE TABLE Profiles
#          (USERNAME TEXT PRIMARY KEY NOT NULL,
#          AGE INT,
#          EMAIL varchar(200),
#          ARML INT,
#          ARMR INT,
#          LEGL INT,
#          LEGR INT);''')
# con.commit()


# con.execute("INSERT into Profiles (USERNAME, AGE, EMAIL, ARML, ARMR, LEGL, LEGR) VALUES ('Vishnu J G', 21, 'jgvishnu2001@gmail.com',0,0,0,0);")
# con.commit()

# print(cursor.fetchall())


# con.execute("drop table Profiles;")
# con.commit()


# con.execute("DELETE from Profiles;")
# con.commit()
# con.close()


# to get the current working directory
# directory = os.getcwd()
# con = sqlite3.connect(directory+'\\test.db')

# cursor = con.cursor()


def dbHealthCheck():

    con = sqlite3.connect(directory+'\\test.db')
    cursor = con.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    x=cursor.fetchall()
    if ('Profiles',) not in x:
        con.execute('''CREATE TABLE Profiles
                 (USERNAME TEXT PRIMARY KEY NOT NULL,
                 AGE INT,
                 EMAIL varchar(200));''')
        con.commit()
    else:
        return


# dbHealthCheck()


def dbVerificationfun(inp_val):
    directory = os.getcwd()
    con = sqlite3.connect(directory+'\\test.db')

    cursor = con.cursor()
    cursor.execute("SELECT * FROM Profiles;")
    for row in cursor:
        if inp_val in row:
            return row[2]
    return None

# print(dbVerificationfun("Tejas D R"))


def dbUpdatefun(inp_uname, update_key, update_val):
    con = sqlite3.connect(directory+'\\test.db')

    cursor = con.cursor()
    tdate = str(date.today())
    cursor.execute(
        f"SELECT * FROM '{inp_uname}_stats' WHERE Date=?;", (tdate,))
    if(cursor.fetchone()):
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

def dbUpdatefunsetting(inp_uname, update_key, update_val):
    con = sqlite3.connect(directory+'\\test.db')

    cursor = con.cursor()
    tdate = str(date.today())
    cursor.execute(
        f"SELECT * FROM '{inp_uname}_stats' WHERE Date=?;", (tdate,))
    if(cursor.fetchone()):
        if("min" in update_key):
            cursor.execute(
                f"UPDATE '{inp_uname}_stats' SET {update_key} =  ? WHERE Date = ?;", (update_val, tdate))
            con.commit()
        elif("max" in update_key):
            cursor.execute(
                f"UPDATE '{inp_uname}_stats' SET {update_key} =  ? WHERE Date = ? AND {update_key}<?;", (update_val, tdate, update_val))
            con.commit()
    else:
        cursor.execute(
            f"INSERT INTO '{inp_uname}_stats' VALUES(?,0,0,0,0,0,0,0,0,0,0,0,0);", (tdate,))
        cursor.execute(
            f"UPDATE '{inp_uname}_stats' SET {update_key} =  ? WHERE Date = ?;", (update_val, tdate))
        con.commit()
    con.close()


def dbInfofun():
    pass


def dbgetinfo(uname, getval):
    con = sqlite3.connect(directory+'\\test.db')
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM '{uname}_stats';")
    temp = []
    for i in cursor:
        temp.append(i)
    x = [i[0] for i in temp]
    if(getval == 'armreps'):
        
        ly = [i[1] for i in temp]
        ry = [i[2] for i in temp]
        lmax = [i[5] for i in temp]
        lmin = [i[6] for i in temp]
        rmax = [i[7] for i in temp]
        rmin = [i[8] for i in temp]
        # pass
    if(getval == 'legcurls'):
        ly = [i[3] for i in temp]
        ry = [i[4] for i in temp]
        lmax = [i[9] for i in temp]
        lmin = [i[10] for i in temp]
        rmax = [i[11] for i in temp]
        rmin = [i[12] for i in temp]
        # pass
    return x, ly, ry, lmax, lmin, rmax, rmin


def dbNewUserfun(inp_username, inp_age, inp_email):

    con = sqlite3.connect(directory+'\\test.db')
    cursor = con.cursor()
    con.execute("INSERT INTO Profiles (USERNAME, AGE, EMAIL) VALUES (?, ?, ?);",
                (inp_username, inp_age, inp_email))

    user_name = inp_username + "_stats"
    con.execute(f"CREATE TABLE '{inp_username}_stats' (Date DATE, armreps_left int, armreps_right int, legcurls_left int, legcurls_right int, armleft_maxangle int, armleft_minangle int, armright_maxangle int, armright_minangle int, legleft_maxangle int, legleft_minangle int, legright_maxangle int, legright_minangle int);")
    con.commit()
    con.close()

# dbNewUserfun("Vishnu J G", 21, "jgvishnu2001@gmail.com")
# dbHealthCheck()



def testingFun():
    print(directory)
    con = sqlite3.connect(directory+'\\test.db')

    cursor = con.cursor()
    name = "Tejas D R"
    cursor.execute(f"SELECT * FROM Profiles;")
    for row in cursor:
        print("Hi")
        print("USERNAME = ", row[0])
        print("AGE = ", row[1])
        print("EMAIL = ", row[2])
testingFun()
