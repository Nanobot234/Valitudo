from Database import Database
from DataClasses import *

'''THis is a file where we can use the databsse created  in Database.py'''

database = Database(':memory:')

patientid = database.generateRandomId()
firstPatient  = Patient(patientid,"John","Doe","2/3/1999",34,"Male","2350 Main Street")
database.insertNewPatient(firstPatient)

database.printAllPatients()









