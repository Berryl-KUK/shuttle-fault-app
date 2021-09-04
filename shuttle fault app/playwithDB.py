import sqlite3

conn = sqlite3.connect('srcappdb.db')

c = conn.cursor()

# c.execute("""CREATE TABLE src_errors (
#            ERROR_CODE text,
#            MESSAGE text,
#            CAUSE text,
#            RESOLUTION text
#            )""")


c.execute("""INSERT INTO src_errors VALUES (
            'M-AOP-OPLC-0101',
            'Emergency stop for rack line.',
            'Emergency stop for rack line is active. Error in emergency circuit.', 
            'Determine and rectify cause of emergency stop. Deactivate emergency stop button. Acknowledge emergency stop with momentary key switch. Check cabling.'
            )""")

# c.execute("select * from src_errors")
# print(c.fetchall())

#c.execute("drop table src_errors")
conn.commit()

conn.close()



