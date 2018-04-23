#reminder: create genericlist class / definition to occupy the class account
#reminder: create a function to input new accounts

class Values(object):
    def genericlist():
        lID = "testingID"
        lPW = "password"
        firstname = "Andrew"    
        lastname = "Hernandez" 
        birthday = "June 14 1999"
        email = "jonandrew@outlook.com"


class Account(genericlist.Values): #upon startup will automatically create a "table" from the genericlist class
    def __init__(self, lID='0', lPW='0', fName='0', lName='0', birthday='0', email='0'):
        self.lId = lID
        self.lPW = lPW
        self.fName = firstname
        self.lName = lastname
        self.birthday = birthday
        self.email = email

    def createAccount(): #creates a new account
