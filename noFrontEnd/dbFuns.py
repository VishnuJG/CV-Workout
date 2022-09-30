import sqlite3
import os

#to get the current working directory
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




#to get the current working directory
# directory = os.getcwd()
# con = sqlite3.connect(directory+'\\test.db')

# cursor = con.cursor()


def dbVerificationfun(inp_val):
    directory = os.getcwd()
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
    cursor.execute(f"UPDATE Profiles SET {update_key} = {update_key} + ? WHERE USERNAME = ?;", ( update_val, inp_uname))
    con.commit()
    con.close()

def dbInfofun():
    pass


def dbNewUserfun(inp_username, inp_age, inp_email):
    
    con = sqlite3.connect(directory+'\\test.db')

    cursor = con.cursor()
    con.execute("INSERT into Profiles (USERNAME, AGE, EMAIL, ARML, ARMR, LEGL, LEGR) VALUES (?, ?, ?, 0, 0, 0, 0);", (inp_username, inp_age, inp_email))
    con.commit()
    con.close()



def testingFun():
    
    con = sqlite3.connect(directory+'\\test.db')

    cursor = con.cursor()
    cursor.execute("SELECT * FROM Profiles;")
    for row in cursor:
        print("Hi")
        print ("USERNAME = ", row[0])
        print ("AGE = ", row[1])
        print ("EMAIL = ", row[2])
        print ("ARML = ", row[3])
        print ("ARMR = ", row[4])
        print ("LEGL = ", row[5])
        print ("LEGR = ", row[6], "\n")
    con.close()

# dbUpdatefun("admin", "ARML", 10)
testingFun()
