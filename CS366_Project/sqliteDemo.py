import sqlite3

#conn=sqlite3.connect(':memory:')
conn=sqlite3.connect('patient.db')

#create cursor
c=conn.cursor()

#now using cursor we can run the SQL statements

# c.execute("""CREATE TABLE patients (
#    Id INT,
#    first TEXT,
#    last TEXT,
#    gender TEXT,
#    date_of_birth DATE
    
#    )""")


c.execute("INSERT INTO patients VALUES(1,'sam','Doe','Male',03-03-1999)")
conn.commit()
c.execute("SELECT * FROM patients WHERE last='Doe'")

#c.fetchone()#only return one row but if no row avail then return NULL
#c.fetchmany(5)#would return 5 rows as a list, if no row avail 
              #return an empty list

#c.fetchall()

print(c.fetchall())
conn.commit()

#close 
conn.close()
