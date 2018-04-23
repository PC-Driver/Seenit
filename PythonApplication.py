#reminder: create genericlist class / definition to occupy the class account
#reminder: create a function to input new accounts


def genericlist():
        #Account generic list
        loginID = "testingID"
        loginPW = "password"
        firstname = "Andrew"    
        lastname = "Hernandez" 
        birthday = "June 14 1999"
        emailaddress = "jonandrew@outlook.com"
        subseenit = 'SJSU - Subseenit'
        
        #subseenit genericlist
        subseenitName ="SJSU - Subseenit"
        subseenitCategory = 'Educational'


class Account(object): #upon startup will automatically create a "table" from the genericlist
    def __init__(self, lID='0', lPW='0', fName='0', lName='0', bday='0', email='0', subbedSS='0'):
        self.lID = loginID
        self.lPW = loginPW
        self.fName = firstname
        self.lName = lastname
        self.bday = birthday
        self.email = emailaddress
        self.subbedSS = subseenit
   # def createSubSeenit():
        #...
    #def joinSubSeenit():
        #...

class subSeenit(object):
    def __init__(self, name='0', category='0'):
        self.name = subseenitName
        self.category = subseenitCategory

   # def createAccount(): #creates a new account
